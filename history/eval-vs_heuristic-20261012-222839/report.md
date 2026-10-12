# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261012-222839`
Games logged: 300
Average rounds per game: 101.8

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 39 | 13.0% |
| heuristic_1 | 123 | 41.0% |
| heuristic_2 | 138 | 46.0% |

## End condition

- last_standing: 239 (79.7%)
- round_limit: 61 (20.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 30% | 53% | 92 |
| 2 | 30 | 7% | 63% | 30% | 117 |
| 3 | 30 | 10% | 33% | 57% | 114 |
| 4 | 30 | 20% | 30% | 50% | 103 |
| 5 | 30 | 7% | 47% | 47% | 100 |
| 6 | 30 | 17% | 40% | 43% | 111 |
| 7 | 30 | 3% | 40% | 57% | 102 |
| 8 | 30 | 17% | 43% | 40% | 94 |
| 9 | 30 | 20% | 47% | 33% | 91 |
| 10 | 30 | 13% | 37% | 50% | 94 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.5 | 4.3 | 1736 | 0.53 |
| heuristic_1 | 11.1 | 17.2 | 4186 | 0.88 |
| heuristic_2 | 12.2 | 18.3 | 4310 | 0.96 |

## Properties most often held by the winner

- Baltic Avenue             91.0%  ############################
- Mediterranean Avenue      90.0%  ############################
- B&O Railroad              90.0%  ############################
- Reading Railroad          88.0%  ###########################-
- Short Line                88.0%  ###########################-
- Ventnor Avenue            87.7%  ###########################-
- Pennsylvania Railroad     87.3%  ###########################-
- Kentucky Avenue           87.3%  ###########################-
- St. Charles Place         87.0%  ###########################-
- States Avenue             87.0%  ###########################-
- Electric Company          86.7%  ###########################-
- St. James Place           86.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.88 per space
- lightblue  0.86 per space
- pink       0.86 per space
- util       0.86 per space
- orange     0.85 per space
- red        0.86 per space
- yellow     0.86 per space
- green      0.86 per space
- darkblue   0.84 per space
