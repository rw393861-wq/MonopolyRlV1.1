# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260920-233132`
Games logged: 300
Average rounds per game: 109.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 40 | 13.3% |
| heuristic_1 | 135 | 45.0% |
| heuristic_2 | 125 | 41.7% |

## End condition

- round_limit: 83 (27.7%)
- last_standing: 217 (72.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 50% | 33% | 131 |
| 2 | 30 | 7% | 50% | 43% | 96 |
| 3 | 30 | 20% | 33% | 47% | 107 |
| 4 | 30 | 7% | 50% | 43% | 111 |
| 5 | 30 | 13% | 57% | 30% | 109 |
| 6 | 30 | 20% | 37% | 43% | 111 |
| 7 | 30 | 13% | 43% | 43% | 105 |
| 8 | 30 | 3% | 50% | 47% | 122 |
| 9 | 30 | 13% | 40% | 47% | 100 |
| 10 | 30 | 20% | 40% | 40% | 100 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.9 | 2.8 | 1569 | 0.00 |
| heuristic_1 | 12.1 | 15.6 | 4487 | 0.92 |
| heuristic_2 | 10.7 | 15.7 | 4421 | 0.91 |

## Properties most often held by the winner

- Mediterranean Avenue      88.3%  ############################
- Baltic Avenue             88.0%  ############################
- Water Works               87.0%  ############################
- States Avenue             87.0%  ############################
- B&O Railroad              86.7%  ###########################-
- Short Line                86.3%  ###########################-
- Indiana Avenue            86.0%  ###########################-
- Oriental Avenue           85.3%  ###########################-
- Virginia Avenue           85.0%  ###########################-
- Kentucky Avenue           84.7%  ###########################-
- Atlantic Avenue           84.7%  ###########################-
- St. Charles Place         84.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.88 per space
- rail       0.85 per space
- lightblue  0.83 per space
- pink       0.85 per space
- util       0.85 per space
- orange     0.83 per space
- red        0.85 per space
- yellow     0.84 per space
- green      0.79 per space
- darkblue   0.79 per space
