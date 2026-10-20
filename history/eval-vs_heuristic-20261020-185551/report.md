# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261020-185551`
Games logged: 300
Average rounds per game: 94.0

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 15 | 5.0% |
| heuristic_1 | 149 | 49.7% |
| heuristic_2 | 136 | 45.3% |

## End condition

- last_standing: 255 (85.0%)
- round_limit: 45 (15.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 43% | 53% | 95 |
| 2 | 30 | 13% | 53% | 33% | 94 |
| 3 | 30 | 3% | 60% | 37% | 107 |
| 4 | 30 | 13% | 43% | 43% | 97 |
| 5 | 30 | 7% | 47% | 47% | 79 |
| 6 | 30 | 3% | 57% | 40% | 105 |
| 7 | 30 | 3% | 43% | 53% | 93 |
| 8 | 30 | 0% | 60% | 40% | 94 |
| 9 | 30 | 0% | 33% | 67% | 91 |
| 10 | 30 | 3% | 57% | 40% | 85 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.2 | 1.7 | 903 | 0.00 |
| heuristic_1 | 13.0 | 17.9 | 4595 | 1.01 |
| heuristic_2 | 12.5 | 17.8 | 4446 | 0.99 |

## Properties most often held by the winner

- Reading Railroad          94.3%  ############################
- Baltic Avenue             93.7%  ############################
- B&O Railroad              93.7%  ############################
- Pennsylvania Railroad     92.3%  ###########################-
- Short Line                92.3%  ###########################-
- Vermont Avenue            92.0%  ###########################-
- St. Charles Place         91.7%  ###########################-
- St. James Place           91.7%  ###########################-
- New York Avenue           91.7%  ###########################-
- Connecticut Avenue        91.3%  ###########################-
- States Avenue             91.0%  ###########################-
- Water Works               90.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.92 per space
- rail       0.93 per space
- lightblue  0.90 per space
- pink       0.90 per space
- util       0.90 per space
- orange     0.91 per space
- red        0.89 per space
- yellow     0.89 per space
- green      0.89 per space
- darkblue   0.90 per space
