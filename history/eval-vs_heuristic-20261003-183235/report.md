# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261003-183235`
Games logged: 300
Average rounds per game: 95.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 68 | 22.7% |
| heuristic_1 | 106 | 35.3% |
| heuristic_2 | 126 | 42.0% |

## End condition

- round_limit: 52 (17.3%)
- last_standing: 248 (82.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 33% | 37% | 30% | 83 |
| 2 | 30 | 30% | 27% | 43% | 86 |
| 3 | 30 | 17% | 47% | 37% | 100 |
| 4 | 30 | 17% | 33% | 50% | 89 |
| 5 | 30 | 20% | 33% | 47% | 110 |
| 6 | 30 | 23% | 30% | 47% | 104 |
| 7 | 30 | 17% | 30% | 53% | 99 |
| 8 | 30 | 20% | 50% | 30% | 102 |
| 9 | 30 | 17% | 37% | 47% | 98 |
| 10 | 30 | 33% | 30% | 37% | 86 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 7.0 | 5.1 | 1941 | 0.01 |
| heuristic_1 | 9.3 | 14.0 | 3538 | 0.90 |
| heuristic_2 | 11.4 | 16.2 | 4138 | 1.10 |

## Properties most often held by the winner

- Mediterranean Avenue      91.7%  ############################
- Baltic Avenue             91.3%  ############################
- B&O Railroad              91.3%  ############################
- Short Line                91.0%  ############################
- Water Works               90.7%  ############################
- Pennsylvania Railroad     90.0%  ###########################-
- Tennessee Avenue          90.0%  ###########################-
- Atlantic Avenue           90.0%  ###########################-
- Illinois Avenue           89.7%  ###########################-
- Ventnor Avenue            89.7%  ###########################-
- Reading Railroad          89.3%  ###########################-
- Pacific Avenue            89.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.92 per space
- rail       0.90 per space
- lightblue  0.89 per space
- pink       0.87 per space
- util       0.89 per space
- orange     0.89 per space
- red        0.88 per space
- yellow     0.90 per space
- green      0.88 per space
- darkblue   0.88 per space
