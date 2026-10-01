# Monopoly self-play report

Run directory: `logs/train-20261001-195758`
Games logged: 60000
Average rounds per game: 60.3

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10197 | 17.0% |
| AI_2 | 18455 | 30.8% |
| AI_3 | 16057 | 26.8% |

## End condition

- last_standing: 59845 (99.7%)
- round_limit: 155 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 18% | 30% | 26% | 58 |
| 2 | 6000 | 17% | 27% | 32% | 60 |
| 3 | 6000 | 16% | 28% | 31% | 60 |
| 4 | 6000 | 17% | 33% | 23% | 61 |
| 5 | 6000 | 17% | 28% | 23% | 61 |
| 6 | 6000 | 17% | 26% | 31% | 61 |
| 7 | 6000 | 17% | 36% | 23% | 61 |
| 8 | 6000 | 17% | 36% | 24% | 60 |
| 9 | 6000 | 16% | 35% | 28% | 60 |
| 10 | 6000 | 17% | 27% | 27% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.2 | 1353 | 0.90 |
| AI_2 | 8.4 | 15.7 | 2498 | 1.53 |
| AI_3 | 7.3 | 13.6 | 2244 | 1.46 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- New York Avenue           98.6%  ############################
- Tennessee Avenue          98.6%  ############################
- St. Charles Place         98.6%  ############################
- St. James Place           98.5%  ############################
- B&O Railroad              98.4%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.0%  ############################
- Water Works               98.0%  ############################
- Indiana Avenue            97.9%  ############################
- Kentucky Avenue           97.9%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
