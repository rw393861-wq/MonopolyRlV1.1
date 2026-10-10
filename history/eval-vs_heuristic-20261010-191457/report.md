# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261010-191457`
Games logged: 300
Average rounds per game: 97.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 36 | 12.0% |
| heuristic_1 | 133 | 44.3% |
| heuristic_2 | 131 | 43.7% |

## End condition

- round_limit: 47 (15.7%)
- last_standing: 253 (84.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 33% | 53% | 99 |
| 2 | 30 | 7% | 60% | 33% | 116 |
| 3 | 30 | 13% | 40% | 47% | 87 |
| 4 | 30 | 13% | 57% | 30% | 93 |
| 5 | 30 | 17% | 37% | 47% | 86 |
| 6 | 30 | 17% | 33% | 50% | 99 |
| 7 | 30 | 13% | 50% | 37% | 92 |
| 8 | 30 | 10% | 50% | 40% | 106 |
| 9 | 30 | 10% | 40% | 50% | 97 |
| 10 | 30 | 7% | 43% | 50% | 99 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.1 | 3.9 | 1731 | 0.54 |
| heuristic_1 | 12.4 | 19.3 | 4556 | 1.07 |
| heuristic_2 | 12.2 | 18.2 | 4419 | 1.04 |

## Properties most often held by the winner

- Connecticut Avenue        93.3%  ############################
- Ventnor Avenue            91.7%  ############################
- Short Line                91.3%  ###########################-
- Vermont Avenue            91.0%  ###########################-
- Tennessee Avenue          91.0%  ###########################-
- B&O Railroad              91.0%  ###########################-
- Reading Railroad          90.7%  ###########################-
- Park Place                90.3%  ###########################-
- Virginia Avenue           90.0%  ###########################-
- Illinois Avenue           90.0%  ###########################-
- St. Charles Place         89.7%  ###########################-
- St. James Place           89.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.91 per space
- lightblue  0.91 per space
- pink       0.90 per space
- util       0.89 per space
- orange     0.90 per space
- red        0.89 per space
- yellow     0.89 per space
- green      0.89 per space
- darkblue   0.89 per space
