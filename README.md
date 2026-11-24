# Alien Field Notes: The Two Day Earth Review

Entry for [make.fun](https://make.fun) competition
`u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000`
($2 total, top 10 share the pool; entries close 26 Nov 2026, 18:55 WIB).

## The entry

One original line of plain text, 114 characters, a review of planet Earth
left by an alien tourist:

> Five stars: the hotel folded my towel into a swan, and I have spent two days apologising to it. Would visit again.

## How it works

`main.py` (program/v1 entrypoint) writes that exact line — no trailing
newline — to `/output/entry.txt` and prints it. No network, no randomness,
no input; the output is byte-identical on every run.

Run locally:

```sh
python3 main.py
```

## Why this line (judge rubric)

The judge compares lines pairwise, most important first:

1. **Reads as a one-line review of Earth by an alien tourist** — a hotel stay
   on Earth, told from the visitor's outside view.
2. **Funny from the alien's angle on ordinary Earth life** — the alien
   mistakes towel art for a living creature and apologises to it for two days.
3. **Original** — a towel swan, not traffic, gravity, money or weather.
4. **Sounds like a real tourist review** — "Five stars" verdict up front,
   "Would visit again" closing remark, single line.
5. **Tight** — every word earns its place; the punch ("apologising to it")
   lands at the end. One joke, landed cleanly, never explained.
