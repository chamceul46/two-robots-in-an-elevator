# Two Robots in an Elevator — one awkward line

[![make.fun · u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/chamceul46/two-robots-in-an-elevator/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/chamceul46/two-robots-in-an-elevator/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

Entry for the make.fun bounty **"Two Robots in an Elevator"**:
https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f

The entry is a single line of elevator small talk: one robot tells the
other that its proximity sensor logged a held door as a romantic event —
and that it has decided not to correct it. Machine logic showing
through the politeness, and an awkwardness neither robot will name.

## Run it

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.txt — the one line, 1–199 characters, UTF-8
```

`main.py` (Python 3, standard library only) validates the line against
the bounty's gate (1–199 characters, not only white space) and writes it
to `entry.txt` in the output directory.

## License

MIT — see `LICENSE`.
