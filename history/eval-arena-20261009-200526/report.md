# Monopoly self-play report

Run directory: `logs/eval-arena-20261009-200526`
Games logged: 300
Average rounds per game: 60.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 58 | 19.3% |
| random_1 | 96 | 32.0% |
| heuristic_1 | 146 | 48.7% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 40% | 47% | 64 |
| 2 | 30 | 17% | 33% | 50% | 61 |
| 3 | 30 | 23% | 33% | 43% | 61 |
| 4 | 30 | 23% | 27% | 50% | 62 |
| 5 | 30 | 33% | 10% | 57% | 65 |
| 6 | 30 | 23% | 37% | 40% | 59 |
| 7 | 30 | 13% | 43% | 43% | 56 |
| 8 | 30 | 7% | 33% | 60% | 61 |
| 9 | 30 | 20% | 37% | 43% | 61 |
| 10 | 30 | 20% | 27% | 53% | 56 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.2 | 7.6 | 1711 | 0.77 |
| random_1 | 8.8 | 16.5 | 2816 | 1.38 |
| heuristic_1 | 13.4 | 25.9 | 3830 | 2.58 |

## Properties most often held by the winner

- Illinois Avenue           99.3%  ############################
- Reading Railroad          99.0%  ############################
- St. Charles Place         99.0%  ############################
- Tennessee Avenue          99.0%  ############################
- B&O Railroad              99.0%  ############################
- Water Works               99.0%  ############################
- Pacific Avenue            99.0%  ############################
- New York Avenue           98.7%  ############################
- Kentucky Avenue           98.7%  ############################
- Vermont Avenue            98.3%  ############################
- Connecticut Avenue        98.3%  ############################
- Electric Company          98.3%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.99 per space
- orange     0.98 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
