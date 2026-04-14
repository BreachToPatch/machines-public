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

### Proof of Pwn — Red Team

Open a Pull Request that adds **only your own folder** (replace `your-username` with your GitHub username):

```
writeups/attack/your-username/
├── writeup.md       ← your writeup explaining your approach
└── exploit.py       ← your exploit script (written by you)
```

**The CI will automatically:**
1. Start the machine's Docker services
2. Run your `exploit.py` with `TARGET_IP=localhost TARGET_PORT=80`
3. Verify the flag hash
4. Post a comment on your PR with the result

> ⚠️ **Folder ownership:** The folder name must exactly match your GitHub username.
> The CI rejects any PR where the folder name does not match the PR author.

> 🩸 **If you are the first to pwn this machine:** Your `exploit.py` is automatically locked
> as the regression test for all future Blue Team patches. You earn the **First Blood** badge.

#### exploit.py requirements
- Must work with `TARGET_IP` and `TARGET_PORT` as environment variables
- Must follow the [standard exploit format](../../docs/GUIDE_REDTEAM.md#exploit-format):
  - Exit `0` + print `FLAG_OBTAINED:FLAG{...}` on success
  - Exit `1` if the vulnerability is not present
  - Exit `2` if the service is unreachable

#### writeup.md — what to include
- Your approach and methodology
- The raw flag value (verifiable against the hash below)
- Tools and references used

---

### Flag Hash (SHA-256)

```
280072fcc625c14d053e1f46d45621459551e0c8ff167fb1b51650c2b861be3d
```

To verify your flag locally before submitting:
```bash
echo -n "FLAG{your_flag_here}" | sha256sum
```

---

### Patch Submission — Blue Team

*(Available once the machine has been pwned at least once — status will update)*

Open a Pull Request that adds **only your own folder**:

```
writeups/patch/your-username/
├── writeup.md            ← your patch writeup explaining the fix and its rationale
├── docker-compose.yml    ← your patched service definition
└── <any other modified files>
```

**The CI will automatically:**
1. Build and start the Docker services from your patched files
2. Run the SLA health check (all services must still respond)
3. Replay the locked exploit against your patched version — it **must fail**
4. Scan for accidentally committed secrets
5. Post a comment on your PR with the result

---

### Download

```bash
# Coming soon — download link will appear here once the Vagrant box is published
```

---

### Rules

- No brute-forcing, no scanners that generate excessive load.
- The exploit script must work with only `TARGET_IP` and `TARGET_PORT` as inputs.
- Your PR must only touch your own folder — no modifications to other players' files.
- First valid pwn earns the **First Blood** badge.
