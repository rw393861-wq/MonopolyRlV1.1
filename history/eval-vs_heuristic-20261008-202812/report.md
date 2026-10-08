# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261008-202812`
Games logged: 300
Average rounds per game: 104.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 22 | 7.3% |
| heuristic_1 | 133 | 44.3% |
| heuristic_2 | 145 | 48.3% |

## End condition

- round_limit: 64 (21.3%)
- last_standing: 236 (78.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 40% | 47% | 98 |
| 2 | 30 | 0% | 43% | 57% | 84 |
| 3 | 30 | 3% | 57% | 40% | 97 |
| 4 | 30 | 7% | 43% | 50% | 96 |
| 5 | 30 | 7% | 30% | 63% | 113 |
| 6 | 30 | 7% | 43% | 50% | 108 |
| 7 | 30 | 7% | 50% | 43% | 110 |
| 8 | 30 | 17% | 50% | 33% | 110 |
| 9 | 30 | 7% | 43% | 50% | 119 |
| 10 | 30 | 7% | 43% | 50% | 108 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.6 | 2.8 | 1314 | 0.23 |
| heuristic_1 | 12.3 | 18.4 | 4607 | 1.00 |
| heuristic_2 | 13.0 | 19.3 | 4724 | 1.09 |

## Properties most often held by the winner

- Tennessee Avenue          90.3%  ############################
- Electric Company          90.0%  ############################
- Mediterranean Avenue      90.0%  ############################
- Baltic Avenue             89.3%  ############################
- Illinois Avenue           88.7%  ###########################-
- B&O Railroad              88.0%  ###########################-
- Virginia Avenue           87.7%  ###########################-
- Pennsylvania Railroad     87.7%  ###########################-
- Boardwalk                 87.7%  ###########################-
- States Avenue             87.3%  ###########################-
- Reading Railroad          87.0%  ###########################-
- Indiana Avenue            87.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.87 per space
- lightblue  0.86 per space
- pink       0.87 per space
- util       0.89 per space
- orange     0.88 per space
- red        0.88 per space
- yellow     0.86 per space
- green      0.86 per space
- darkblue   0.86 per space
