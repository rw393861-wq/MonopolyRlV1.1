# Monopoly self-play report

Run directory: `logs/eval-arena-20261004-183726`
Games logged: 300
Average rounds per game: 57.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 63 | 21.0% |
| random_1 | 79 | 26.3% |
| heuristic_1 | 158 | 52.7% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 27% | 60% | 61 |
| 2 | 30 | 30% | 37% | 33% | 55 |
| 3 | 30 | 7% | 33% | 60% | 61 |
| 4 | 30 | 33% | 33% | 33% | 55 |
| 5 | 30 | 20% | 20% | 60% | 58 |
| 6 | 30 | 23% | 23% | 53% | 64 |
| 7 | 30 | 20% | 27% | 53% | 55 |
| 8 | 30 | 20% | 13% | 67% | 54 |
| 9 | 30 | 23% | 23% | 53% | 57 |
| 10 | 30 | 20% | 27% | 53% | 54 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.8 | 7.5 | 1617 | 0.71 |
| random_1 | 7.2 | 14.4 | 2462 | 1.40 |
| heuristic_1 | 14.5 | 28.6 | 3899 | 2.65 |

## Properties most often held by the winner

- Tennessee Avenue          99.7%  ############################
- New York Avenue           99.3%  ############################
- Mediterranean Avenue      99.0%  ############################
- St. James Place           98.7%  ############################
- Kentucky Avenue           98.7%  ############################
- Illinois Avenue           98.7%  ############################
- North Carolina Avenue     98.7%  ############################
- Reading Railroad          98.3%  ############################
- Vermont Avenue            98.3%  ############################
- Connecticut Avenue        98.3%  ############################
- Atlantic Avenue           98.3%  ############################
- St. Charles Place         98.0%  ############################

## Colour group pull rate (winner)

- brown      0.98 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.97 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.98 per space
- darkblue   0.97 per space
