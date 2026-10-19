# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261019-202738`
Games logged: 300
Average rounds per game: 109.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 23 | 7.7% |
| heuristic_1 | 133 | 44.3% |
| heuristic_2 | 144 | 48.0% |

## End condition

- last_standing: 229 (76.3%)
- round_limit: 71 (23.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 50% | 40% | 100 |
| 2 | 30 | 7% | 57% | 37% | 125 |
| 3 | 30 | 0% | 40% | 60% | 109 |
| 4 | 30 | 3% | 33% | 63% | 114 |
| 5 | 30 | 3% | 57% | 40% | 100 |
| 6 | 30 | 7% | 40% | 53% | 111 |
| 7 | 30 | 17% | 47% | 37% | 98 |
| 8 | 30 | 17% | 37% | 47% | 110 |
| 9 | 30 | 3% | 43% | 53% | 111 |
| 10 | 30 | 10% | 40% | 50% | 118 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.6 | 1.2 | 1331 | 0.00 |
| heuristic_1 | 13.1 | 17.9 | 4682 | 0.72 |
| heuristic_2 | 12.1 | 16.8 | 4748 | 0.72 |

## Properties most often held by the winner

- Baltic Avenue             90.7%  ############################
- Mediterranean Avenue      88.7%  ###########################-
- Connecticut Avenue        88.3%  ###########################-
- Pennsylvania Railroad     87.3%  ###########################-
- New York Avenue           87.3%  ###########################-
- Reading Railroad          87.0%  ###########################-
- B&O Railroad              87.0%  ###########################-
- St. Charles Place         86.3%  ###########################-
- Virginia Avenue           86.0%  ###########################-
- North Carolina Avenue     86.0%  ###########################-
- Boardwalk                 86.0%  ###########################-
- Kentucky Avenue           85.7%  ##########################--

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.86 per space
- lightblue  0.84 per space
- pink       0.85 per space
- util       0.85 per space
- orange     0.85 per space
- red        0.85 per space
- yellow     0.83 per space
- green      0.84 per space
- darkblue   0.85 per space
