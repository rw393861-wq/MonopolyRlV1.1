# Monopoly self-play report

Run directory: `logs/eval-arena-20261021-191333`
Games logged: 300
Average rounds per game: 60.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 107 | 35.7% |
| random_1 | 69 | 23.0% |
| heuristic_1 | 124 | 41.3% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 40% | 13% | 47% | 60 |
| 2 | 30 | 37% | 27% | 37% | 63 |
| 3 | 30 | 23% | 27% | 50% | 60 |
| 4 | 30 | 43% | 20% | 37% | 59 |
| 5 | 30 | 30% | 30% | 40% | 60 |
| 6 | 30 | 33% | 30% | 37% | 66 |
| 7 | 30 | 33% | 27% | 40% | 53 |
| 8 | 30 | 40% | 30% | 30% | 60 |
| 9 | 30 | 33% | 13% | 53% | 62 |
| 10 | 30 | 43% | 13% | 43% | 64 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 9.6 | 13.4 | 2708 | 0.85 |
| random_1 | 6.2 | 13.2 | 2259 | 1.31 |
| heuristic_1 | 11.4 | 23.5 | 3463 | 2.35 |

## Properties most often held by the winner

- New York Avenue           99.3%  ############################
- St. James Place           98.3%  ############################
- Tennessee Avenue          98.3%  ############################
- Reading Railroad          98.0%  ############################
- Kentucky Avenue           98.0%  ############################
- Indiana Avenue            98.0%  ############################
- Illinois Avenue           98.0%  ############################
- Park Place                98.0%  ############################
- Oriental Avenue           97.7%  ############################
- Ventnor Avenue            97.7%  ############################
- Marvin Gardens            97.3%  ###########################-
- Boardwalk                 97.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.97 per space
- lightblue  0.97 per space
- pink       0.96 per space
- util       0.96 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.96 per space
- darkblue   0.98 per space
