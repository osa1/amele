#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO yeni klasor eklendiginde, recursive ekleme aktifse takibe alinsin
# bir sinif icine almali miyim? sinif kullanmami gerektirecek bir durum yok
# ama yine de duzen acisindan iyi olabilir sanki?

# aslinda burda module singleton gorevi de goruyor, o acidan iyi gibi sanki

import os
import sys
import json
import time
import threading
from fsmonitor import FSMonitorThread, FSEvent

# dict ve list'den eleman alma thread-safe olduguna gore, bunda
# lock kullanmali miyim?
commands = {}
json_path = os.path.join(os.getenv("HOME"), 'dinleyici')
formats = commands.keys()

replace = {'_path_': lambda x: x[0] if not x[0].endswith('/') else x[0][:-1],
           '_name_': lambda x: x[1].rsplit('.', 1)[0],
           '_frm_' : lambda x: file_format(x[1])}

folders = []

monitor = None


def load_json(json_name):
    with open(os.path.join(json_path, json_name), 'r') as f:
        return json.load(f)

def save_json(json_name, data):
    with open(os.path.join(json_path, json_name), 'w') as f:
        json.dump(data, f, indent=4)
    print "saved"

# ilginc `feature`:
# from monitor import * seklinde kullaildiginda, global commands
# monitor.commands oluyor, import ettigim modulun commands'i olmuyor
def load_commands():
    global commands, formats
    commands = load_json('commands.json')
    formats = commands.keys()

def save_commands():
    save_json('commands.json', commands)

def load_folders():
    global folders
    folders = load_json('folders.json')

def save_folders():
    save_json('folders.json', folders)

def add_folder(path, recursive=False):
    """Add path to watched folder list, return false if it's already added."""
    for f in folders:
        # O(n)'de arama, daha mantikli birseyler dusunulebilir
        # yine de zaten birkac klasor olacagindan sorun olacagini sanmiyorum
        if f[0] == path:
            return False
    folders.append((path, recursive))
    save_folders()
    return True

def toggle_folder_recursion(path):
    for f in folders:  # yine lineer arama
        if f[0] == path:
            f[1] = False if f[1] else True

def add_command(frm, cmd):
    global formats

    d = commands.get(frm, [])
    d = commands.setdefault(frm, [])
    if not d:
        formats = commands.keys()
    d.append(cmd)

def remove_command(frm, cmd=None):
    if not cmd:
        del commands[frm]
    else:
        # bu islem thread safe olmayabilir
        commands[frm].remove(cmd)

def remove_folder(folder):
    for i in range(len(folders)):
        if folders[i][0] == folder:
            del folders[i]
            break

def file_format(file):
    return file.split('.')[-1]

def run_commands(fsevent):
    name = fsevent.name
    path = fsevent.path
    frm = file_format(name)

    if frm in formats:
        cmds = commands.get(frm, [])
        for cmd in cmds:
            for r in replace.keys():
                cmd = cmd.replace(r, replace[r]((path, name)))
            print ">> " + cmd
            os.system(cmd)

monitor = None
class Monitor:
    def __init__(self, callback=run_commands):
        self.__monitor = FSMonitorThread(callback)
        self.events = FSEvent.Create | FSEvent.Modify
        self.callback = callback

    def add_dir_watch(self, path, subfolders=False):
        def recursive_adder(path):
            self.__monitor.add_dir_watch(path, self.events)
            print "Adding subfolder: " + path
            for f in os.listdir(path):
                full_path = os.path.join(path, f)
                if os.path.isdir(full_path):
                    recursive_adder(full_path)

        if not subfolders:
            self.__monitor.add_dir_watch(path, self.events)
        else:
            recursive_adder(path)

    def remove_watch(self, path):
        return self.__monitor.remove_watch(path)

    def remove_all_watches(self):
        return self.__monitor.remove_all_watches()

    def run(self):
        return self.__monitor.run()

    def stop(self):
        return self.__monitor.stop()

    def read_events(self):
        return self.__monitor.read_events()

def stop_monitor():
    print "Stopping monitor."
    global monitor
    if monitor:
        monitor.stop()

def start_monitor():
    """Stop monitor (if exists) and start new one."""
    #return # test
    print "Starting new monitor."
    global monitor
    if monitor:
        monitor.stop()
    monitor = Monitor()
    for folder in folders:
        monitor.add_dir_watch(folder[0], folder[1])

def reset_monitor():
    start_monitor()

def test():
    load_folders()
    load_commands()
    start_monitor()
    while True:
        time.sleep(3)
        monitor.read_events()


if __name__ == '__main__':
    test()
