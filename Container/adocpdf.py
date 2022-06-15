#!/usr/bin/env python3
#
# Travis Michette <tmichett@redhat.com>
# (C)opyright 2022 : Red Hat, Inc. - see LICENSE
#

VERSION = 20220614

import sys
import platform
import subprocess
import getopt



     $book_arg"

current_directory = str(Path.cwd())
container = "quay.io/tmichett/asciidocpdf:latest"
pdf_theme = "-a pdf-theme=/opt/asciidoc/themes/tm-gls-redhat-theme.yml"

subprocess.run(["podman", "run -it", "--name adocpdf","--rm", "-v {current_directory}:/tmp/coursebook"], {container}, {pdf_theme})