# machines-public 🎯

> **Public repository — `BreachToPatch` organization**
> This is the main arena. Players download machines here, submit writeups here, and earn their place on the leaderboard here.

---

## What this repo is

`machines-public` is the **player-facing hub** of the BreachToPatch platform. It is the only place players need to interact with to participate — whether they are Red Teamers trying to pwn a machine or Blue Teamers trying to patch one.

Every action a player takes (submitting a writeup, submitting an exploit, submitting a patch) happens through a **Pull Request** to this repo. That PR is automatically validated by GitHub Actions CI before being merged.

---

## What lives here

```
machines-public/
├── README.md                               ← You are here
│
└── vuln-apache-path-traversal/             ← One folder per machine
    ├── README.md                           # Public description, rules, flag hash, download link
    ├── CHANGELOG.md                        # Version history (v1.0, v1.1 after patches, etc.)
    ├── writeups/
    │   ├── attack/                         # Red Team writeups (one .md file per player)
    │   │   └── .gitkeep                    # Empty until first pwn is submitted
    │   └── remediation/                    # Blue Team patch writeups
    │       └── .gitkeep                    # Empty until first patch is submitted
    └── exploit/
        └── .gitkeep                        # Empty until first Red Teamer submits their exploit
```

> **Note on `exploit/exploit.py`:** This file does **not** exist when a machine is first published.
> It is submitted by the **first Red Teamer** who successfully pwns the machine, as part of their PR.
> Once merged, it becomes the automated regression test that validates all future Blue Team patches.
 
---

## The two phases of a machine

### 🔴 Red Team Phase
- The machine is listed with status **Red Team Active**
- Players download the Vagrant box and try to pwn it locally (Vagrant + VirtualBox)
- To claim a pwn, a player opens a PR containing:
  - A writeup in `writeups/attack/their-username.md`
  - An exploit script in `exploit/exploit.py` — **written by the player**, not provided in advance
  - The raw flag value (written in the writeup)
- The CI pipeline starts the machine's Docker services directly and runs the submitted exploit against them, then verifies the flag hash
- The **first** validated pwn earns the **First Blood** badge and unlocks the Blue Team phase
- From that point on, `exploit/exploit.py` is locked — no further changes are accepted

### 🔵 Blue Team Phase
- Once a machine is pwned, it enters **Blue Team Active** status
- The original source code is published in `machines-archive` for analysis
- Blue Teamers fork the sources, apply a security patch, and open a PR here containing:
  - A patch description in `writeups/remediation/their-username.md`
  - The modified source files (in a linked PR to `machines-archive`)
- The CI pipeline verifies:
  1. All services still respond after starting with Docker Compose (SLA — the patch didn't break anything)
  2. The `exploit/exploit.py` submitted by the Red Teamer **fails** on the patched version (exit code `1`)
  3. No new secrets or backdoors were introduced (TruffleHog + Semgrep scan)
- A validated patch becomes the new version of the machine (v1.1, v1.2, ...) and resets to Red Team Active
- When a new Red Team phase begins, `exploit/exploit.py` is removed — a new Red Teamer must submit a new one

---

## How the CI works (no VM needed)

Players run machines locally using **Vagrant + VirtualBox** for a realistic, fully isolated pentest environment.

The CI pipeline, however, runs the **Docker Compose services directly** on GitHub's free hosted runners (Ubuntu Linux). This works because:
- The vulnerable services (web, SSH, FTP, databases, etc.) run inside Docker containers
- The exploit script connects to those containers exactly as it would inside a VM
- This covers 99% of vulnerability types: web, SSH, FTP, misconfigured services, application-level privilege escalation

> **Exception:** Vulnerabilities that require kernel-level exploitation or Layer 2 network attacks
> cannot be validated this way. Such machines would require a dedicated self-hosted runner.
> These are rare, advanced cases — out of scope for Easy and Medium difficulty machines.

---
 
## The exploit script — what it is and who writes it
 
The `exploit/exploit.py` file is **the proof of pwn**. It is written entirely by the Red Teamer who cracks the machine.
 
It must follow the standard BtoP interface:
 
```python
#!/usr/bin/env python3
import sys, os
 
TARGET = os.environ.get("TARGET_IP", "192.168.56.10")
PORT   = os.environ.get("TARGET_PORT", "80")
 
def exploit() -> str:
    # Must return the flag string on success
    # Must raise AssertionError if the vulnerability is absent (patched)
    pass
 
if __name__ == "__main__":
    try:
        flag = exploit()
        print(f"FLAG_OBTAINED:{flag}")
        sys.exit(0)    # vulnerability present and exploitable
    except AssertionError as e:
        print(f"EXPLOIT_FAILED:{e}", file=sys.stderr)
        sys.exit(1)    # vulnerability neutralized (patch worked)
    except Exception as e:
        print(f"EXPLOIT_ERROR:{e}", file=sys.stderr)
        sys.exit(2)    # service down or network error (SLA violation)
```
 
Exit code interpretation by the CI:
 
| Exit code | During pwn validation | During patch validation |
|-----------|----------------------|------------------------|
| `0`       | ✅ Flag verified — pwn accepted | ❌ Patch insufficient — PR rejected |
| `1`       | ❌ Exploit failed — pwn rejected | ✅ Vulnerability fixed — patch accepted |
| `2`       | ❌ Service unreachable | ❌ SLA violation — PR rejected |
 
See the [Red Team Guide](../docs/GUIDE_REDTEAM.md) for the full exploit script template and submission instructions.

---

## How to participate

### As a Red Teamer
1. Read the machine's `README.md` for download instructions
2. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
3. Follow the [Red Team Guide](../docs/GUIDE_REDTEAM.md)
4. Submit your writeup **and your exploit script** via Pull Request

### As a Blue Teamer
1. Wait for a machine to enter Blue Team phase (status changes in the README)
2. Find the machine's source code in `machines-archive`
3. Follow the [Blue Team Guide](../docs/GUIDE_BLUETEAM.md)
4. Submit your patch via Pull Request — the CI will run the Red Teamer's exploit against your patch automatically

---

## How this repo interacts with other repos

```
machines-sources (btop-sources, private)
   └── Maintainers build and publish the Vagrant box as a GitHub Release here

machines-public (this repo) ←── Players submit PRs here
   └── CI validates pwns and patches automatically via Docker Compose + GitHub Actions

machines-archive (BreachToPatch, public)
   └── Source code is revealed here after first pwn
   └── Blue Teamers fork from here

leaderboard (BreachToPatch, public)
   └── Every merged PR here triggers a leaderboard update there

web-site (BreachToPatch, public)
   └── The website reads machine data from this repo via GitHub API
```

---

## Scoring

| Action | Points |
|--------|--------|
| First Blood (first pwn on a machine) | 100 pts |
| Subsequent pwn | 50 pts |
| Patch validated (Blue Team) | 75 pts |
| Machine created (accepted by maintainers) | 150 pts |
| Writeup quality bonus (awarded by maintainers) | up to 25 pts |
