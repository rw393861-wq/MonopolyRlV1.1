# Monopoly self-play report

Run directory: `logs/train-20261015-184603`
Games logged: 60000
Average rounds per game: 60.0

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9875 | 16.5% |
| AI_2 | 16758 | 27.9% |
| AI_3 | 16463 | 27.4% |

## End condition

- last_standing: 59847 (99.7%)
- round_limit: 153 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 26% | 35% | 60 |
| 2 | 6000 | 16% | 32% | 29% | 59 |
| 3 | 6000 | 16% | 31% | 25% | 60 |
| 4 | 6000 | 17% | 27% | 29% | 60 |
| 5 | 6000 | 17% | 22% | 29% | 61 |
| 6 | 6000 | 16% | 23% | 22% | 60 |
| 7 | 6000 | 17% | 23% | 26% | 60 |
| 8 | 6000 | 17% | 28% | 30% | 60 |
| 9 | 6000 | 16% | 33% | 28% | 60 |
| 10 | 6000 | 17% | 36% | 22% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.5 | 9.0 | 1310 | 0.89 |
| AI_2 | 7.6 | 14.2 | 2325 | 1.47 |
| AI_3 | 7.5 | 13.8 | 2281 | 1.39 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- New York Avenue           98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           98.0%  ############################
- Water Works               97.9%  ############################
- Indiana Avenue            97.8%  ############################

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
