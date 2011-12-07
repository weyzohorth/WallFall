#!/usr/bin/env python
from sys import argv
import os
os.chdir("/".join(argv[0].replace('\\', '/').split('/')[ : -1]))
from mod.fen import menu
menu.Menu()
