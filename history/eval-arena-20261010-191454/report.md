# Monopoly self-play report

Run directory: `logs/eval-arena-20261010-191454`
Games logged: 300
Average rounds per game: 63.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 42 | 14.0% |
| random_1 | 81 | 27.0% |
| heuristic_1 | 177 | 59.0% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 23% | 63% | 70 |
| 2 | 30 | 13% | 43% | 43% | 65 |
| 3 | 30 | 17% | 17% | 67% | 64 |
| 4 | 30 | 17% | 23% | 60% | 58 |
| 5 | 30 | 23% | 33% | 43% | 63 |
| 6 | 30 | 3% | 47% | 50% | 61 |
| 7 | 30 | 13% | 13% | 73% | 58 |
| 8 | 30 | 10% | 33% | 57% | 66 |
| 9 | 30 | 17% | 13% | 70% | 61 |
| 10 | 30 | 13% | 23% | 63% | 66 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.7 | 7.5 | 1559 | 1.02 |
| random_1 | 7.5 | 15.3 | 2617 | 1.52 |
| heuristic_1 | 16.3 | 29.5 | 4541 | 2.75 |

## Properties most often held by the winner

- St. Charles Place         99.7%  ############################
- Electric Company          99.0%  ############################
- Illinois Avenue           99.0%  ############################
- Water Works               99.0%  ############################
- Pacific Avenue            99.0%  ############################
- Reading Railroad          98.7%  ############################
- Indiana Avenue            98.7%  ############################
- Connecticut Avenue        98.3%  ############################
- States Avenue             98.3%  ############################
- Pennsylvania Avenue       98.3%  ############################
- Virginia Avenue           98.0%  ############################
- Tennessee Avenue          98.0%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.99 per space
- util       0.99 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.98 per space
- darkblue   0.97 per space
