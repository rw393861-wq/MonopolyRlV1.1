# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260928-210733`
Games logged: 300
Average rounds per game: 101.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 44 | 14.7% |
| heuristic_1 | 111 | 37.0% |
| heuristic_2 | 145 | 48.3% |

## End condition

- last_standing: 239 (79.7%)
- round_limit: 61 (20.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 53% | 37% | 93 |
| 2 | 30 | 10% | 33% | 57% | 98 |
| 3 | 30 | 17% | 27% | 57% | 107 |
| 4 | 30 | 10% | 57% | 33% | 102 |
| 5 | 30 | 13% | 47% | 40% | 112 |
| 6 | 30 | 13% | 43% | 43% | 100 |
| 7 | 30 | 10% | 40% | 50% | 94 |
| 8 | 30 | 23% | 30% | 47% | 89 |
| 9 | 30 | 13% | 30% | 57% | 109 |
| 10 | 30 | 27% | 10% | 63% | 110 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.2 | 2.3 | 1567 | 0.15 |
| heuristic_1 | 10.1 | 14.9 | 3978 | 0.85 |
| heuristic_2 | 13.5 | 18.5 | 4630 | 0.98 |

## Properties most often held by the winner

- Mediterranean Avenue      91.3%  ############################
- Baltic Avenue             90.0%  ############################
- Pennsylvania Railroad     90.0%  ############################
- B&O Railroad              89.0%  ###########################-
- St. Charles Place         88.7%  ###########################-
- Electric Company          88.3%  ###########################-
- Tennessee Avenue          88.0%  ###########################-
- Reading Railroad          87.7%  ###########################-
- Indiana Avenue            87.7%  ###########################-
- Water Works               87.7%  ###########################-
- Short Line                87.3%  ###########################-
- Connecticut Avenue        86.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.89 per space
- lightblue  0.85 per space
- pink       0.85 per space
- util       0.88 per space
- orange     0.87 per space
- red        0.87 per space
- yellow     0.86 per space
- green      0.85 per space
- darkblue   0.84 per space
