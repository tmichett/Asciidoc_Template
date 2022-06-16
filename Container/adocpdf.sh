#!/usr/bin/env python3
#
# Travis Michette <tmichett@redhat.com>

container = "quay.io/tmichett/asciidocpdf:latest"
pdf_theme = "-a pdf-theme=/opt/asciidoc/themes/tm-gls-redhat-theme.yml"
current_directory=$(pwd)

podman run -it --name adocpdf --rm -v $current_directory:/tmp/coursebook $container $pdf_theme $1