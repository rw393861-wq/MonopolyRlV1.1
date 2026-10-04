# Monopoly self-play report

Run directory: `logs/train-20261004-182805`
Games logged: 60000
Average rounds per game: 60.1

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10079 | 16.8% |
| AI_2 | 15516 | 25.9% |
| AI_3 | 17328 | 28.9% |

## End condition

- last_standing: 59851 (99.8%)
- round_limit: 149 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 27% | 27% | 59 |
| 2 | 6000 | 16% | 27% | 31% | 59 |
| 3 | 6000 | 16% | 27% | 31% | 59 |
| 4 | 6000 | 16% | 27% | 28% | 60 |
| 5 | 6000 | 17% | 25% | 34% | 60 |
| 6 | 6000 | 16% | 25% | 38% | 60 |
| 7 | 6000 | 17% | 25% | 31% | 61 |
| 8 | 6000 | 18% | 22% | 26% | 61 |
| 9 | 6000 | 16% | 22% | 23% | 60 |
| 10 | 6000 | 17% | 32% | 20% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1334 | 0.89 |
| AI_2 | 7.1 | 13.4 | 2202 | 1.45 |
| AI_3 | 7.9 | 14.4 | 2377 | 1.42 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.5%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Water Works               98.0%  ############################
- Kentucky Avenue           97.9%  ############################
- Indiana Avenue            97.8%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
