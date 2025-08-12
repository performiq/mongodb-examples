#!/usr/bin/env python3
#
#       Author:  Peter Harding  <plh@performiq.com>
#
#                PerformIQ Pty. Ltd.
#
#
# NAME
#   mongo-explorer.py - Skeleton MongoDB python script
#
# SYNOPSIS
#   mongo-explorer.py [-dqv]
#
# PARAMETERS
#   See __doc__ below
#
# DESCRIPTION
#   ...
#
# RETURNS
#   0 for successful completion, 1 for any error
#
# FILES
#   ...
#
# -----------------------------------------------------------------------------
"""
Usage:

   $ mongo-explorer.py [-dv] -apn 10y

   $ mongo-explorer.py [-dv] -o             # ...

Parameters:

   -a              ...
   -p              ...
   -n 10           No of ...
   -o              ...
   -d              Increment Debug level
   -q              Set Quiet
   -v              Set Verbose

"""
# -----------------------------------------------------------------------------

import os
import re
import sys
import time
import getopt
import random
import pickle
import pprint
import urllib
import logging
import tempfile

from datetime import datetime

# -----------------------------------------------------------------------------

__at_id__     = "@(#)  mongo-explorer.py  [1.0.0]  2023-12-07"
__version__   = re.sub(r".*\[([0-9.]*)\].*", r"\1", __at_id__)

quiet_flg     = False
verbose_flg   = False

debug_level   = 0

LOG_DIR       = os.getenv("LOG_DIR")
home_dir      = None

p_crlf        = re.compile(r"[\r\n]*")

pp            = pprint.PrettyPrinter(indent=4)

with tempfile.NamedTemporaryFile(dir=LOG_DIR, prefix="mongo-explorer-", suffix=".log", delete=False) as tmpfile:
    temp_file_name = tmpfile.name

logging.basicConfig(filename=temp_file_name,
                    encoding='utf-8',
                    format='%(asctime)s -  %(levelname)s - %(message)s',
                    level=logging.DEBUG)

# logger.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

logger        = logging.getLogger(__name__)


# =============================================================================

class Enum(set):
   pass

   #--------------------------------------------------------------------

   def __getattr__(self, name):
      if name in self:
         return name
      raise AttributeError

   #--------------------------------------------------------------------


# =============================================================================

class Data:
    TotalCount = 0

    #--------------------------------------------------------------------

    @classmethod
    def count_row(cls):
        cls.TotalCount += 1

   #--------------------------------------------------------------------

    def __init__(self, row):
        Data.count_row()
        cols = row.split(",")
        self.One = cols[0]
        self.Two = cols[1]

   #--------------------------------------------------------------------

    def __str__(self):
        return self.One

   #--------------------------------------------------------------------


# =============================================================================
# And here are a couple of model utility methods...
# -----------------------------------------------------------------------------

def csv_reader(fname):
    Logger.Info("[csv_reader]")

    csv_data  = []

    f_in      = open(fname, "rb")
    reader    = csv.reader(f_in)

    cnt   = 0
    total = 0

    for row in reader:
        cnt += 1

        if cnt < 2: continue  # Skip headings

        data = Data(row)
  
        if data.TotalCount < 1000: continue

        total += data.TotalCount

        # print(data)

        csv_data.append(data)

    f_in.close()  # Explicitly close the file *NOW*

    no_lines  = len(csv_data)

    print("Read %d data items..." % no_lines)
    print("                 -> Total data  %d" % total)

    return csv_data


# -----------------------------------------------------------------------------

def file_reader(fname):
    Logger.Info("[file_reader]")

    fname_in  = f"{fname}.log"
    fname_out = f"{fname}.dat"

    try:
        f_in = open(fname_in, "r")
    except IOError as err:
        sys.stderr.write(f"{fname_in}: cannot open: {err}\n")
        sys.exit(1)

    try:
        f_out = open(fname_out, "a+")
    except IOError as err:
        sys.stderr.write(f"{fname_out}: cannot open: {err}\n")
        sys.exit(1)

    while True:
        line = f_in.readline()

        if not line: break

        #  Truncate EoL markers from end of line

        line = p_crlf.sub("", line)  # or "line = line[:-1]"

        data = Data(line)

        f_out.write("[%s]\n" % (line, ))

    f_in.close()
    f_out.close()


# -----------------------------------------------------------------------------
# And here is the real work...
# -----------------------------------------------------------------------------

def list_collections(database):
    pass


# -----------------------------------------------------------------------------

def list_databases():
    pass


# =============================================================================

def usage():
    print(__doc__)

# -----------------------------------------------------------------------------

def main(argv):
    global debug_level
    global quiet_flg
    global verbose_flg
    global target
    global home_dir

    try:
        home_dir = os.environ["HOME"]
    except:
        print("Set HOME environment variable and re-run")
        sys.exit(0)

    Modes    = Enum(["Info", "Parse", ])

    mode     = Modes.Info
    filename = None

    try:
        opts, args = getopt.getopt(argv, "dD:f:hqvV?",
                ("debug", "debug-level=", "file=", "help", "quiet", "verbose", "version"))
    except getopt.error as err:
        print(err)
        usage()
        return 1

    for opt, arg in opts:
        if opt in ("-?", "-h", "--help"):
            usage()
            return 0
        elif opt in ("-d", "--debug"):
            debug_level                        += 1
        elif opt in ("-D", "--debug-level"):
            debug_level                         = int(arg)
        elif opt in ("-f", "--file"):
            mode                                = Modes.Parse
            filename                            = arg
        elif opt in ("-q", "--quiet"):
            quiet_flg                           = True
        elif opt in ("-v", "--verbose"):
            verbose_flg                         = True
        elif opt in ("-V", "--version"):
            if quiet_flg:
                print(__version__)
            else:
                print("[mongo-explorer]  Version: %s" % __version__)
            return 1
        else:
            usage()
            return 1

    rest = []

    if args:
        for arg in args:
            rest.append(arg)

    sys.stderr.write("[mongo-explorer]  Working directory is %s\n" % os.getcwd())

    if (debug_level > 0): sys.stderr.write("[mongo-explorer]  Debugging level set to %d\n" % debug_level)

    sys.stderr.flush()

    if mode == Modes.Info:
        print(rest)
    elif mode == Modes.Parse:
        logger.info("Parsing")
        do_work(filename)
    else:
        logger.info("Nothing to do")

    return 0

# -----------------------------------------------------------------------------

if __name__ == "__main__" or __name__ == sys.argv[0]:
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt as err:
        print(f"[mongo-explorer]  Interrupted! - {err}")


# -----------------------------------------------------------------------------

"""
Revision History:

     Date     Who   Description
   --------   ---   -----------------------------------------------------------
   20031014   plh   Initial implementation
   20111101   plh   Add in Enums for modal behaviour
   20130220   plh   Reconstructed performiq module
   20150831   plh   Fixed mssing rest

Problems to fix:

To Do:

Issues:


Notes:

  This is a starter only.  No real functionality has been added - plh 2025-08-13



"""
# -----------------------------------------------------------------------------

