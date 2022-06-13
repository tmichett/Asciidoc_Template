FROM registry.fedoraproject.org/fedora:34-x86_64

MAINTAINER Travis Michette <tmichett@redhat.com>

# --version option and argument for gem install
# Now it is the RPM package version
#ARG ASCIIDOCTOR=
#ARG ASCIIDOCTOR="-2.0.10"

ENV BOOK="/tmp/coursebook"

RUN dnf -y install  ruby python3 asciidoc \
  && dnf clean all \
  && gem install asciidoctor rouge  pygments.rb coderay \
  && gem install asciidoctor-pdf -v 2.1.0 \
  && mkdir -p ${BOOK} \
  && mkdir -p /opt/asciidoc

ADD asciidoc /opt

VOLUME ${BOOK}

WORKDIR ${BOOK}
 
#ENTRYPOINT [ "/usr/local/share/gems/gems/asciidoctor-pdf-2.1.0/bin/asciidoctor-pdf", "-a pdf-theme=/opt/asciidoc/themes/tm-gls-redhat-theme.yml"]
ENTRYPOINT [ "/usr/local/share/gems/gems/asciidoctor-pdf-2.1.0/bin/asciidoctor-pdf"]
