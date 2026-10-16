# Monopoly self-play report

Run directory: `logs/train-20261016-183103`
Games logged: 60000
Average rounds per game: 60.0

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10272 | 17.1% |
| AI_2 | 16263 | 27.1% |
| AI_3 | 14840 | 24.7% |

## End condition

- last_standing: 59844 (99.7%)
- round_limit: 156 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 29% | 27% | 59 |
| 2 | 6000 | 17% | 25% | 28% | 59 |
| 3 | 6000 | 16% | 31% | 26% | 60 |
| 4 | 6000 | 17% | 30% | 26% | 61 |
| 5 | 6000 | 18% | 28% | 23% | 60 |
| 6 | 6000 | 17% | 25% | 25% | 60 |
| 7 | 6000 | 18% | 28% | 24% | 60 |
| 8 | 6000 | 17% | 25% | 24% | 61 |
| 9 | 6000 | 16% | 23% | 22% | 60 |
| 10 | 6000 | 17% | 27% | 23% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1349 | 0.90 |
| AI_2 | 7.4 | 14.3 | 2285 | 1.48 |
| AI_3 | 6.8 | 12.8 | 2137 | 1.39 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.5%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           98.0%  ############################
- Water Works               97.9%  ############################
- Indiana Avenue            97.9%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
