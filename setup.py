#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob

from distutils.core import setup
from distutils.command.build import build
from distutils.command.install import install

os.chdir(os.path.split(os.path.join(os.getcwd(), __file__))[0])

class Build(build):
    def run(self):
        os.system('rm -rf build/')
        os.system('mkdir build')

        os.system('cp -R src/fsmonitor build/')
        os.system('cp -R src/data build/')

        for ui in glob.glob1('src/ui/', '*.ui'):
            os.system('pyuic4 src/ui/%s > build/%s.py' % (ui, ui.split('.')[0]))

        for qrc in glob.glob1('src/data/', '*.qrc'):
            os.system('pyrcc4 src/data/%s > build/data_rc.py' % qrc)

        for py in glob.glob1('src/','*.py'):
            os.system('cp src/%s build/' % py)

class Install(install):
    def run(self):
        if self.root:
            root_dir = '%s/usr' % self.root
        else:
            root_dir = '/usr'
        bin_dir = os.path.join(root_dir, 'bin')
        home_dir = os.getenv('HOME')
        os.system('mkdir %s/amele' % home_dir)

        #os.system('rm -rf %s/amele' % home_dir)
        os.system('cp -R build/* %s/amele' % home_dir)
        os.chmod(os.path.join(home_dir, 'amele/amele.py'), 0755)
        print 'Need root access to create bin(/usr/bin)'
        os.system('sudo ln -s %s %s' % (os.path.join(home_dir, 'amele/amele.py'),
                                        os.path.join(bin_dir, 'amele')))
        print 'Done.'

setup(cmdclass = {'build'  : Build,
                  'install': Install})
