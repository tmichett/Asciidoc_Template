FROM registry.fedoraproject.org/fedora:34-x86_64

MAINTAINER Travis Michette <tmichett@redhat.com>

# --version option and argument for gem install
# Now it is the RPM package version
#ARG ASCIIDOCTOR=
#ARG ASCIIDOCTOR="-2.0.10"

ENV BOOK="/tmp/coursebook"

RUN dnf -y install  ruby python3 asciidoc \
  && dnf clean all \
  && gem install asciidoctor asciidoctor-pdf rouge  pygments.rb coderay \
  && mkdir -p ${BOOK}

VOLUME ${BOOK}

WORKDIR ${BOOK}/guides

ENTRYPOINT [ "/usr/bin/flamel" ]
