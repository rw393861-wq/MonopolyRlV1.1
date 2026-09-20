# Monopoly self-play report

Run directory: `logs/eval-arena-20260920-233129`
Games logged: 300
Average rounds per game: 61.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 45 | 15.0% |
| random_1 | 87 | 29.0% |
| heuristic_1 | 168 | 56.0% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 23% | 20% | 57% | 60 |
| 2 | 30 | 13% | 23% | 63% | 64 |
| 3 | 30 | 20% | 27% | 53% | 63 |
| 4 | 30 | 13% | 20% | 67% | 64 |
| 5 | 30 | 7% | 47% | 47% | 60 |
| 6 | 30 | 7% | 43% | 50% | 68 |
| 7 | 30 | 10% | 37% | 53% | 61 |
| 8 | 30 | 20% | 23% | 57% | 57 |
| 9 | 30 | 20% | 23% | 57% | 58 |
| 10 | 30 | 17% | 27% | 57% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.1 | 6.3 | 1458 | 0.51 |
| random_1 | 8.0 | 16.2 | 2732 | 1.49 |
| heuristic_1 | 15.3 | 29.4 | 4192 | 2.77 |

## Properties most often held by the winner

- Reading Railroad          99.3%  ############################
- Connecticut Avenue        98.7%  ############################
- St. James Place           98.7%  ############################
- Illinois Avenue           98.7%  ############################
- Marvin Gardens            98.7%  ############################
- St. Charles Place         98.3%  ############################
- Electric Company          98.3%  ############################
- Pacific Avenue            98.3%  ############################
- Boardwalk                 98.3%  ############################
- Vermont Avenue            98.0%  ############################
- New York Avenue           98.0%  ############################
- Kentucky Avenue           98.0%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.97 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
