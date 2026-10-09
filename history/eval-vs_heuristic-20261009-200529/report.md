# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261009-200529`
Games logged: 300
Average rounds per game: 105.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 34 | 11.3% |
| heuristic_1 | 128 | 42.7% |
| heuristic_2 | 138 | 46.0% |

## End condition

- last_standing: 235 (78.3%)
- round_limit: 65 (21.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 60% | 37% | 108 |
| 2 | 30 | 10% | 37% | 53% | 102 |
| 3 | 30 | 10% | 43% | 47% | 119 |
| 4 | 30 | 17% | 43% | 40% | 109 |
| 5 | 30 | 20% | 33% | 47% | 104 |
| 6 | 30 | 13% | 50% | 37% | 102 |
| 7 | 30 | 3% | 30% | 67% | 98 |
| 8 | 30 | 7% | 43% | 50% | 106 |
| 9 | 30 | 20% | 47% | 33% | 99 |
| 10 | 30 | 10% | 40% | 50% | 103 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.4 | 3.7 | 1479 | 0.29 |
| heuristic_1 | 12.1 | 17.2 | 4341 | 0.79 |
| heuristic_2 | 12.3 | 17.0 | 4471 | 0.81 |

## Properties most often held by the winner

- Baltic Avenue             89.7%  ############################
- Water Works               89.0%  ############################
- Reading Railroad          88.7%  ############################
- Short Line                88.7%  ############################
- St. Charles Place         88.3%  ############################
- Tennessee Avenue          88.3%  ############################
- B&O Railroad              88.3%  ############################
- Pennsylvania Railroad     87.7%  ###########################-
- Ventnor Avenue            87.7%  ###########################-
- Indiana Avenue            87.3%  ###########################-
- Boardwalk                 87.3%  ###########################-
- Mediterranean Avenue      87.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.88 per space
- rail       0.88 per space
- lightblue  0.86 per space
- pink       0.87 per space
- util       0.88 per space
- orange     0.86 per space
- red        0.87 per space
- yellow     0.86 per space
- green      0.86 per space
- darkblue   0.86 per space
