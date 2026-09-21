# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260921-200026`
Games logged: 300
Average rounds per game: 96.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 22 | 7.3% |
| heuristic_1 | 148 | 49.3% |
| heuristic_2 | 130 | 43.3% |

## End condition

- round_limit: 47 (15.7%)
- last_standing: 253 (84.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 57% | 37% | 90 |
| 2 | 30 | 10% | 43% | 47% | 91 |
| 3 | 30 | 10% | 47% | 43% | 96 |
| 4 | 30 | 10% | 57% | 33% | 102 |
| 5 | 30 | 10% | 43% | 47% | 77 |
| 6 | 30 | 7% | 60% | 33% | 100 |
| 7 | 30 | 3% | 57% | 40% | 97 |
| 8 | 30 | 3% | 47% | 50% | 106 |
| 9 | 30 | 7% | 50% | 43% | 102 |
| 10 | 30 | 7% | 33% | 60% | 104 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.3 | 1.6 | 1163 | 0.26 |
| heuristic_1 | 13.5 | 19.7 | 4762 | 1.13 |
| heuristic_2 | 12.0 | 17.3 | 4152 | 1.02 |

## Properties most often held by the winner

- Mediterranean Avenue      92.3%  ############################
- Baltic Avenue             92.3%  ############################
- Pennsylvania Railroad     91.3%  ############################
- St. Charles Place         91.0%  ############################
- Electric Company          91.0%  ############################
- Tennessee Avenue          91.0%  ############################
- Kentucky Avenue           90.7%  ###########################-
- Water Works               90.7%  ###########################-
- Short Line                90.7%  ###########################-
- Park Place                90.7%  ###########################-
- B&O Railroad              90.3%  ###########################-
- Ventnor Avenue            90.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.92 per space
- rail       0.91 per space
- lightblue  0.89 per space
- pink       0.90 per space
- util       0.91 per space
- orange     0.90 per space
- red        0.89 per space
- yellow     0.89 per space
- green      0.89 per space
- darkblue   0.90 per space
