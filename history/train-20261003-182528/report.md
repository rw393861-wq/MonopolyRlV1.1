# Monopoly self-play report

Run directory: `logs/train-20261003-182528`
Games logged: 60000
Average rounds per game: 60.4

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9920 | 16.5% |
| AI_2 | 18134 | 30.2% |
| AI_3 | 15978 | 26.6% |

## End condition

- last_standing: 59835 (99.7%)
- round_limit: 165 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 33% | 27% | 59 |
| 2 | 6000 | 17% | 25% | 28% | 60 |
| 3 | 6000 | 16% | 27% | 26% | 60 |
| 4 | 6000 | 16% | 23% | 37% | 61 |
| 5 | 6000 | 17% | 26% | 32% | 61 |
| 6 | 6000 | 18% | 26% | 26% | 60 |
| 7 | 6000 | 17% | 35% | 24% | 61 |
| 8 | 6000 | 16% | 38% | 22% | 61 |
| 9 | 6000 | 16% | 36% | 22% | 60 |
| 10 | 6000 | 15% | 33% | 22% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.0 | 1316 | 0.90 |
| AI_2 | 8.3 | 15.7 | 2491 | 1.56 |
| AI_3 | 7.3 | 13.6 | 2242 | 1.45 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.3%  ############################
- Kentucky Avenue           98.1%  ############################
- Electric Company          98.1%  ############################
- Water Works               98.0%  ############################
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
