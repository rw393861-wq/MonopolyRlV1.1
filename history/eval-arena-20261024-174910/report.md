# Monopoly self-play report

Run directory: `logs/eval-arena-20261024-174910`
Games logged: 300
Average rounds per game: 62.8

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 44 | 14.7% |
| random_1 | 79 | 26.3% |
| heuristic_1 | 177 | 59.0% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 23% | 23% | 53% | 57 |
| 2 | 30 | 13% | 17% | 70% | 59 |
| 3 | 30 | 20% | 17% | 63% | 71 |
| 4 | 30 | 27% | 30% | 43% | 66 |
| 5 | 30 | 17% | 27% | 57% | 60 |
| 6 | 30 | 13% | 33% | 53% | 64 |
| 7 | 30 | 13% | 23% | 63% | 65 |
| 8 | 30 | 7% | 17% | 77% | 63 |
| 9 | 30 | 10% | 23% | 67% | 58 |
| 10 | 30 | 3% | 53% | 43% | 64 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.1 | 6.6 | 1481 | 0.61 |
| random_1 | 7.3 | 15.6 | 2655 | 1.41 |
| heuristic_1 | 16.2 | 30.1 | 4452 | 2.49 |

## Properties most often held by the winner

- Kentucky Avenue           99.7%  ############################
- St. Charles Place         99.3%  ############################
- New York Avenue           99.3%  ############################
- Illinois Avenue           99.3%  ############################
- Oriental Avenue           99.0%  ############################
- Vermont Avenue            99.0%  ############################
- Electric Company          99.0%  ############################
- Virginia Avenue           99.0%  ############################
- St. James Place           99.0%  ############################
- Tennessee Avenue          99.0%  ############################
- B&O Railroad              99.0%  ############################
- Boardwalk                 99.0%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.99 per space
- pink       0.99 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.98 per space
