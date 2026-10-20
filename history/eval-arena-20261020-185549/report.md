# Monopoly self-play report

Run directory: `logs/eval-arena-20261020-185549`
Games logged: 300
Average rounds per game: 63.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 45 | 15.0% |
| random_1 | 69 | 23.0% |
| heuristic_1 | 186 | 62.0% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 30% | 13% | 57% | 62 |
| 2 | 30 | 10% | 17% | 73% | 60 |
| 3 | 30 | 10% | 23% | 67% | 70 |
| 4 | 30 | 13% | 23% | 63% | 66 |
| 5 | 30 | 13% | 27% | 60% | 61 |
| 6 | 30 | 17% | 23% | 60% | 62 |
| 7 | 30 | 27% | 27% | 47% | 58 |
| 8 | 30 | 17% | 20% | 63% | 60 |
| 9 | 30 | 7% | 23% | 70% | 70 |
| 10 | 30 | 7% | 33% | 60% | 66 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.1 | 5.9 | 1434 | 0.63 |
| random_1 | 6.3 | 14.3 | 2619 | 1.33 |
| heuristic_1 | 17.1 | 31.1 | 4873 | 2.82 |

## Properties most often held by the winner

- Pennsylvania Railroad     99.7%  ############################
- Boardwalk                 99.7%  ############################
- Reading Railroad          99.3%  ############################
- Virginia Avenue           99.3%  ############################
- Tennessee Avenue          99.3%  ############################
- Vermont Avenue            99.0%  ############################
- Connecticut Avenue        99.0%  ############################
- St. James Place           99.0%  ############################
- B&O Railroad              99.0%  ############################
- St. Charles Place         98.7%  ############################
- Illinois Avenue           98.7%  ############################
- Short Line                98.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.99 per space
- lightblue  0.99 per space
- pink       0.99 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.98 per space
