#!/usr/bin/env python3
#
#
# Chris Tusa <ctusa@redhat.com>
# Travis Michette <tmichett@redhat.com>
# (C)opyright 2022 : Red Hat, Inc. - see LICENSE
#

VERSION = 20220614

import sys
import platform
import argparse
from pathlib import Path
import shlex
import subprocess
import yaml


def runcmd(cmdline):
    """
    Wrapper to parse a command line and execute with subprocess module
    :param cmdline:
    :return:
    """
    result = subprocess.run(splitargs(cmdline), capture_output=True, text=True)
    return result



def getpodid(image, tag):
    if TOOLSET == 'podman':
        cmdline = f"podman inspect --type image --format '{{{{.Id}}}}' {cfg['image']}:{cfg['tag']}"
    elif TOOLSET == 'docker':
        cmdline = f"docker inspect --type image --format '{{{{.Id}}}}' {cfg['image']}:{cfg['tag']}"
    result = runcmd(cmdline)
    return result.stdout


 cmdline = f"docker }"
    result = runcmd(cmdline)