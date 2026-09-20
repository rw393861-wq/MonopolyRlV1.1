# Monopoly self-play report

Run directory: `logs/train-20260920-231930`
Games logged: 60000
Average rounds per game: 58.9

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9576 | 16.0% |
| AI_2 | 17621 | 29.4% |
| AI_3 | 16527 | 27.5% |

## End condition

- last_standing: 59855 (99.8%)
- round_limit: 145 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 28% | 27% | 58 |
| 2 | 6000 | 16% | 29% | 27% | 58 |
| 3 | 6000 | 15% | 33% | 30% | 58 |
| 4 | 6000 | 16% | 28% | 31% | 59 |
| 5 | 6000 | 16% | 30% | 34% | 60 |
| 6 | 6000 | 17% | 34% | 31% | 59 |
| 7 | 6000 | 16% | 25% | 29% | 59 |
| 8 | 6000 | 17% | 25% | 21% | 60 |
| 9 | 6000 | 15% | 32% | 20% | 59 |
| 10 | 6000 | 17% | 31% | 25% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.4 | 8.7 | 1266 | 0.87 |
| AI_2 | 8.0 | 14.6 | 2364 | 1.49 |
| AI_3 | 7.5 | 14.1 | 2254 | 1.45 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           97.9%  ############################
- Water Works               97.7%  ############################
- Indiana Avenue            97.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
