# Monopoly self-play report

Run directory: `logs/eval-arena-20261014-190937`
Games logged: 300
Average rounds per game: 65.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 47 | 15.7% |
| random_1 | 98 | 32.7% |
| heuristic_1 | 155 | 51.7% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 43% | 37% | 68 |
| 2 | 30 | 30% | 30% | 40% | 60 |
| 3 | 30 | 27% | 37% | 37% | 64 |
| 4 | 30 | 10% | 27% | 63% | 65 |
| 5 | 30 | 13% | 40% | 47% | 68 |
| 6 | 30 | 17% | 37% | 47% | 67 |
| 7 | 30 | 10% | 43% | 47% | 69 |
| 8 | 30 | 23% | 23% | 53% | 65 |
| 9 | 30 | 3% | 23% | 73% | 65 |
| 10 | 30 | 3% | 23% | 73% | 64 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.3 | 7.6 | 1716 | 0.65 |
| random_1 | 9.0 | 16.1 | 2915 | 1.42 |
| heuristic_1 | 14.2 | 27.8 | 4135 | 2.50 |

## Properties most often held by the winner

- Reading Railroad          99.3%  ############################
- Tennessee Avenue          99.3%  ############################
- New York Avenue           99.3%  ############################
- Vermont Avenue            99.0%  ############################
- St. Charles Place         99.0%  ############################
- Illinois Avenue           99.0%  ############################
- B&O Railroad              99.0%  ############################
- Virginia Avenue           98.7%  ############################
- Kentucky Avenue           98.7%  ############################
- Indiana Avenue            98.7%  ############################
- Ventnor Avenue            98.7%  ############################
- Boardwalk                 98.7%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.99 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.97 per space
