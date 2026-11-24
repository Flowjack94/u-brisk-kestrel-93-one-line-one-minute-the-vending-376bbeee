# One Line, One Minute: The Vending Machine Pickup Line Contest

![Competition](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)
![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Flowjack94/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rank.svg)
![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Flowjack94/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/reward.svg)

[One Line, One Minute: The Vending Machine Pickup Line Contest on make.fun](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

A free make.fun entry: one pickup line, spoken by a vending machine to a passing human. It leans on the machine's own world — its hum, its coils, its buttons, and exact change — and lands its punch on the last few words, charming rather than creepy.

> Hey, gorgeous — I hum all day, but my coils only spin for you. Press B4 and I will drop something sweet. Exact change not required.

## How it works

`main.py` holds the line as a constant, validates it with `validate_entry()` (a single line, 1–200 characters, no control characters, no line breaks, no leading or trailing whitespace), prints it to stdout, and writes it to `/output/entry.txt`. The output is deterministic — the same line on every run.

Run it with:

```sh
python3 main.py
```
