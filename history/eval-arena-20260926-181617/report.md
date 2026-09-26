# Monopoly self-play report

Run directory: `logs/eval-arena-20260926-181617`
Games logged: 300
Average rounds per game: 63.0

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 63 | 21.0% |
| random_1 | 77 | 25.7% |
| heuristic_1 | 160 | 53.3% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 23% | 50% | 66 |
| 2 | 30 | 27% | 23% | 50% | 61 |
| 3 | 30 | 10% | 40% | 50% | 66 |
| 4 | 30 | 40% | 10% | 50% | 62 |
| 5 | 30 | 13% | 17% | 70% | 56 |
| 6 | 30 | 20% | 23% | 57% | 62 |
| 7 | 30 | 17% | 27% | 57% | 54 |
| 8 | 30 | 10% | 40% | 50% | 73 |
| 9 | 30 | 23% | 23% | 53% | 66 |
| 10 | 30 | 23% | 30% | 47% | 64 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.8 | 8.2 | 1911 | 0.65 |
| random_1 | 7.1 | 13.9 | 2513 | 1.42 |
| heuristic_1 | 14.6 | 28.6 | 4191 | 2.66 |

## Properties most often held by the winner

- St. Charles Place         99.7%  ############################
- New York Avenue           99.3%  ############################
- St. James Place           99.0%  ############################
- B&O Railroad              99.0%  ############################
- Water Works               99.0%  ############################
- Reading Railroad          98.7%  ############################
- Connecticut Avenue        98.7%  ############################
- Tennessee Avenue          98.7%  ############################
- Illinois Avenue           98.7%  ############################
- Vermont Avenue            98.3%  ############################
- Electric Company          98.3%  ############################
- Kentucky Avenue           98.3%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.98 per space
- darkblue   0.97 per space
