# Machine: Bee-Path (v1.0)

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
See the [Red Team Guide](../../docs/GUIDE_REDTEAM.md) for setup instructions.

---

### Proof of Pwn

To validate your pwn, you must submit a Pull Request containing:

1. `writeups/attack/YOUR_GITHUB_USERNAME.md` — a Markdown writeup explaining your approach.
2. `exploit/exploit.py` — a Python script **written by you** that exploits the vulnerability and retrieves the flag. This file does not exist yet — you are the one who creates it. It must follow the [standard exploit format](../../docs/GUIDE_REDTEAM.md#exploit-format).
3. The raw flag value (in your writeup) — anyone can verify it against the hash below.

> **How the CI validates your pwn:** When you open a PR, GitHub Actions automatically starts
> the machine's Docker services and runs your exploit script against them
> (`TARGET_IP=localhost`). If your script returns exit code `0` and the flag hash matches,
> your pwn is confirmed.

> **Note:** The exploit script you submit becomes the automated regression test for all future
> Blue Team patches. Once your pwn is validated and merged, your script is locked — it will be
> replayed automatically against every patch PR.

**Flag Hash (SHA-256)**:
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

---

### Rules

- No brute-forcing, no scanners that generate excessive load.
- The exploit script must work with only `TARGET_IP` and `TARGET_PORT` as inputs.
- First valid pwn earns the **First Blood** badge.
