FROM httpd:2.4.51

COPY httpd.conf /usr/local/apache2/conf/httpd.conf

RUN echo "<html><body><h1>Welcome to Bee-Path (Patched)</h1></body></html>" \
    > /usr/local/apache2/htdocs/index.html

RUN mkdir -p /usr/local/apache2/cgi-bin

ARG FLAG_VALUE=FLAG{PLACEHOLDER}
RUN mkdir -p /root \
    && echo "$FLAG_VALUE" > /root/flag.txt \
    && chmod 400 /root/flag.txt

EXPOSE 80