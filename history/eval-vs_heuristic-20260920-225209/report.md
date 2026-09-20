# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260920-225209`
Games logged: 300
Average rounds per game: 94.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 51 | 17.0% |
| heuristic_1 | 122 | 40.7% |
| heuristic_2 | 127 | 42.3% |

## End condition

- round_limit: 48 (16.0%)
- last_standing: 252 (84.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 37% | 37% | 101 |
| 2 | 30 | 10% | 47% | 43% | 95 |
| 3 | 30 | 13% | 57% | 30% | 102 |
| 4 | 30 | 13% | 60% | 27% | 89 |
| 5 | 30 | 13% | 37% | 50% | 86 |
| 6 | 30 | 23% | 23% | 53% | 98 |
| 7 | 30 | 33% | 30% | 37% | 97 |
| 8 | 30 | 10% | 30% | 60% | 94 |
| 9 | 30 | 20% | 40% | 40% | 94 |
| 10 | 30 | 7% | 47% | 47% | 85 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.1 | 5.8 | 2009 | 0.44 |
| heuristic_1 | 11.1 | 16.7 | 3928 | 1.08 |
| heuristic_2 | 11.5 | 15.1 | 3785 | 0.98 |

## Properties most often held by the winner

- Short Line                91.7%  ############################
- Electric Company          91.0%  ############################
- Baltic Avenue             91.0%  ############################
- Water Works               90.7%  ############################
- Reading Railroad          90.3%  ############################
- Virginia Avenue           90.0%  ###########################-
- North Carolina Avenue     89.7%  ###########################-
- New York Avenue           89.7%  ###########################-
- Indiana Avenue            89.7%  ###########################-
- Connecticut Avenue        89.3%  ###########################-
- Pennsylvania Railroad     89.3%  ###########################-
- B&O Railroad              89.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.90 per space
- lightblue  0.89 per space
- pink       0.89 per space
- util       0.91 per space
- orange     0.89 per space
- red        0.88 per space
- yellow     0.88 per space
- green      0.89 per space
- darkblue   0.89 per space
