# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261018-174926`
Games logged: 300
Average rounds per game: 100.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 17 | 5.7% |
| heuristic_1 | 120 | 40.0% |
| heuristic_2 | 163 | 54.3% |

## End condition

- last_standing: 244 (81.3%)
- round_limit: 56 (18.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 60% | 37% | 74 |
| 2 | 30 | 10% | 47% | 43% | 108 |
| 3 | 30 | 7% | 33% | 60% | 100 |
| 4 | 30 | 7% | 50% | 43% | 101 |
| 5 | 30 | 13% | 30% | 57% | 126 |
| 6 | 30 | 7% | 50% | 43% | 92 |
| 7 | 30 | 7% | 30% | 63% | 103 |
| 8 | 30 | 0% | 40% | 60% | 114 |
| 9 | 30 | 0% | 27% | 73% | 91 |
| 10 | 30 | 3% | 33% | 63% | 95 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 1.9 | 1.0 | 1016 | 0.10 |
| heuristic_1 | 11.0 | 15.7 | 4309 | 0.81 |
| heuristic_2 | 14.6 | 21.1 | 5072 | 1.06 |

## Properties most often held by the winner

- Baltic Avenue             91.3%  ############################
- Mediterranean Avenue      90.3%  ############################
- Pennsylvania Railroad     89.7%  ###########################-
- Connecticut Avenue        89.3%  ###########################-
- New York Avenue           89.0%  ###########################-
- Electric Company          88.3%  ###########################-
- B&O Railroad              88.0%  ###########################-
- Vermont Avenue            87.7%  ###########################-
- Tennessee Avenue          87.7%  ###########################-
- Pennsylvania Avenue       87.7%  ###########################-
- Reading Railroad          87.3%  ###########################-
- Kentucky Avenue           87.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.88 per space
- lightblue  0.88 per space
- pink       0.86 per space
- util       0.88 per space
- orange     0.88 per space
- red        0.86 per space
- yellow     0.87 per space
- green      0.86 per space
- darkblue   0.86 per space
