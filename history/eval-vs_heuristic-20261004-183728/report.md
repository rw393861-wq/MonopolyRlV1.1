# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261004-183728`
Games logged: 300
Average rounds per game: 104.0

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 35 | 11.7% |
| heuristic_1 | 129 | 43.0% |
| heuristic_2 | 136 | 45.3% |

## End condition

- last_standing: 234 (78.0%)
- round_limit: 66 (22.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 60% | 30% | 94 |
| 2 | 30 | 20% | 23% | 57% | 104 |
| 3 | 30 | 10% | 47% | 43% | 111 |
| 4 | 30 | 3% | 63% | 33% | 108 |
| 5 | 30 | 13% | 43% | 43% | 112 |
| 6 | 30 | 13% | 37% | 50% | 112 |
| 7 | 30 | 10% | 47% | 43% | 112 |
| 8 | 30 | 3% | 33% | 63% | 98 |
| 9 | 30 | 17% | 33% | 50% | 100 |
| 10 | 30 | 17% | 43% | 40% | 89 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.1 | 2.5 | 1410 | 0.04 |
| heuristic_1 | 11.7 | 16.3 | 4386 | 0.75 |
| heuristic_2 | 11.9 | 17.2 | 4501 | 0.88 |

## Properties most often held by the winner

- Mediterranean Avenue      90.0%  ############################
- Baltic Avenue             89.0%  ############################
- Vermont Avenue            88.7%  ############################
- Connecticut Avenue        88.3%  ###########################-
- St. James Place           88.0%  ###########################-
- Kentucky Avenue           88.0%  ###########################-
- Pennsylvania Railroad     87.7%  ###########################-
- New York Avenue           87.7%  ###########################-
- Marvin Gardens            87.3%  ###########################-
- St. Charles Place         87.0%  ###########################-
- Virginia Avenue           87.0%  ###########################-
- Tennessee Avenue          87.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.86 per space
- lightblue  0.88 per space
- pink       0.87 per space
- util       0.85 per space
- orange     0.88 per space
- red        0.86 per space
- yellow     0.85 per space
- green      0.84 per space
- darkblue   0.84 per space
