# Build notes

- Competition: u-eager-stork-81-9647-funniest-time-machine-warning-f8add151
  ("Funniest Time Machine Warning Label", $2, closes 26 Nov 2026 21:15 WIB).
- Read RULES.txt + competition.yaml first. Gate: entry.txt must be UTF-8,
  1–120 characters, not only whitespace. Judge: pairwise AI comedy judging
  against the published brief (time-machine warning, real hazard as joke,
  surprise at the end, straight face, no wasted words).
- main.py: Python stdlib only. Reads MAKEFUN_OUTPUT_DIR (default /output),
  writes the single entry line to entry.txt with no trailing newline.
- Draft v1: "WARNING: If you encounter yourself during travel, do not wave.
  He knows what you did." — 85 chars, local test passed.
- Revision (v2, final): tightened to "WARNING: If you meet yourself in the
  past, do not wave. He knows what you did." — 78 chars. Dropped the filler
  "during travel", swapped "encounter" for punchier "meet", added "in the
  past" to anchor the time-machine setting. Punchline still lands last.
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`,
  then verified out/entry.txt: 78 characters, 78 bytes, 1 line, not
  whitespace-only, within 1–120. Test output dir removed afterwards.
- Not submitted; no repo created; no contact with make.fun.
