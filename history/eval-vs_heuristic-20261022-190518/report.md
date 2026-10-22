# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261022-190518`
Games logged: 300
Average rounds per game: 97.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 14 | 4.7% |
| heuristic_1 | 138 | 46.0% |
| heuristic_2 | 148 | 49.3% |

## End condition

- round_limit: 51 (17.0%)
- last_standing: 249 (83.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 43% | 53% | 101 |
| 2 | 30 | 7% | 50% | 43% | 106 |
| 3 | 30 | 3% | 57% | 40% | 94 |
| 4 | 30 | 10% | 37% | 53% | 94 |
| 5 | 30 | 10% | 40% | 50% | 84 |
| 6 | 30 | 0% | 47% | 53% | 97 |
| 7 | 30 | 0% | 50% | 50% | 96 |
| 8 | 30 | 0% | 60% | 40% | 95 |
| 9 | 30 | 3% | 40% | 57% | 113 |
| 10 | 30 | 10% | 37% | 53% | 97 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 1.9 | 1.1 | 1033 | 0.01 |
| heuristic_1 | 12.2 | 19.1 | 4610 | 1.00 |
| heuristic_2 | 13.6 | 18.6 | 4760 | 1.11 |

## Properties most often held by the winner

- Mediterranean Avenue      94.7%  ############################
- Electric Company          92.3%  ###########################-
- Water Works               92.0%  ###########################-
- New York Avenue           91.0%  ###########################-
- Baltic Avenue             91.0%  ###########################-
- Vermont Avenue            90.7%  ###########################-
- Pennsylvania Railroad     90.7%  ###########################-
- B&O Railroad              90.7%  ###########################-
- Reading Railroad          90.7%  ###########################-
- Virginia Avenue           90.3%  ###########################-
- Connecticut Avenue        90.0%  ###########################-
- Indiana Avenue            89.3%  ##########################--

## Colour group pull rate (winner)

- brown      0.93 per space
- rail       0.90 per space
- lightblue  0.89 per space
- pink       0.89 per space
- util       0.92 per space
- orange     0.90 per space
- red        0.88 per space
- yellow     0.87 per space
- green      0.87 per space
- darkblue   0.87 per space
