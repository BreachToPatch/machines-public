# Machine: Bee-Path (v1)

**Difficulty**: Easy
**Category**: Web / Path Traversal
**Status**: 🔴 Red Team Phase Active

---

### Description

A misconfigured Apache server is exposing more than it should.
Can you find a path to the root flag?

> **Hint**: What happens when a web server doesn't properly normalize the URLs it receives?

---

### Target Information

| Field      | Value                     |
|------------|--------------------------|
| IP Address | `192.168.56.10` (local)  |
| Port       | `80` (HTTP)              |
| OS         | Ubuntu 22.04             |

The machine runs **locally** on your machine via Vagrant + VirtualBox.
See the [Red Team Guide](https://github.com/BreachToPatch/docs/blob/main/GUIDE_REDTEAM.md) for setup instructions.

---

### Submitting a PWN — Red Team

**Step 1 — Create your branch**
```
attack/{your-github-username}/vuln-apache-path-traversal
```
Example: `attack/alice/vuln-apache-path-traversal`

**Step 2 — Add your files** inside your own folder:
```
vuln-apache-path-traversal/writeups/attack/{your-username}/
├── writeup.md       ← your writeup explaining your approach
└── exploit.py       ← your exploit script (written by you)
```

**Step 3 — Open a Pull Request**

The CI will automatically:
1. Verify your branch name and folder ownership
2. Start the machine's Docker services
3. Run your `exploit.py` with `TARGET_IP=localhost TARGET_PORT=80`
4. Verify the flag hash against `accepted_hashes.json`
5. Post a comment on your PR with the result

> ⚠️ **Rules:**
> - Your branch must be named exactly `attack/{your-username}/vuln-apache-path-traversal`
> - Your folder must be named exactly after your GitHub username
> - Your PR must only touch files inside your own folder

> 🩸 **First Blood:** If you are the first to pwn this machine on the current version,
> your `exploit.py` is locked as the regression test for all future patches. +100 pts.

For the full exploit format, see the [Red Team Guide](https://github.com/BreachToPatch/docs/blob/main/GUIDE_REDTEAM.md#exploit-format).

---

### Submitting a Patch — Blue Team

*(Available once the machine has been pwned at least once)*

**Step 1 — Get the source code**

Fork the archive: `https://github.com/BreachToPatch/machines-archive/tree/main/vuln-apache-path-traversal-v1`

**Step 2 — Create your branch**
```
patch/{your-github-username}/vuln-apache-path-traversal
```
Example: `patch/bob/vuln-apache-path-traversal`

**Step 3 — Add your files** inside your own folder:
```
vuln-apache-path-traversal/writeups/patch/{your-username}/
├── writeup.md            ← your patch writeup explaining the fix
├── docker-compose.yml    ← CI test compose file (see required format below)
└── patch/                ← your patched files, mirroring the machine structure
    └── app/
        └── apache/
            ├── Dockerfile    ← MUST have ARG FLAG_VALUE (see guide)
            └── httpd.conf    ← (or whichever files you modified)
```

**Required `docker-compose.yml` format:**
```yaml
services:
  apache:
    build:
      context: ./patch/app/apache/
      args:
        FLAG_VALUE: ${FLAG_VALUE}   # ← required — CI injects the validation flag here
    ports:
      - "80:80"
```

**Required `Dockerfile` pattern inside `patch/`:**
```dockerfile
FROM httpd:2.4.49   # (or the version you chose as fix)

# ... your security fix here ...

ARG FLAG_VALUE=FLAG{PLACEHOLDER}   # ← required — do not remove
RUN mkdir -p /root \
    && echo "$FLAG_VALUE" > /root/flag.txt \
    && chmod 400 /root/flag.txt

EXPOSE 80
```

**Step 4 — Open a Pull Request**

The CI will:
1. Run structural checks immediately (< 30s)
2. Post "🕐 Validation in progress"
3. Build your image with the injected flag and replay the locked exploit (~3 min)
4. Post the final result ✅ or ❌

See the [Blue Team Guide](https://github.com/BreachToPatch/docs/blob/main/GUIDE_BLUETEAM.md) for full instructions.

---

### Flag Hash (SHA-256)

```
280072fcc625c14d053e1f46d45621459551e0c8ff167fb1b51650c2b861be3d
```

To verify your flag locally:
```bash
echo -n "FLAG{your_flag_here}" | sha256sum
```

---

### Download

```bash
# Coming soon — download link will appear here once the Vagrant box is published
```