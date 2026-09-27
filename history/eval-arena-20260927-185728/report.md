# Monopoly self-play report

Run directory: `logs/eval-arena-20260927-185728`
Games logged: 300
Average rounds per game: 62.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 43 | 14.3% |
| random_1 | 78 | 26.0% |
| heuristic_1 | 179 | 59.7% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 33% | 60% | 61 |
| 2 | 30 | 20% | 17% | 63% | 65 |
| 3 | 30 | 27% | 23% | 50% | 65 |
| 4 | 30 | 37% | 13% | 50% | 65 |
| 5 | 30 | 10% | 33% | 57% | 65 |
| 6 | 30 | 3% | 37% | 60% | 57 |
| 7 | 30 | 13% | 27% | 60% | 63 |
| 8 | 30 | 10% | 20% | 70% | 55 |
| 9 | 30 | 10% | 23% | 67% | 63 |
| 10 | 30 | 7% | 33% | 60% | 63 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.9 | 6.9 | 1543 | 0.71 |
| random_1 | 7.2 | 14.6 | 2575 | 1.41 |
| heuristic_1 | 16.5 | 33.0 | 4528 | 2.91 |

## Properties most often held by the winner

- Tennessee Avenue         100.0%  ############################
- Reading Railroad          99.7%  ############################
- New York Avenue           99.7%  ############################
- B&O Railroad              99.7%  ############################
- Electric Company          99.3%  ############################
- Kentucky Avenue           99.3%  ############################
- Indiana Avenue            99.3%  ############################
- Water Works               99.3%  ############################
- St. Charles Place         99.0%  ############################
- Virginia Avenue           99.0%  ############################
- Pennsylvania Railroad     99.0%  ############################
- Atlantic Avenue           99.0%  ############################

## Colour group pull rate (winner)

- brown      0.98 per space
- rail       0.99 per space
- lightblue  0.98 per space
- pink       0.99 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.97 per space
