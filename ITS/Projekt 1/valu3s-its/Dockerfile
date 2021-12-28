FROM python:3.8.7
COPY web_server /opt/web_server
WORKDIR /opt/web_server
RUN pip install -r requirements.txt
RUN /usr/local/bin/buildout
RUN mkdir -p /opt/web_server/var
#COPY filestorage /opt/web_server/var/filestorage
CMD /opt/web_server/bin/instance fg
