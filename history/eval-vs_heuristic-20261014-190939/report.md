# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261014-190939`
Games logged: 300
Average rounds per game: 106.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 28 | 9.3% |
| heuristic_1 | 141 | 47.0% |
| heuristic_2 | 131 | 43.7% |

## End condition

- last_standing: 225 (75.0%)
- round_limit: 75 (25.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 53% | 30% | 105 |
| 2 | 30 | 7% | 53% | 40% | 131 |
| 3 | 30 | 0% | 57% | 43% | 111 |
| 4 | 30 | 10% | 47% | 43% | 107 |
| 5 | 30 | 10% | 33% | 57% | 78 |
| 6 | 30 | 10% | 47% | 43% | 118 |
| 7 | 30 | 10% | 40% | 50% | 104 |
| 8 | 30 | 7% | 47% | 47% | 113 |
| 9 | 30 | 10% | 50% | 40% | 99 |
| 10 | 30 | 13% | 43% | 43% | 98 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.4 | 2.1 | 1412 | 0.15 |
| heuristic_1 | 12.0 | 16.5 | 4367 | 0.70 |
| heuristic_2 | 12.2 | 14.6 | 4113 | 0.69 |

## Properties most often held by the winner

- Water Works               87.0%  ############################
- Mediterranean Avenue      86.7%  ############################
- Virginia Avenue           86.3%  ############################
- Baltic Avenue             86.0%  ############################
- St. Charles Place         86.0%  ############################
- B&O Railroad              85.7%  ############################
- Park Place                85.7%  ############################
- Short Line                85.3%  ###########################-
- Illinois Avenue           85.0%  ###########################-
- Kentucky Avenue           84.7%  ###########################-
- Indiana Avenue            84.7%  ###########################-
- Vermont Avenue            84.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.86 per space
- rail       0.84 per space
- lightblue  0.83 per space
- pink       0.85 per space
- util       0.85 per space
- orange     0.83 per space
- red        0.85 per space
- yellow     0.83 per space
- green      0.84 per space
- darkblue   0.85 per space
