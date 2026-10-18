# Monopoly self-play report

Run directory: `logs/eval-arena-20261018-174923`
Games logged: 300
Average rounds per game: 63.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 38 | 12.7% |
| random_1 | 98 | 32.7% |
| heuristic_1 | 164 | 54.7% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 23% | 67% | 64 |
| 2 | 30 | 13% | 40% | 47% | 58 |
| 3 | 30 | 20% | 37% | 43% | 60 |
| 4 | 30 | 17% | 30% | 53% | 59 |
| 5 | 30 | 13% | 27% | 60% | 68 |
| 6 | 30 | 7% | 20% | 73% | 68 |
| 7 | 30 | 13% | 23% | 63% | 69 |
| 8 | 30 | 17% | 43% | 40% | 68 |
| 9 | 30 | 10% | 40% | 50% | 63 |
| 10 | 30 | 7% | 43% | 50% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.4 | 4.3 | 1286 | 0.54 |
| random_1 | 9.0 | 17.3 | 3088 | 1.63 |
| heuristic_1 | 15.1 | 30.7 | 4460 | 2.79 |

## Properties most often held by the winner

- Oriental Avenue           99.7%  ############################
- Vermont Avenue            99.7%  ############################
- Electric Company          99.3%  ############################
- Tennessee Avenue          99.3%  ############################
- Boardwalk                 99.3%  ############################
- Connecticut Avenue        99.0%  ############################
- St. James Place           99.0%  ############################
- Kentucky Avenue           99.0%  ############################
- B&O Railroad              99.0%  ############################
- Reading Railroad          98.7%  ############################
- St. Charles Place         98.7%  ############################
- Indiana Avenue            98.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.99 per space
- pink       0.98 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.97 per space
- green      0.98 per space
- darkblue   0.98 per space
