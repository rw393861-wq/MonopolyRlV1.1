# Monopoly self-play report

Run directory: `logs/train-20261007-201819`
Games logged: 60000
Average rounds per game: 60.3

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10260 | 17.1% |
| AI_2 | 17055 | 28.4% |
| AI_3 | 15577 | 26.0% |

## End condition

- last_standing: 59844 (99.7%)
- round_limit: 156 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 18% | 26% | 28% | 59 |
| 2 | 6000 | 17% | 25% | 29% | 59 |
| 3 | 6000 | 15% | 28% | 26% | 60 |
| 4 | 6000 | 17% | 29% | 25% | 60 |
| 5 | 6000 | 18% | 25% | 26% | 60 |
| 6 | 6000 | 17% | 31% | 21% | 62 |
| 7 | 6000 | 18% | 26% | 23% | 60 |
| 8 | 6000 | 17% | 39% | 22% | 61 |
| 9 | 6000 | 16% | 31% | 29% | 60 |
| 10 | 6000 | 18% | 25% | 31% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1347 | 0.89 |
| AI_2 | 7.8 | 14.3 | 2347 | 1.48 |
| AI_3 | 7.1 | 13.6 | 2215 | 1.45 |

## Properties most often held by the winner

- Reading Railroad          98.7%  ############################
- Illinois Avenue           98.7%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.4%  ############################
- St. Charles Place         98.4%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           97.9%  ############################
- Indiana Avenue            97.9%  ############################
- Water Works               97.9%  ############################

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
