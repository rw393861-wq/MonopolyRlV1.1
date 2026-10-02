# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261002-195125`
Games logged: 300
Average rounds per game: 101.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 26 | 8.7% |
| heuristic_1 | 135 | 45.0% |
| heuristic_2 | 139 | 46.3% |

## End condition

- last_standing: 242 (80.7%)
- round_limit: 58 (19.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 53% | 40% | 96 |
| 2 | 30 | 7% | 43% | 50% | 100 |
| 3 | 30 | 3% | 43% | 53% | 103 |
| 4 | 30 | 3% | 60% | 37% | 85 |
| 5 | 30 | 13% | 27% | 60% | 95 |
| 6 | 30 | 3% | 47% | 50% | 112 |
| 7 | 30 | 13% | 50% | 37% | 104 |
| 8 | 30 | 20% | 40% | 40% | 107 |
| 9 | 30 | 7% | 43% | 50% | 92 |
| 10 | 30 | 10% | 43% | 47% | 122 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.8 | 3.8 | 1644 | 0.46 |
| heuristic_1 | 11.8 | 18.8 | 4506 | 0.88 |
| heuristic_2 | 13.1 | 18.7 | 4493 | 0.84 |

## Properties most often held by the winner

- Pennsylvania Railroad     91.3%  ############################
- B&O Railroad              91.0%  ############################
- Reading Railroad          90.0%  ############################
- New York Avenue           90.0%  ############################
- Oriental Avenue           89.0%  ###########################-
- Electric Company          89.0%  ###########################-
- Boardwalk                 89.0%  ###########################-
- Mediterranean Avenue      88.7%  ###########################-
- Baltic Avenue             88.3%  ###########################-
- Water Works               88.3%  ###########################-
- States Avenue             88.0%  ###########################-
- Vermont Avenue            87.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.90 per space
- lightblue  0.87 per space
- pink       0.86 per space
- util       0.89 per space
- orange     0.88 per space
- red        0.86 per space
- yellow     0.86 per space
- green      0.87 per space
- darkblue   0.88 per space
