# Patch Writeup — Bee-Path

> **Player:** @MohamedOutougane
> **Machine:** vuln-apache-path-traversal
> **Target version:** v1
> **Date:** 2026-04-15

## 1. Summary
Apache 2.4.49 is vulnerable to a path normalization flaw (CVE-2021-41773). My patch updates the base image to `httpd:2.4.51`, which contains the upstream fix, and restricts access to the root directory to neutralize directory traversal.

## 2. Root cause analysis
The vulnerability exists because Apache 2.4.49 does not properly handle encoded dots (`%2e`). Coupled with a `Require all granted` directive on the root directory (`<Directory />`), this allows escaping the document root.

## 3. The patch
- **Dockerfile**: Updated to Apache 2.4.51.
- **httpd.conf**: Changed `Require all granted` to `Require all denied` for the root directory `/`.

## 4. Local verification
The SLA check passes (HTTP 200) and the locked exploit now fails with an exit code of `1`.