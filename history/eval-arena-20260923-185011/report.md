# Monopoly self-play report

Run directory: `logs/eval-arena-20260923-185011`
Games logged: 300
Average rounds per game: 62.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 39 | 13.0% |
| random_1 | 90 | 30.0% |
| heuristic_1 | 171 | 57.0% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 30% | 57% | 62 |
| 2 | 30 | 23% | 23% | 53% | 62 |
| 3 | 30 | 13% | 63% | 23% | 62 |
| 4 | 30 | 10% | 17% | 73% | 69 |
| 5 | 30 | 10% | 20% | 70% | 63 |
| 6 | 30 | 10% | 23% | 67% | 69 |
| 7 | 30 | 13% | 20% | 67% | 58 |
| 8 | 30 | 3% | 43% | 53% | 66 |
| 9 | 30 | 7% | 33% | 60% | 58 |
| 10 | 30 | 27% | 27% | 47% | 54 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.5 | 5.3 | 1253 | 0.60 |
| random_1 | 8.2 | 16.2 | 2960 | 1.60 |
| heuristic_1 | 15.7 | 28.7 | 4226 | 2.51 |

## Properties most often held by the winner

- Illinois Avenue           99.3%  ############################
- Electric Company          98.7%  ############################
- Pennsylvania Railroad     98.7%  ############################
- Reading Railroad          98.3%  ############################
- Connecticut Avenue        98.3%  ############################
- St. Charles Place         98.3%  ############################
- St. James Place           98.3%  ############################
- Tennessee Avenue          98.3%  ############################
- Ventnor Avenue            98.3%  ############################
- Water Works               98.3%  ############################
- Pacific Avenue            98.3%  ############################
- Boardwalk                 98.3%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.98 per space
