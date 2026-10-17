# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261017-174908`
Games logged: 300
Average rounds per game: 114.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 31 | 10.3% |
| heuristic_1 | 124 | 41.3% |
| heuristic_2 | 145 | 48.3% |

## End condition

- last_standing: 211 (70.3%)
- round_limit: 89 (29.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 50% | 43% | 108 |
| 2 | 30 | 7% | 50% | 43% | 112 |
| 3 | 30 | 13% | 57% | 30% | 117 |
| 4 | 30 | 3% | 40% | 57% | 114 |
| 5 | 30 | 23% | 20% | 57% | 107 |
| 6 | 30 | 13% | 43% | 43% | 129 |
| 7 | 30 | 3% | 50% | 47% | 121 |
| 8 | 30 | 7% | 23% | 70% | 104 |
| 9 | 30 | 17% | 43% | 40% | 126 |
| 10 | 30 | 10% | 37% | 53% | 107 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.0 | 2.2 | 1315 | 0.05 |
| heuristic_1 | 11.5 | 13.8 | 4380 | 0.61 |
| heuristic_2 | 12.2 | 14.3 | 4791 | 0.59 |

## Properties most often held by the winner

- Mediterranean Avenue      86.0%  ############################
- Baltic Avenue             85.7%  ############################
- Vermont Avenue            85.3%  ############################
- Electric Company          85.3%  ############################
- B&O Railroad              85.0%  ############################
- Reading Railroad          84.0%  ###########################-
- Oriental Avenue           84.0%  ###########################-
- Water Works               84.0%  ###########################-
- St. James Place           83.7%  ###########################-
- Indiana Avenue            83.7%  ###########################-
- Connecticut Avenue        83.0%  ###########################-
- New York Avenue           83.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.86 per space
- rail       0.82 per space
- lightblue  0.84 per space
- pink       0.81 per space
- util       0.85 per space
- orange     0.82 per space
- red        0.82 per space
- yellow     0.80 per space
- green      0.82 per space
- darkblue   0.80 per space
