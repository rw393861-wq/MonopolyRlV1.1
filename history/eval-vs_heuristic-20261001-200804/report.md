# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261001-200804`
Games logged: 300
Average rounds per game: 99.7

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 23 | 7.7% |
| heuristic_1 | 142 | 47.3% |
| heuristic_2 | 135 | 45.0% |

## End condition

- last_standing: 248 (82.7%)
- round_limit: 52 (17.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 40% | 57% | 88 |
| 2 | 30 | 7% | 37% | 57% | 113 |
| 3 | 30 | 10% | 33% | 57% | 110 |
| 4 | 30 | 7% | 50% | 43% | 85 |
| 5 | 30 | 10% | 57% | 33% | 105 |
| 6 | 30 | 20% | 43% | 37% | 87 |
| 7 | 30 | 3% | 60% | 37% | 100 |
| 8 | 30 | 3% | 63% | 33% | 105 |
| 9 | 30 | 10% | 53% | 37% | 105 |
| 10 | 30 | 3% | 37% | 60% | 99 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.8 | 1.6 | 1404 | 0.01 |
| heuristic_1 | 12.5 | 19.0 | 4591 | 1.02 |
| heuristic_2 | 12.4 | 18.1 | 4517 | 0.93 |

## Properties most often held by the winner

- Mediterranean Avenue      93.0%  ############################
- Baltic Avenue             92.7%  ############################
- Tennessee Avenue          90.7%  ###########################-
- B&O Railroad              90.3%  ###########################-
- St. Charles Place         89.7%  ###########################-
- Boardwalk                 89.0%  ###########################-
- Short Line                88.7%  ###########################-
- Oriental Avenue           88.3%  ###########################-
- States Avenue             88.3%  ###########################-
- Virginia Avenue           88.3%  ###########################-
- Pennsylvania Railroad     88.3%  ###########################-
- Ventnor Avenue            88.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.93 per space
- rail       0.89 per space
- lightblue  0.87 per space
- pink       0.89 per space
- util       0.88 per space
- orange     0.89 per space
- red        0.86 per space
- yellow     0.88 per space
- green      0.88 per space
- darkblue   0.89 per space
