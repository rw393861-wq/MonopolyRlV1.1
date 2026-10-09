# Monopoly self-play report

Run directory: `logs/train-20261009-195328`
Games logged: 60000
Average rounds per game: 59.9

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10100 | 16.8% |
| AI_2 | 15212 | 25.4% |
| AI_3 | 17379 | 29.0% |

## End condition

- last_standing: 59827 (99.7%)
- round_limit: 173 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 25% | 30% | 58 |
| 2 | 6000 | 17% | 28% | 33% | 59 |
| 3 | 6000 | 16% | 23% | 35% | 59 |
| 4 | 6000 | 17% | 28% | 25% | 60 |
| 5 | 6000 | 18% | 31% | 24% | 60 |
| 6 | 6000 | 17% | 34% | 24% | 61 |
| 7 | 6000 | 16% | 23% | 26% | 60 |
| 8 | 6000 | 17% | 19% | 24% | 59 |
| 9 | 6000 | 16% | 21% | 35% | 60 |
| 10 | 6000 | 18% | 22% | 35% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1328 | 0.89 |
| AI_2 | 6.9 | 13.1 | 2171 | 1.39 |
| AI_3 | 7.9 | 14.5 | 2376 | 1.48 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- New York Avenue           98.5%  ############################
- St. Charles Place         98.5%  ############################
- Illinois Avenue           98.5%  ############################
- Tennessee Avenue          98.4%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.1%  ############################
- Water Works               97.9%  ############################
- Kentucky Avenue           97.7%  ############################
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
