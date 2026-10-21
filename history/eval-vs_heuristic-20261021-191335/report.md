# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261021-191335`
Games logged: 300
Average rounds per game: 97.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 58 | 19.3% |
| heuristic_1 | 112 | 37.3% |
| heuristic_2 | 130 | 43.3% |

## End condition

- round_limit: 52 (17.3%)
- last_standing: 248 (82.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 40% | 33% | 99 |
| 2 | 30 | 20% | 33% | 47% | 102 |
| 3 | 30 | 10% | 53% | 37% | 105 |
| 4 | 30 | 20% | 37% | 43% | 105 |
| 5 | 30 | 13% | 30% | 57% | 95 |
| 6 | 30 | 23% | 33% | 43% | 102 |
| 7 | 30 | 27% | 27% | 47% | 92 |
| 8 | 30 | 13% | 60% | 27% | 92 |
| 9 | 30 | 20% | 27% | 53% | 85 |
| 10 | 30 | 20% | 33% | 47% | 95 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.6 | 6.3 | 2092 | 0.40 |
| heuristic_1 | 10.2 | 15.8 | 3895 | 0.84 |
| heuristic_2 | 11.9 | 16.9 | 4148 | 0.99 |

## Properties most often held by the winner

- Baltic Avenue             91.3%  ############################
- Water Works               91.3%  ############################
- Tennessee Avenue          90.7%  ############################
- Illinois Avenue           90.0%  ############################
- Electric Company          90.0%  ############################
- B&O Railroad              90.0%  ############################
- Atlantic Avenue           90.0%  ############################
- Ventnor Avenue            89.7%  ###########################-
- Kentucky Avenue           89.0%  ###########################-
- St. Charles Place         89.0%  ###########################-
- Pennsylvania Railroad     88.7%  ###########################-
- Mediterranean Avenue      88.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.89 per space
- lightblue  0.88 per space
- pink       0.88 per space
- util       0.91 per space
- orange     0.89 per space
- red        0.89 per space
- yellow     0.89 per space
- green      0.87 per space
- darkblue   0.87 per space
