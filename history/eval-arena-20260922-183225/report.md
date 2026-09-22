# Monopoly self-play report

Run directory: `logs/eval-arena-20260922-183225`
Games logged: 300
Average rounds per game: 57.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 75 | 25.0% |
| random_1 | 75 | 25.0% |
| heuristic_1 | 150 | 50.0% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 23% | 50% | 60 |
| 2 | 30 | 33% | 33% | 33% | 58 |
| 3 | 30 | 10% | 47% | 43% | 61 |
| 4 | 30 | 37% | 7% | 57% | 55 |
| 5 | 30 | 17% | 33% | 50% | 59 |
| 6 | 30 | 20% | 17% | 63% | 52 |
| 7 | 30 | 17% | 33% | 50% | 59 |
| 8 | 30 | 20% | 13% | 67% | 60 |
| 9 | 30 | 27% | 23% | 50% | 55 |
| 10 | 30 | 43% | 20% | 37% | 53 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.9 | 10.3 | 1858 | 0.88 |
| random_1 | 6.8 | 12.9 | 2338 | 1.31 |
| heuristic_1 | 13.7 | 26.1 | 3729 | 2.57 |

## Properties most often held by the winner

- Illinois Avenue           99.7%  ############################
- St. Charles Place         99.3%  ############################
- Pennsylvania Railroad     99.0%  ############################
- Tennessee Avenue          99.0%  ############################
- Water Works               99.0%  ############################
- Reading Railroad          98.7%  ############################
- Vermont Avenue            98.7%  ############################
- Kentucky Avenue           98.7%  ############################
- Boardwalk                 98.7%  ############################
- Oriental Avenue           98.3%  ############################
- St. James Place           98.3%  ############################
- New York Avenue           98.3%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.97 per space
