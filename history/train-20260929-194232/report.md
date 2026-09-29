# Monopoly self-play report

Run directory: `logs/train-20260929-194232`
Games logged: 60000
Average rounds per game: 59.5

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9878 | 16.5% |
| AI_2 | 18125 | 30.2% |
| AI_3 | 14321 | 23.9% |

## End condition

- last_standing: 59845 (99.7%)
- round_limit: 155 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 34% | 23% | 58 |
| 2 | 6000 | 17% | 29% | 26% | 59 |
| 3 | 6000 | 16% | 26% | 24% | 60 |
| 4 | 6000 | 17% | 23% | 26% | 60 |
| 5 | 6000 | 16% | 35% | 22% | 59 |
| 6 | 6000 | 16% | 43% | 20% | 59 |
| 7 | 6000 | 16% | 39% | 20% | 59 |
| 8 | 6000 | 16% | 27% | 21% | 60 |
| 9 | 6000 | 16% | 22% | 27% | 60 |
| 10 | 6000 | 18% | 25% | 31% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.5 | 9.1 | 1306 | 0.89 |
| AI_2 | 8.2 | 14.7 | 2433 | 1.48 |
| AI_3 | 6.5 | 12.3 | 2048 | 1.38 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.5%  ############################
- New York Avenue           98.5%  ############################
- St. Charles Place         98.5%  ############################
- Tennessee Avenue          98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Water Works               97.9%  ############################
- Kentucky Avenue           97.8%  ############################
- Indiana Avenue            97.8%  ############################

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
