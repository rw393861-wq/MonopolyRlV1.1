# Monopoly self-play report

Run directory: `logs/train-20260926-180939`
Games logged: 60000
Average rounds per game: 60.3

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10016 | 16.7% |
| AI_2 | 16366 | 27.3% |
| AI_3 | 16366 | 27.3% |

## End condition

- last_standing: 59850 (99.8%)
- round_limit: 150 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 29% | 29% | 60 |
| 2 | 6000 | 16% | 34% | 24% | 60 |
| 3 | 6000 | 16% | 31% | 25% | 60 |
| 4 | 6000 | 17% | 25% | 28% | 61 |
| 5 | 6000 | 17% | 25% | 21% | 61 |
| 6 | 6000 | 17% | 21% | 23% | 59 |
| 7 | 6000 | 17% | 22% | 35% | 60 |
| 8 | 6000 | 17% | 23% | 38% | 60 |
| 9 | 6000 | 16% | 31% | 26% | 61 |
| 10 | 6000 | 17% | 31% | 24% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1327 | 0.90 |
| AI_2 | 7.4 | 14.3 | 2292 | 1.49 |
| AI_3 | 7.4 | 13.5 | 2281 | 1.41 |

## Properties most often held by the winner

- St. Charles Place         98.5%  ############################
- Reading Railroad          98.5%  ############################
- Illinois Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- New York Avenue           98.4%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.3%  ############################
- Pennsylvania Railroad     98.0%  ############################
- Electric Company          98.0%  ############################
- Water Works               97.9%  ############################
- Kentucky Avenue           97.9%  ############################
- Virginia Avenue           97.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
