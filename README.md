# The World in One Day — Wednesday 25 November 2026

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Ritwan007/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Ritwan007/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

Entry for the [make.fun competition "Sum up 25 November's world news in one image"](https://make.fun/bounty/news-image-20261125)
(`news-image-20261125`, $100 USDC escrowed, deadline 2026-11-27 00:00 UTC).

## The image

A one-page newspaper front page — **"WEDNESDAY 25 NOVEMBER 2026"** — summing up
Wednesday 25 November 2026 in four panels:

- **UKRAINE SINKS RUSSIAN SHIP** — Zelenskyy confirms Ukrainian drones sank the
  Russian corvette Merkury in Benghazi port, Libya, and hit the cargo ship Sparta II
  in the Gulf of Finland; Russia calls the strikes "terrorist acts".
- **RIYADH TOWER HIT AGAIN** — a Houthi projectile strikes Riyadh's tallest tower,
  the PIF Tower, wounding 11 people; the second hit in five days.
- **COP31 ENDS WITH NO DEAL** — the UN climate summit in Antalya collapses without
  a final agreement, the first COP to fail that way since Copenhagen 2009, split
  over fossil fuels.
- **HUAWEI FOUND GUILTY** — a US jury finds Huawei guilty on 10 counts, including
  conspiracy to steal trade secrets and bank fraud.

Footer: an unclassified CIA computer system was breached; China investigates top
official Chen Jining; the World Chess Championship opens with a Game 1 draw.

Built from wire reporting (Reuters, AP) checked on the morning of 25 November 2026;
see the findings note in the builder's workspace. The day was only ~90 minutes old
in UTC when this entry was built, so the finisher may iterate with later news
before the deadline.

## How it runs

`main.ts` (Node 22, standard library only) copies the composed `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). No network. Both runs write
identical bytes.
