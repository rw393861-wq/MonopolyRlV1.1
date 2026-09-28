# Monopoly self-play report

Run directory: `logs/eval-arena-20260928-210730`
Games logged: 300
Average rounds per game: 60.8

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 51 | 17.0% |
| random_1 | 97 | 32.3% |
| heuristic_1 | 152 | 50.7% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 27% | 47% | 51 |
| 2 | 30 | 13% | 50% | 37% | 63 |
| 3 | 30 | 17% | 13% | 70% | 64 |
| 4 | 30 | 13% | 30% | 57% | 60 |
| 5 | 30 | 20% | 37% | 43% | 55 |
| 6 | 30 | 13% | 27% | 60% | 66 |
| 7 | 30 | 23% | 30% | 47% | 63 |
| 8 | 30 | 13% | 40% | 47% | 62 |
| 9 | 30 | 13% | 47% | 40% | 62 |
| 10 | 30 | 17% | 23% | 60% | 64 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.6 | 5.5 | 1481 | 0.68 |
| random_1 | 9.0 | 16.8 | 2868 | 1.48 |
| heuristic_1 | 13.9 | 27.8 | 3887 | 2.57 |

## Properties most often held by the winner

- Vermont Avenue            99.3%  ############################
- Tennessee Avenue          99.3%  ############################
- Illinois Avenue           99.3%  ############################
- Reading Railroad          99.0%  ############################
- New York Avenue           99.0%  ############################
- B&O Railroad              99.0%  ############################
- Oriental Avenue           98.7%  ############################
- St. Charles Place         98.7%  ############################
- Marvin Gardens            98.7%  ############################
- Pacific Avenue            98.7%  ############################
- North Carolina Avenue     98.7%  ############################
- Virginia Avenue           98.3%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.99 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
