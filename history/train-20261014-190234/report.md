# Monopoly self-play report

Run directory: `logs/train-20261014-190234`
Games logged: 60000
Average rounds per game: 59.9

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10005 | 16.7% |
| AI_2 | 17282 | 28.8% |
| AI_3 | 16178 | 27.0% |

## End condition

- last_standing: 59842 (99.7%)
- round_limit: 158 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 30% | 26% | 59 |
| 2 | 6000 | 17% | 28% | 25% | 58 |
| 3 | 6000 | 16% | 22% | 27% | 59 |
| 4 | 6000 | 16% | 24% | 23% | 60 |
| 5 | 6000 | 17% | 33% | 27% | 60 |
| 6 | 6000 | 17% | 36% | 23% | 60 |
| 7 | 6000 | 17% | 37% | 23% | 60 |
| 8 | 6000 | 17% | 30% | 26% | 61 |
| 9 | 6000 | 17% | 24% | 32% | 61 |
| 10 | 6000 | 16% | 25% | 38% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1332 | 0.89 |
| AI_2 | 7.9 | 14.3 | 2372 | 1.42 |
| AI_3 | 7.4 | 14.0 | 2253 | 1.48 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- B&O Railroad              98.3%  ############################
- St. James Place           98.2%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.0%  ############################
- Water Works               97.9%  ############################
- Kentucky Avenue           97.8%  ############################
- Indiana Avenue            97.7%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
