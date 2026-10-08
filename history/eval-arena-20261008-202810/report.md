# Monopoly self-play report

Run directory: `logs/eval-arena-20261008-202810`
Games logged: 300
Average rounds per game: 61.9

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 47 | 15.7% |
| random_1 | 103 | 34.3% |
| heuristic_1 | 150 | 50.0% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 27% | 60% | 62 |
| 2 | 30 | 23% | 43% | 33% | 62 |
| 3 | 30 | 20% | 50% | 30% | 64 |
| 4 | 30 | 13% | 27% | 60% | 62 |
| 5 | 30 | 10% | 23% | 67% | 62 |
| 6 | 30 | 7% | 37% | 57% | 67 |
| 7 | 30 | 17% | 40% | 43% | 60 |
| 8 | 30 | 27% | 30% | 43% | 63 |
| 9 | 30 | 17% | 20% | 63% | 58 |
| 10 | 30 | 10% | 47% | 43% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.3 | 6.8 | 1484 | 0.73 |
| random_1 | 9.4 | 17.7 | 3100 | 1.59 |
| heuristic_1 | 13.7 | 27.3 | 4043 | 2.86 |

## Properties most often held by the winner

- Illinois Avenue           99.3%  ############################
- Electric Company          99.0%  ############################
- St. James Place           99.0%  ############################
- Kentucky Avenue           99.0%  ############################
- Ventnor Avenue            99.0%  ############################
- Marvin Gardens            99.0%  ############################
- Reading Railroad          98.7%  ############################
- St. Charles Place         98.7%  ############################
- Virginia Avenue           98.7%  ############################
- Tennessee Avenue          98.7%  ############################
- New York Avenue           98.7%  ############################
- Vermont Avenue            98.3%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.97 per space
