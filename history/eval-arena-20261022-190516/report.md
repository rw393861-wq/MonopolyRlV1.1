# Monopoly self-play report

Run directory: `logs/eval-arena-20261022-190516`
Games logged: 300
Average rounds per game: 57.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 39 | 13.0% |
| random_1 | 84 | 28.0% |
| heuristic_1 | 177 | 59.0% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 30% | 60% | 51 |
| 2 | 30 | 23% | 13% | 63% | 57 |
| 3 | 30 | 0% | 23% | 77% | 56 |
| 4 | 30 | 17% | 37% | 47% | 60 |
| 5 | 30 | 27% | 40% | 33% | 57 |
| 6 | 30 | 10% | 20% | 70% | 61 |
| 7 | 30 | 10% | 27% | 63% | 59 |
| 8 | 30 | 17% | 33% | 50% | 60 |
| 9 | 30 | 10% | 23% | 67% | 62 |
| 10 | 30 | 7% | 33% | 60% | 53 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.6 | 5.0 | 1253 | 0.42 |
| random_1 | 7.6 | 14.8 | 2534 | 1.40 |
| heuristic_1 | 16.1 | 30.1 | 4232 | 2.84 |

## Properties most often held by the winner

- Electric Company          99.3%  ############################
- Illinois Avenue           99.3%  ############################
- B&O Railroad              99.0%  ############################
- St. Charles Place         98.7%  ############################
- St. James Place           98.7%  ############################
- New York Avenue           98.7%  ############################
- Pacific Avenue            98.7%  ############################
- North Carolina Avenue     98.7%  ############################
- Reading Railroad          98.3%  ############################
- Tennessee Avenue          98.3%  ############################
- Indiana Avenue            98.3%  ############################
- Water Works               98.3%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.97 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.96 per space
