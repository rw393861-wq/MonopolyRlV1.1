# Monopoly self-play report

Run directory: `logs/eval-arena-20260930-195543`
Games logged: 300
Average rounds per game: 59.7

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 56 | 18.7% |
| random_1 | 77 | 25.7% |
| heuristic_1 | 167 | 55.7% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 43% | 47% | 63 |
| 2 | 30 | 20% | 20% | 60% | 62 |
| 3 | 30 | 23% | 17% | 60% | 57 |
| 4 | 30 | 20% | 27% | 53% | 60 |
| 5 | 30 | 7% | 37% | 57% | 55 |
| 6 | 30 | 23% | 13% | 63% | 59 |
| 7 | 30 | 20% | 30% | 50% | 61 |
| 8 | 30 | 13% | 20% | 67% | 58 |
| 9 | 30 | 20% | 37% | 43% | 58 |
| 10 | 30 | 30% | 13% | 57% | 64 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.1 | 8.8 | 1625 | 0.97 |
| random_1 | 7.1 | 14.4 | 2434 | 1.43 |
| heuristic_1 | 15.2 | 28.4 | 4127 | 2.74 |

## Properties most often held by the winner

- Reading Railroad          99.3%  ############################
- St. James Place           99.3%  ############################
- B&O Railroad              99.3%  ############################
- Pennsylvania Railroad     99.0%  ############################
- Kentucky Avenue           99.0%  ############################
- Indiana Avenue            99.0%  ############################
- St. Charles Place         98.7%  ############################
- States Avenue             98.7%  ############################
- Tennessee Avenue          98.7%  ############################
- Illinois Avenue           98.7%  ############################
- Oriental Avenue           98.3%  ############################
- Vermont Avenue            98.3%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.99 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.97 per space
- green      0.96 per space
- darkblue   0.97 per space
