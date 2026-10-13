# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261013-203746`
Games logged: 300
Average rounds per game: 95.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 20 | 6.7% |
| heuristic_1 | 147 | 49.0% |
| heuristic_2 | 133 | 44.3% |

## End condition

- last_standing: 250 (83.3%)
- round_limit: 50 (16.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 37% | 60% | 86 |
| 2 | 30 | 3% | 60% | 37% | 106 |
| 3 | 30 | 13% | 60% | 27% | 93 |
| 4 | 30 | 10% | 40% | 50% | 93 |
| 5 | 30 | 3% | 53% | 43% | 113 |
| 6 | 30 | 7% | 53% | 40% | 95 |
| 7 | 30 | 7% | 50% | 43% | 94 |
| 8 | 30 | 7% | 50% | 43% | 97 |
| 9 | 30 | 7% | 33% | 60% | 94 |
| 10 | 30 | 7% | 53% | 40% | 87 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.6 | 1.7 | 933 | 0.26 |
| heuristic_1 | 12.5 | 18.8 | 4805 | 1.14 |
| heuristic_2 | 12.5 | 17.6 | 4537 | 1.10 |

## Properties most often held by the winner

- Baltic Avenue             92.3%  ############################
- B&O Railroad              92.3%  ############################
- Pennsylvania Railroad     91.7%  ############################
- Mediterranean Avenue      90.7%  ###########################-
- Reading Railroad          90.3%  ###########################-
- Oriental Avenue           90.3%  ###########################-
- States Avenue             90.0%  ###########################-
- St. James Place           90.0%  ###########################-
- New York Avenue           90.0%  ###########################-
- Indiana Avenue            90.0%  ###########################-
- Atlantic Avenue           90.0%  ###########################-
- Short Line                90.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.92 per space
- rail       0.91 per space
- lightblue  0.89 per space
- pink       0.89 per space
- util       0.89 per space
- orange     0.90 per space
- red        0.89 per space
- yellow     0.89 per space
- green      0.88 per space
- darkblue   0.87 per space
