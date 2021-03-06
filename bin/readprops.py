

import subprocess
import configparser
import traceback
import sys


def readProps(prefsLoc):
    """Read the version of our project as a string"""

    config = configparser.RawConfigParser()
    config.read(prefsLoc)
    version = dict(config.items('VERSION'))

    # Try to find current build SHA if if the workspace is clean.  This could fail if git is not installed
    try:
        sha = subprocess.check_output(
            ['git', 'rev-parse', '--short', 'HEAD']).decode("utf-8").strip()
        isDirty = subprocess.check_output(
            ['git', 'diff', 'HEAD']).decode("utf-8").strip()
        suffix = sha
        if isDirty:
            # short for 'dirty', we want to keep our verstrings source for protobuf reasons
            suffix = sha + "-d"
        verStr = "{}.{}.{}.{}".format(
            version["major"], version["minor"], version["build"], suffix)
    except:
        # print("Unexpected error:", sys.exc_info()[0])
        # traceback.print_exc()
        verStr = "{}.{}.{}".format(
            version["major"], version["minor"], version["build"])

    # print("firmare version " + verStr)
    return verStr
# print("path is" + ','.join(sys.path))
