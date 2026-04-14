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
4. Verify the flag hash
5. Post a comment on your PR with the result

> ⚠️ **Rules:**
> - Your branch must be named exactly `attack/{your-username}/vuln-apache-path-traversal`
> - Your folder must be named exactly after your GitHub username
> - Your PR must only touch files inside your own folder

> 🩸 **First Blood:** If you are the first to pwn this machine, your `exploit.py` is
> automatically locked as the regression test for all future patches. You earn the **First Blood** badge.

#### exploit.py requirements
- Must work with `TARGET_IP` and `TARGET_PORT` as environment variables
- Exit `0` + print `FLAG_OBTAINED:FLAG{...}` on success
- Exit `1` if the vulnerability is not present
- Exit `2` if the service is unreachable
- See the [standard exploit format](../../docs/GUIDE_REDTEAM.md#exploit-format)

---

### Submitting a Patch — Blue Team

*(Available once the machine has been pwned at least once)*

**Step 1 — Create your branch**
```
patch/{your-github-username}/vuln-apache-path-traversal
```
Example: `patch/bob/vuln-apache-path-traversal`

**Step 2 — Add your files** inside your own folder:
```
vuln-apache-path-traversal/writeups/patch/{your-username}/
├── writeup.md            ← your patch writeup explaining the fix
├── docker-compose.yml    ← your patched service definition
└── <any other modified files>
```

**Step 3 — Open a Pull Request**

The CI will automatically run the locked exploit against your patch.
See the [Blue Team Guide](../../docs/GUIDE_BLUETEAM.md) for detailed instructions.

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