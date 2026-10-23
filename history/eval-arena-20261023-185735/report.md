# Monopoly self-play report

Run directory: `logs/eval-arena-20261023-185735`
Games logged: 300
Average rounds per game: 62.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 72 | 24.0% |
| random_1 | 83 | 27.7% |
| heuristic_1 | 145 | 48.3% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 20% | 60% | 62 |
| 2 | 30 | 20% | 27% | 53% | 61 |
| 3 | 30 | 30% | 30% | 40% | 62 |
| 4 | 30 | 27% | 27% | 47% | 57 |
| 5 | 30 | 40% | 23% | 37% | 63 |
| 6 | 30 | 3% | 37% | 60% | 60 |
| 7 | 30 | 30% | 23% | 47% | 64 |
| 8 | 30 | 13% | 40% | 47% | 64 |
| 9 | 30 | 23% | 27% | 50% | 70 |
| 10 | 30 | 33% | 23% | 43% | 58 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.4 | 9.4 | 1959 | 0.64 |
| random_1 | 7.6 | 15.8 | 2662 | 1.61 |
| heuristic_1 | 13.3 | 27.3 | 3793 | 2.66 |

## Properties most often held by the winner

- Electric Company          99.0%  ############################
- Tennessee Avenue          99.0%  ############################
- New York Avenue           99.0%  ############################
- St. James Place           98.7%  ############################
- Illinois Avenue           98.7%  ############################
- Reading Railroad          98.3%  ############################
- Oriental Avenue           98.0%  ############################
- Virginia Avenue           98.0%  ############################
- B&O Railroad              98.0%  ############################
- North Carolina Avenue     98.0%  ############################
- St. Charles Place         97.7%  ############################
- Atlantic Avenue           97.7%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.97 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.97 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
