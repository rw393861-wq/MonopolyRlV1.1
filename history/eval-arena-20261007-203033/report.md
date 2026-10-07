# Monopoly self-play report

Run directory: `logs/eval-arena-20261007-203033`
Games logged: 300
Average rounds per game: 64.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 52 | 17.3% |
| random_1 | 91 | 30.3% |
| heuristic_1 | 157 | 52.3% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 33% | 27% | 40% | 63 |
| 2 | 30 | 17% | 27% | 57% | 72 |
| 3 | 30 | 7% | 33% | 60% | 68 |
| 4 | 30 | 17% | 43% | 40% | 64 |
| 5 | 30 | 17% | 33% | 50% | 68 |
| 6 | 30 | 20% | 27% | 53% | 67 |
| 7 | 30 | 17% | 27% | 57% | 56 |
| 8 | 30 | 7% | 40% | 53% | 62 |
| 9 | 30 | 27% | 27% | 47% | 64 |
| 10 | 30 | 13% | 20% | 67% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.7 | 5.3 | 1523 | 0.47 |
| random_1 | 8.4 | 16.6 | 2932 | 1.60 |
| heuristic_1 | 14.5 | 28.5 | 4270 | 2.49 |

## Properties most often held by the winner

- Kentucky Avenue           99.7%  ############################
- Ventnor Avenue            99.7%  ############################
- Pennsylvania Railroad     99.3%  ############################
- St. James Place           99.3%  ############################
- Atlantic Avenue           99.3%  ############################
- Pacific Avenue            99.3%  ############################
- Reading Railroad          99.0%  ############################
- Vermont Avenue            99.0%  ############################
- Connecticut Avenue        99.0%  ############################
- St. Charles Place         98.7%  ############################
- Tennessee Avenue          98.7%  ############################
- B&O Railroad              98.7%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.99 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.97 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.99 per space
- green      0.98 per space
- darkblue   0.98 per space
