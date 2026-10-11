# Monopoly self-play report

Run directory: `logs/eval-arena-20261011-192746`
Games logged: 300
Average rounds per game: 60.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 60 | 20.0% |
| random_1 | 79 | 26.3% |
| heuristic_1 | 161 | 53.7% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 30% | 50% | 66 |
| 2 | 30 | 10% | 33% | 57% | 53 |
| 3 | 30 | 13% | 23% | 63% | 65 |
| 4 | 30 | 20% | 20% | 60% | 59 |
| 5 | 30 | 17% | 23% | 60% | 64 |
| 6 | 30 | 17% | 37% | 47% | 59 |
| 7 | 30 | 20% | 37% | 43% | 60 |
| 8 | 30 | 30% | 27% | 43% | 58 |
| 9 | 30 | 20% | 17% | 63% | 59 |
| 10 | 30 | 33% | 17% | 50% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.4 | 7.8 | 1642 | 0.77 |
| random_1 | 7.2 | 14.6 | 2515 | 1.37 |
| heuristic_1 | 14.7 | 26.7 | 4026 | 2.37 |

## Properties most often held by the winner

- Reading Railroad          99.3%  ############################
- St. James Place           99.3%  ############################
- Kentucky Avenue           99.3%  ############################
- Electric Company          99.0%  ############################
- St. Charles Place         98.7%  ############################
- Tennessee Avenue          98.7%  ############################
- New York Avenue           98.7%  ############################
- Indiana Avenue            98.7%  ############################
- Oriental Avenue           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Water Works               98.3%  ############################
- Illinois Avenue           98.0%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.97 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.96 per space
