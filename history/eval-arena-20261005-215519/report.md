# Monopoly self-play report

Run directory: `logs/eval-arena-20261005-215519`
Games logged: 300
Average rounds per game: 63.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 46 | 15.3% |
| random_1 | 97 | 32.3% |
| heuristic_1 | 157 | 52.3% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 23% | 63% | 62 |
| 2 | 30 | 10% | 33% | 57% | 59 |
| 3 | 30 | 23% | 23% | 53% | 61 |
| 4 | 30 | 27% | 33% | 40% | 62 |
| 5 | 30 | 13% | 37% | 50% | 62 |
| 6 | 30 | 10% | 33% | 57% | 64 |
| 7 | 30 | 3% | 43% | 53% | 66 |
| 8 | 30 | 13% | 37% | 50% | 65 |
| 9 | 30 | 13% | 33% | 53% | 60 |
| 10 | 30 | 27% | 27% | 47% | 72 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.1 | 5.8 | 1388 | 0.48 |
| random_1 | 9.0 | 16.1 | 3068 | 1.44 |
| heuristic_1 | 14.4 | 28.7 | 4334 | 2.57 |

## Properties most often held by the winner

- St. Charles Place         99.7%  ############################
- St. James Place           99.7%  ############################
- B&O Railroad              99.7%  ############################
- Water Works               99.3%  ############################
- Vermont Avenue            99.0%  ############################
- Virginia Avenue           99.0%  ############################
- New York Avenue           99.0%  ############################
- Kentucky Avenue           99.0%  ############################
- Indiana Avenue            99.0%  ############################
- Atlantic Avenue           99.0%  ############################
- Reading Railroad          98.7%  ############################
- Tennessee Avenue          98.7%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.99 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
