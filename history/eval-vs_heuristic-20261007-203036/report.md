# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261007-203036`
Games logged: 300
Average rounds per game: 99.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 16 | 5.3% |
| heuristic_1 | 131 | 43.7% |
| heuristic_2 | 153 | 51.0% |

## End condition

- round_limit: 60 (20.0%)
- last_standing: 240 (80.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 53% | 40% | 103 |
| 2 | 30 | 3% | 27% | 70% | 97 |
| 3 | 30 | 0% | 50% | 50% | 91 |
| 4 | 30 | 10% | 50% | 40% | 94 |
| 5 | 30 | 10% | 37% | 53% | 99 |
| 6 | 30 | 3% | 43% | 53% | 118 |
| 7 | 30 | 3% | 37% | 60% | 94 |
| 8 | 30 | 13% | 47% | 40% | 88 |
| 9 | 30 | 3% | 40% | 57% | 94 |
| 10 | 30 | 0% | 53% | 47% | 114 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.0 | 0.8 | 1017 | 0.00 |
| heuristic_1 | 12.0 | 17.4 | 4471 | 0.98 |
| heuristic_2 | 13.8 | 20.0 | 4918 | 1.10 |

## Properties most often held by the winner

- Reading Railroad          91.3%  ############################
- Mediterranean Avenue      91.0%  ############################
- Virginia Avenue           90.7%  ############################
- Vermont Avenue            90.0%  ############################
- Indiana Avenue            89.7%  ###########################-
- Ventnor Avenue            89.3%  ###########################-
- Connecticut Avenue        89.0%  ###########################-
- Baltic Avenue             89.0%  ###########################-
- B&O Railroad              89.0%  ###########################-
- Kentucky Avenue           88.7%  ###########################-
- St. James Place           88.3%  ###########################-
- Short Line                88.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.89 per space
- lightblue  0.88 per space
- pink       0.88 per space
- util       0.87 per space
- orange     0.87 per space
- red        0.89 per space
- yellow     0.87 per space
- green      0.87 per space
- darkblue   0.88 per space
