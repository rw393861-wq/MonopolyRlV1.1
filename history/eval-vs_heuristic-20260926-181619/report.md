# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260926-181619`
Games logged: 300
Average rounds per game: 92.0

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 29 | 9.7% |
| heuristic_1 | 125 | 41.7% |
| heuristic_2 | 146 | 48.7% |

## End condition

- last_standing: 258 (86.0%)
- round_limit: 42 (14.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 43% | 40% | 87 |
| 2 | 30 | 13% | 43% | 43% | 87 |
| 3 | 30 | 3% | 47% | 50% | 91 |
| 4 | 30 | 7% | 40% | 53% | 101 |
| 5 | 30 | 10% | 43% | 47% | 108 |
| 6 | 30 | 10% | 33% | 57% | 96 |
| 7 | 30 | 10% | 43% | 47% | 83 |
| 8 | 30 | 3% | 53% | 43% | 89 |
| 9 | 30 | 7% | 47% | 47% | 87 |
| 10 | 30 | 17% | 23% | 60% | 92 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.0 | 3.1 | 1343 | 0.11 |
| heuristic_1 | 12.1 | 17.8 | 4119 | 1.09 |
| heuristic_2 | 12.4 | 18.5 | 4362 | 1.12 |

## Properties most often held by the winner

- B&O Railroad              92.3%  ############################
- Oriental Avenue           92.0%  ############################
- Tennessee Avenue          92.0%  ############################
- Short Line                92.0%  ############################
- Mediterranean Avenue      91.7%  ############################
- Baltic Avenue             91.7%  ############################
- Reading Railroad          91.7%  ############################
- Ventnor Avenue            91.7%  ############################
- Water Works               91.7%  ############################
- Marvin Gardens            91.3%  ############################
- Boardwalk                 91.0%  ############################
- Connecticut Avenue        90.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.92 per space
- rail       0.92 per space
- lightblue  0.91 per space
- pink       0.90 per space
- util       0.91 per space
- orange     0.91 per space
- red        0.89 per space
- yellow     0.91 per space
- green      0.89 per space
- darkblue   0.90 per space
