# Monopoly self-play report

Run directory: `logs/train-20261023-184733`
Games logged: 60000
Average rounds per game: 60.4

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10094 | 16.8% |
| AI_2 | 15809 | 26.3% |
| AI_3 | 17516 | 29.2% |

## End condition

- last_standing: 59849 (99.7%)
- round_limit: 151 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 31% | 27% | 59 |
| 2 | 6000 | 17% | 34% | 26% | 59 |
| 3 | 6000 | 16% | 31% | 25% | 60 |
| 4 | 6000 | 17% | 28% | 27% | 60 |
| 5 | 6000 | 17% | 26% | 28% | 61 |
| 6 | 6000 | 17% | 24% | 27% | 62 |
| 7 | 6000 | 17% | 19% | 38% | 61 |
| 8 | 6000 | 17% | 22% | 39% | 61 |
| 9 | 6000 | 16% | 23% | 28% | 61 |
| 10 | 6000 | 17% | 26% | 27% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.4 | 1347 | 0.91 |
| AI_2 | 7.2 | 13.5 | 2243 | 1.41 |
| AI_3 | 8.0 | 14.7 | 2410 | 1.54 |

## Properties most often held by the winner

- Illinois Avenue           98.7%  ############################
- Reading Railroad          98.6%  ############################
- St. Charles Place         98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- New York Avenue           98.5%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.4%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           97.9%  ############################
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
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
