#!/usr/bin/env python3
from lib.database import *
import argparse
import sys
import os

__author__  = 'Regis SENET'
__email__   = 'regis.senet@orhus.fr'
__git__     = 'https://github.com/rsenet/iosEnv'
__version__ = '0.1'
__license__ = 'GPLv3'
__pyver__   = '%d.%d.%d' % sys.version_info[0:3]
short_desc  = "iOS installed application parser"

arg_parser = argparse.ArgumentParser(description=short_desc)
arg_parser.add_argument('--file', help="Specify the applicationState.db file")
arg_parser.add_argument('--app', help="Focus on this specific application")
args = arg_parser.parse_args()

# Get variable
main_file = args.file
application = args.app if args.app is not None else ''

try:
    if main_file:
        if os.path.exists(main_file):
            conn = create_connection(main_file)
            parse_application_state(conn, application)

        else:
            print("[!] %s is not found. Leaving ..." % main_file)

    else:
        arg_parser.print_help()

except KeyboardInterrupt:
    print("\n[x] Leaving ...")
