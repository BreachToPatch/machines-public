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
    │   │   └── player-username.md
    │   └── remediation/                    # Blue Team patch writeups
    │       └── player-username.md
    └── exploit/
        └── exploit.py                      # Validated exploit script (submitted by Red Teamer)
```

---

## The two phases of a machine

### 🔴 Red Team Phase
- The machine is listed with status **Red Team Active**
- Players download the Vagrant box and try to pwn it
- To claim a pwn, a player opens a PR containing:
  - A writeup in `writeups/attack/their-username.md`
  - An exploit script in `exploit/exploit.py`
  - The raw flag value (written in the writeup)
- The CI pipeline automatically boots the machine, runs the exploit, and verifies the flag hash
- The **first** validated pwn earns the **First Blood** badge and unlocks the Blue Team phase

### 🔵 Blue Team Phase
- Once a machine is pwned, it enters **Blue Team Active** status
- The original source code is published in `machines-archive` for analysis
- Blue Teamers fork the sources, apply a security patch, and open a PR here containing:
  - A patch description in `writeups/remediation/their-username.md`
  - The modified source files (in a linked PR to `machines-archive`)
- The CI pipeline verifies:
  1. All services still respond (SLA — the patch didn't break anything)
  2. The original exploit **fails** on the patched version (the vulnerability is fixed)
  3. No new secrets or backdoors were introduced (TruffleHog + Semgrep scan)
- A validated patch becomes the new version of the machine (v1.1, v1.2, ...) and resets to Red Team Active

---

## How to participate

### As a Red Teamer
1. Read the machine's `README.md` for download instructions
2. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
3. Follow the [Red Team Guide](../docs/GUIDE_REDTEAM.md)
4. Submit your writeup + exploit via Pull Request

### As a Blue Teamer
1. Wait for a machine to enter Blue Team phase (status changes in the README)
2. Find the machine's source code in `machines-archive`
3. Follow the [Blue Team Guide](../docs/GUIDE_BLUETEAM.md)
4. Submit your patch via Pull Request

---

## How this repo interacts with other repos

```
machines-sources (btop-sources, private)
   └── Maintainers build and publish the Vagrant box as a GitHub Release here

machines-public (this repo) ←── Players submit PRs here
   └── CI validates pwns and patches automatically

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
