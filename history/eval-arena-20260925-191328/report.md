# Monopoly self-play report

Run directory: `logs/eval-arena-20260925-191328`
Games logged: 300
Average rounds per game: 59.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 49 | 16.3% |
| random_1 | 79 | 26.3% |
| heuristic_1 | 172 | 57.3% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 17% | 63% | 58 |
| 2 | 30 | 20% | 23% | 57% | 57 |
| 3 | 30 | 20% | 33% | 47% | 68 |
| 4 | 30 | 20% | 20% | 60% | 55 |
| 5 | 30 | 10% | 17% | 73% | 58 |
| 6 | 30 | 17% | 27% | 57% | 62 |
| 7 | 30 | 20% | 27% | 53% | 59 |
| 8 | 30 | 7% | 37% | 57% | 60 |
| 9 | 30 | 13% | 30% | 57% | 61 |
| 10 | 30 | 17% | 33% | 50% | 58 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.5 | 7.1 | 1395 | 1.17 |
| random_1 | 7.2 | 15.1 | 2603 | 1.41 |
| heuristic_1 | 15.7 | 28.0 | 4143 | 2.50 |

## Properties most often held by the winner

- Electric Company          99.7%  ############################
- B&O Railroad              99.3%  ############################
- North Carolina Avenue     99.3%  ############################
- St. James Place           99.0%  ############################
- States Avenue             98.7%  ############################
- Tennessee Avenue          98.7%  ############################
- Boardwalk                 98.7%  ############################
- Reading Railroad          98.3%  ############################
- Connecticut Avenue        98.3%  ############################
- Virginia Avenue           98.3%  ############################
- Pennsylvania Railroad     98.3%  ############################
- Illinois Avenue           98.3%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.99 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.97 per space
