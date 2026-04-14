#!/usr/bin/env python3
"""
update_leaderboard.py — Scoring script for BreachToPatch.

Called by update-leaderboard.yml every time a pwn or patch PR is merged.
Reads environment variables set by the workflow, updates leaderboard.json,
and writes it back to disk. The workflow then commits the result.

Environment variables (set by the workflow):
    SUBMISSION_TYPE   — "attack" or "patch"
    USERNAME          — GitHub username of the player
    MACHINE           — machine slug (e.g. vuln-apache-path-traversal)
    IS_FIRST_BLOOD    — "true" if this is the first pwn on this machine
    LEADERBOARD_PATH  — path to leaderboard.json on disk
"""

import json
import os
import sys
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Read inputs from environment
# ---------------------------------------------------------------------------
SUBMISSION_TYPE  = os.environ["SUBMISSION_TYPE"]
USERNAME         = os.environ["USERNAME"]
MACHINE          = os.environ["MACHINE"]
IS_FIRST_BLOOD   = os.environ.get("IS_FIRST_BLOOD", "false").lower() == "true"
LEADERBOARD_PATH = os.environ["LEADERBOARD_PATH"]

# ---------------------------------------------------------------------------
# Scoring rules
# ---------------------------------------------------------------------------
POINTS_FIRST_BLOOD = 100   # first pwn on a machine
POINTS_ATTACK      = 50    # subsequent pwn
POINTS_PATCH       = 75    # validated patch

# ---------------------------------------------------------------------------
# Load existing leaderboard
# ---------------------------------------------------------------------------
with open(LEADERBOARD_PATH, "r") as f:
    data = json.load(f)

# ---------------------------------------------------------------------------
# Find or create the player's entry
# ---------------------------------------------------------------------------
player = None
for p in data["players"]:
    if p["github_username"] == USERNAME:
        player = p
        break

if player is None:
    # New player — create a blank entry
    player = {
        "github_username":  USERNAME,
        "points":           0,
        "pwns":             0,
        "patches":          0,
        "machines_created": 0,
        "badges":           [],
        "github_profile":   f"https://github.com/{USERNAME}"
    }
    data["players"].append(player)
    print(f"[+] New player registered: {USERNAME}")

# ---------------------------------------------------------------------------
# Apply scoring based on submission type
# ---------------------------------------------------------------------------
if SUBMISSION_TYPE == "attack":
    player["pwns"] += 1

    if IS_FIRST_BLOOD:
        player["points"] += POINTS_FIRST_BLOOD
        print(f"[+] First Blood! +{POINTS_FIRST_BLOOD} pts for {USERNAME}")

        # Award First Blood badge (only once per player total, not per machine)
        if "🩸 First Blood" not in player["badges"]:
            player["badges"].append("🩸 First Blood")
            print(f"[+] Badge unlocked: 🩸 First Blood")
    else:
        player["points"] += POINTS_ATTACK
        print(f"[+] Subsequent pwn. +{POINTS_ATTACK} pts for {USERNAME}")

    # Scribe badge: 5 writeups submitted (pwns each include a writeup)
    if player["pwns"] >= 5 and "✍️ Scribe" not in player["badges"]:
        player["badges"].append("✍️ Scribe")
        print(f"[+] Badge unlocked: ✍️ Scribe")

elif SUBMISSION_TYPE == "patch":
    player["patches"] += 1
    player["points"]  += POINTS_PATCH
    print(f"[+] Patch validated. +{POINTS_PATCH} pts for {USERNAME}")

    # Defender badge: first validated patch
    if "🛡️ Defender" not in player["badges"]:
        player["badges"].append("🛡️ Defender")
        print(f"[+] Badge unlocked: 🛡️ Defender")

else:
    print(f"[!] Unknown submission type: {SUBMISSION_TYPE}", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Sort players by points (highest first)
# ---------------------------------------------------------------------------
data["players"].sort(key=lambda p: p["points"], reverse=True)

# ---------------------------------------------------------------------------
# Update the timestamp
# ---------------------------------------------------------------------------
data["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# ---------------------------------------------------------------------------
# Write the updated leaderboard back to disk
# ---------------------------------------------------------------------------
with open(LEADERBOARD_PATH, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write("\n")   # trailing newline — good practice for text files

print(f"[+] Leaderboard written to {LEADERBOARD_PATH}")
print(f"[+] {USERNAME} now has {player['points']} pts | "
      f"{player['pwns']} pwns | {player['patches']} patches | "
      f"badges: {player['badges']}")
