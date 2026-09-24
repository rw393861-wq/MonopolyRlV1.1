# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260924-185226`
Games logged: 300
Average rounds per game: 105.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 20 | 6.7% |
| heuristic_1 | 141 | 47.0% |
| heuristic_2 | 139 | 46.3% |

## End condition

- last_standing: 236 (78.7%)
- round_limit: 64 (21.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 43% | 40% | 98 |
| 2 | 30 | 13% | 47% | 40% | 110 |
| 3 | 30 | 3% | 43% | 53% | 105 |
| 4 | 30 | 3% | 43% | 53% | 111 |
| 5 | 30 | 3% | 37% | 60% | 113 |
| 6 | 30 | 3% | 67% | 30% | 101 |
| 7 | 30 | 3% | 33% | 63% | 106 |
| 8 | 30 | 3% | 53% | 43% | 103 |
| 9 | 30 | 10% | 57% | 33% | 95 |
| 10 | 30 | 7% | 47% | 47% | 112 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.7 | 3.0 | 1170 | 0.40 |
| heuristic_1 | 12.2 | 17.2 | 4876 | 0.83 |
| heuristic_2 | 12.9 | 18.3 | 4759 | 1.04 |

## Properties most often held by the winner

- Water Works               91.3%  ############################
- Pennsylvania Railroad     90.3%  ############################
- Mediterranean Avenue      89.7%  ###########################-
- B&O Railroad              89.3%  ###########################-
- St. Charles Place         89.0%  ###########################-
- Baltic Avenue             88.7%  ###########################-
- Indiana Avenue            88.7%  ###########################-
- Boardwalk                 88.7%  ###########################-
- Pacific Avenue            88.0%  ###########################-
- Short Line                88.0%  ###########################-
- Electric Company          87.7%  ###########################-
- New York Avenue           87.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.89 per space
- lightblue  0.86 per space
- pink       0.86 per space
- util       0.90 per space
- orange     0.86 per space
- red        0.87 per space
- yellow     0.86 per space
- green      0.86 per space
- darkblue   0.87 per space
