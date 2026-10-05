# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261005-215523`
Games logged: 300
Average rounds per game: 99.7

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 12 | 4.0% |
| heuristic_1 | 143 | 47.7% |
| heuristic_2 | 145 | 48.3% |

## End condition

- last_standing: 238 (79.3%)
- round_limit: 62 (20.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 47% | 47% | 79 |
| 2 | 30 | 0% | 60% | 40% | 92 |
| 3 | 30 | 3% | 60% | 37% | 90 |
| 4 | 30 | 10% | 33% | 57% | 122 |
| 5 | 30 | 3% | 57% | 40% | 100 |
| 6 | 30 | 3% | 37% | 60% | 111 |
| 7 | 30 | 3% | 43% | 53% | 106 |
| 8 | 30 | 0% | 53% | 47% | 97 |
| 9 | 30 | 3% | 40% | 57% | 97 |
| 10 | 30 | 7% | 47% | 47% | 105 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.0 | 0.9 | 765 | 0.09 |
| heuristic_1 | 12.4 | 15.7 | 4359 | 0.81 |
| heuristic_2 | 13.3 | 17.3 | 4531 | 0.75 |

## Properties most often held by the winner

- B&O Railroad              92.3%  ############################
- Reading Railroad          91.3%  ############################
- Pennsylvania Railroad     90.3%  ###########################-
- Atlantic Avenue           89.0%  ###########################-
- Baltic Avenue             88.7%  ###########################-
- Marvin Gardens            88.7%  ###########################-
- Mediterranean Avenue      88.0%  ###########################-
- Electric Company          88.0%  ###########################-
- Vermont Avenue            87.7%  ###########################-
- Short Line                87.3%  ##########################--
- Boardwalk                 87.3%  ##########################--
- Ventnor Avenue            87.0%  ##########################--

## Colour group pull rate (winner)

- brown      0.88 per space
- rail       0.90 per space
- lightblue  0.86 per space
- pink       0.86 per space
- util       0.87 per space
- orange     0.86 per space
- red        0.85 per space
- yellow     0.88 per space
- green      0.85 per space
- darkblue   0.87 per space
