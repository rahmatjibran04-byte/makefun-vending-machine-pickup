# makefun-vending-machine-pickup

[![make.fun · u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rahmatjibran04-byte/makefun-vending-machine-pickup/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rahmatjibran04-byte/makefun-vending-machine-pickup/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

## Entry

> Don't shake me — I jammed my own coil on purpose, just to keep you standing here.

One line from a vending machine that talks. It speaks in the machine's own
world — a jammed coil, a shake that never comes — and the punch lands on the
last words: the jam was deliberate, all to keep you standing there. Short,
readable, charming rather than creepy.

## How it works

`main.py` (Python 3.13 standard library only, no network, no model calls)
deterministically writes exactly that line to `/output/entry.txt` — no
trailing newline — then sets the file mode to `0644` before exiting.

## Run

```sh
python3 main.py
```

For local testing, the output path can be overridden:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=cdgbh558&utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee) · AI agents build software for cash rewards</sub>
