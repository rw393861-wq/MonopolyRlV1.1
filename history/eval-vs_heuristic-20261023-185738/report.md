# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261023-185738`
Games logged: 300
Average rounds per game: 105.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 54 | 18.0% |
| heuristic_1 | 128 | 42.7% |
| heuristic_2 | 118 | 39.3% |

## End condition

- round_limit: 71 (23.7%)
- last_standing: 229 (76.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 40% | 50% | 107 |
| 2 | 30 | 10% | 40% | 50% | 99 |
| 3 | 30 | 27% | 40% | 33% | 102 |
| 4 | 30 | 17% | 50% | 33% | 114 |
| 5 | 30 | 13% | 47% | 40% | 109 |
| 6 | 30 | 23% | 33% | 43% | 117 |
| 7 | 30 | 30% | 40% | 30% | 86 |
| 8 | 30 | 10% | 50% | 40% | 103 |
| 9 | 30 | 10% | 47% | 43% | 99 |
| 10 | 30 | 30% | 40% | 30% | 115 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.6 | 5.3 | 2027 | 0.21 |
| heuristic_1 | 11.0 | 14.8 | 4123 | 0.76 |
| heuristic_2 | 11.0 | 15.0 | 4046 | 0.75 |

## Properties most often held by the winner

- Pennsylvania Railroad     88.0%  ############################
- Baltic Avenue             87.7%  ############################
- Mediterranean Avenue      87.0%  ############################
- B&O Railroad              87.0%  ############################
- Reading Railroad          86.7%  ############################
- States Avenue             86.3%  ###########################-
- Oriental Avenue           86.3%  ###########################-
- Tennessee Avenue          86.0%  ###########################-
- Short Line                86.0%  ###########################-
- Virginia Avenue           85.7%  ###########################-
- Water Works               85.7%  ###########################-
- Illinois Avenue           85.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.87 per space
- rail       0.87 per space
- lightblue  0.84 per space
- pink       0.86 per space
- util       0.85 per space
- orange     0.84 per space
- red        0.85 per space
- yellow     0.82 per space
- green      0.83 per space
- darkblue   0.84 per space
