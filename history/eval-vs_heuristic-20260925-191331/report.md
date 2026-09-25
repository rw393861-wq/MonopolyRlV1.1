# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260925-191331`
Games logged: 300
Average rounds per game: 97.9

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 29 | 9.7% |
| heuristic_1 | 134 | 44.7% |
| heuristic_2 | 137 | 45.7% |

## End condition

- last_standing: 254 (84.7%)
- round_limit: 46 (15.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 57% | 37% | 86 |
| 2 | 30 | 17% | 30% | 53% | 115 |
| 3 | 30 | 3% | 37% | 60% | 91 |
| 4 | 30 | 13% | 37% | 50% | 86 |
| 5 | 30 | 7% | 53% | 40% | 107 |
| 6 | 30 | 10% | 47% | 43% | 96 |
| 7 | 30 | 7% | 47% | 47% | 106 |
| 8 | 30 | 10% | 43% | 47% | 99 |
| 9 | 30 | 0% | 63% | 37% | 101 |
| 10 | 30 | 23% | 33% | 43% | 92 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.1 | 4.8 | 1516 | 0.73 |
| heuristic_1 | 12.0 | 17.5 | 4529 | 0.84 |
| heuristic_2 | 12.6 | 19.0 | 4728 | 0.97 |

## Properties most often held by the winner

- Pennsylvania Railroad     93.3%  ############################
- B&O Railroad              93.0%  ############################
- Mediterranean Avenue      92.3%  ############################
- Illinois Avenue           92.3%  ############################
- Water Works               92.3%  ############################
- Reading Railroad          92.0%  ############################
- Oriental Avenue           92.0%  ############################
- Electric Company          92.0%  ############################
- Kentucky Avenue           91.0%  ###########################-
- Short Line                91.0%  ###########################-
- Baltic Avenue             90.7%  ###########################-
- Pennsylvania Avenue       90.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.92 per space
- rail       0.92 per space
- lightblue  0.91 per space
- pink       0.90 per space
- util       0.92 per space
- orange     0.89 per space
- red        0.91 per space
- yellow     0.89 per space
- green      0.90 per space
- darkblue   0.89 per space
