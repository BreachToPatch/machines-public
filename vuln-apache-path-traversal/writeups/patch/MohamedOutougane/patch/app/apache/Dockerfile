# Apache 2.4.51 — contains the upstream fix for CVE-2021-41773
FROM httpd:2.4.51

# Copy the hardened Apache configuration
COPY httpd.conf /usr/local/apache2/conf/httpd.conf

# Create a simple index page
RUN echo "<html><body><h1>Welcome to Bee-Path (Patched)</h1></body></html>" \
    > /usr/local/apache2/htdocs/index.html

# Ensure cgi-bin directory exists (kept for service compatibility)
RUN mkdir -p /usr/local/apache2/cgi-bin

# Required pattern for BtoP CI — do not remove
ARG FLAG_VALUE=FLAG{PLACEHOLDER}
RUN mkdir -p /root \
    && echo "$FLAG_VALUE" > /root/flag.txt \
    && chmod 400 /root/flag.txt

EXPOSE 80