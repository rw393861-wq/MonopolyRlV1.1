# Monopoly self-play report

Run directory: `logs/eval-arena-20261002-195122`
Games logged: 300
Average rounds per game: 59.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 47 | 15.7% |
| random_1 | 103 | 34.3% |
| heuristic_1 | 150 | 50.0% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 40% | 57% | 60 |
| 2 | 30 | 17% | 33% | 50% | 62 |
| 3 | 30 | 13% | 47% | 40% | 61 |
| 4 | 30 | 27% | 20% | 53% | 58 |
| 5 | 30 | 10% | 30% | 60% | 60 |
| 6 | 30 | 13% | 23% | 63% | 63 |
| 7 | 30 | 20% | 37% | 43% | 54 |
| 8 | 30 | 20% | 43% | 37% | 58 |
| 9 | 30 | 23% | 33% | 43% | 62 |
| 10 | 30 | 10% | 37% | 53% | 56 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.3 | 8.2 | 1521 | 1.04 |
| random_1 | 9.4 | 17.4 | 2912 | 1.40 |
| heuristic_1 | 13.6 | 26.0 | 3702 | 2.42 |

## Properties most often held by the winner

- New York Avenue           99.3%  ############################
- Tennessee Avenue          99.0%  ############################
- Connecticut Avenue        98.7%  ############################
- St. Charles Place         98.7%  ############################
- Reading Railroad          98.3%  ############################
- Electric Company          98.3%  ############################
- Water Works               98.3%  ############################
- Virginia Avenue           98.0%  ############################
- B&O Railroad              98.0%  ############################
- Atlantic Avenue           98.0%  ############################
- Oriental Avenue           97.7%  ############################
- St. James Place           97.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.97 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.97 per space
- yellow     0.97 per space
- green      0.96 per space
- darkblue   0.97 per space
