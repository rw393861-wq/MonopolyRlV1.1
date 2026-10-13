# Monopoly self-play report

Run directory: `logs/eval-arena-20261013-203743`
Games logged: 300
Average rounds per game: 64.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 35 | 11.7% |
| random_1 | 81 | 27.0% |
| heuristic_1 | 184 | 61.3% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 20% | 67% | 61 |
| 2 | 30 | 3% | 23% | 73% | 63 |
| 3 | 30 | 13% | 37% | 50% | 62 |
| 4 | 30 | 10% | 23% | 67% | 68 |
| 5 | 30 | 17% | 27% | 57% | 63 |
| 6 | 30 | 3% | 33% | 63% | 68 |
| 7 | 30 | 17% | 30% | 53% | 69 |
| 8 | 30 | 17% | 23% | 60% | 58 |
| 9 | 30 | 13% | 27% | 60% | 69 |
| 10 | 30 | 10% | 27% | 63% | 62 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.2 | 4.1 | 1089 | 0.64 |
| random_1 | 7.5 | 16.3 | 3079 | 1.53 |
| heuristic_1 | 16.9 | 32.0 | 5127 | 3.05 |

## Properties most often held by the winner

- Reading Railroad         100.0%  ############################
- Tennessee Avenue          99.7%  ############################
- New York Avenue           99.7%  ############################
- Illinois Avenue           99.7%  ############################
- Boardwalk                 99.7%  ############################
- Virginia Avenue           99.3%  ############################
- Pennsylvania Railroad     99.3%  ############################
- Indiana Avenue            99.3%  ############################
- B&O Railroad              99.3%  ############################
- Ventnor Avenue            99.3%  ############################
- Water Works               99.3%  ############################
- Marvin Gardens            99.3%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.99 per space
- lightblue  0.99 per space
- pink       0.99 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.99 per space
- green      0.98 per space
- darkblue   0.98 per space
