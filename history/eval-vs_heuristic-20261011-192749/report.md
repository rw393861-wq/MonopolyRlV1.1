# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261011-192749`
Games logged: 300
Average rounds per game: 110.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 38 | 12.7% |
| heuristic_1 | 122 | 40.7% |
| heuristic_2 | 140 | 46.7% |

## End condition

- round_limit: 85 (28.3%)
- last_standing: 215 (71.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 53% | 40% | 123 |
| 2 | 30 | 13% | 53% | 33% | 118 |
| 3 | 30 | 17% | 43% | 40% | 101 |
| 4 | 30 | 27% | 20% | 53% | 119 |
| 5 | 30 | 13% | 37% | 50% | 110 |
| 6 | 30 | 3% | 40% | 57% | 116 |
| 7 | 30 | 7% | 37% | 57% | 102 |
| 8 | 30 | 20% | 37% | 43% | 107 |
| 9 | 30 | 13% | 40% | 47% | 87 |
| 10 | 30 | 7% | 47% | 47% | 124 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.7 | 2.3 | 1695 | 0.22 |
| heuristic_1 | 11.6 | 14.5 | 4241 | 0.74 |
| heuristic_2 | 12.4 | 15.0 | 4292 | 0.77 |

## Properties most often held by the winner

- B&O Railroad              86.7%  ############################
- St. Charles Place         86.0%  ############################
- Mediterranean Avenue      85.0%  ###########################-
- Kentucky Avenue           84.7%  ###########################-
- Indiana Avenue            84.3%  ###########################-
- Water Works               84.3%  ###########################-
- Pennsylvania Railroad     84.0%  ###########################-
- Reading Railroad          83.7%  ###########################-
- Oriental Avenue           83.7%  ###########################-
- Short Line                83.3%  ###########################-
- Connecticut Avenue        83.0%  ###########################-
- Pennsylvania Avenue       83.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.84 per space
- rail       0.84 per space
- lightblue  0.83 per space
- pink       0.81 per space
- util       0.83 per space
- orange     0.82 per space
- red        0.83 per space
- yellow     0.82 per space
- green      0.81 per space
- darkblue   0.81 per space
