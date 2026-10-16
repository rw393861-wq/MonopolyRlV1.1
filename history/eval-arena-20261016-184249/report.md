# Monopoly self-play report

Run directory: `logs/eval-arena-20261016-184249`
Games logged: 300
Average rounds per game: 59.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 56 | 18.7% |
| random_1 | 99 | 33.0% |
| heuristic_1 | 145 | 48.3% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 30% | 53% | 60 |
| 2 | 30 | 27% | 23% | 50% | 61 |
| 3 | 30 | 3% | 30% | 67% | 60 |
| 4 | 30 | 20% | 23% | 57% | 56 |
| 5 | 30 | 20% | 33% | 47% | 60 |
| 6 | 30 | 20% | 37% | 43% | 59 |
| 7 | 30 | 23% | 37% | 40% | 62 |
| 8 | 30 | 20% | 27% | 53% | 64 |
| 9 | 30 | 13% | 53% | 33% | 57 |
| 10 | 30 | 23% | 37% | 40% | 57 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.1 | 6.8 | 1445 | 0.78 |
| random_1 | 9.1 | 17.6 | 3079 | 1.65 |
| heuristic_1 | 13.1 | 25.4 | 3766 | 2.71 |

## Properties most often held by the winner

- Illinois Avenue           98.7%  ############################
- St. Charles Place         98.3%  ############################
- Pennsylvania Railroad     98.3%  ############################
- Water Works               98.3%  ############################
- Reading Railroad          98.0%  ############################
- Oriental Avenue           98.0%  ############################
- Virginia Avenue           98.0%  ############################
- Ventnor Avenue            98.0%  ############################
- Tennessee Avenue          97.7%  ############################
- Kentucky Avenue           97.7%  ############################
- B&O Railroad              97.7%  ############################
- Atlantic Avenue           97.7%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.97 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.97 per space
- orange     0.97 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
