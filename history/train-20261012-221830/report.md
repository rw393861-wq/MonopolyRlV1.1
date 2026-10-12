# Monopoly self-play report

Run directory: `logs/train-20261012-221830`
Games logged: 60000
Average rounds per game: 60.5

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9960 | 16.6% |
| AI_2 | 17216 | 28.7% |
| AI_3 | 16924 | 28.2% |

## End condition

- last_standing: 59844 (99.7%)
- round_limit: 156 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 25% | 29% | 59 |
| 2 | 6000 | 17% | 31% | 28% | 59 |
| 3 | 6000 | 16% | 31% | 31% | 61 |
| 4 | 6000 | 17% | 29% | 29% | 61 |
| 5 | 6000 | 17% | 31% | 29% | 62 |
| 6 | 6000 | 17% | 25% | 32% | 61 |
| 7 | 6000 | 17% | 28% | 26% | 61 |
| 8 | 6000 | 17% | 38% | 20% | 60 |
| 9 | 6000 | 16% | 29% | 27% | 61 |
| 10 | 6000 | 16% | 21% | 31% | 62 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1332 | 0.90 |
| AI_2 | 7.8 | 14.3 | 2391 | 1.43 |
| AI_3 | 7.7 | 14.2 | 2364 | 1.43 |

## Properties most often held by the winner

- Reading Railroad          98.7%  ############################
- Illinois Avenue           98.7%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.4%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           98.1%  ############################
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
