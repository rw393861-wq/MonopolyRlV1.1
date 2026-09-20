# Monopoly self-play report

Run directory: `logs/eval-arena-20260920-225207`
Games logged: 300
Average rounds per game: 64.0

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 84 | 28.0% |
| random_1 | 77 | 25.7% |
| heuristic_1 | 139 | 46.3% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 30% | 57% | 66 |
| 2 | 30 | 33% | 20% | 47% | 61 |
| 3 | 30 | 30% | 23% | 47% | 62 |
| 4 | 30 | 27% | 30% | 43% | 62 |
| 5 | 30 | 30% | 17% | 53% | 64 |
| 6 | 30 | 27% | 30% | 43% | 62 |
| 7 | 30 | 37% | 23% | 40% | 57 |
| 8 | 30 | 20% | 23% | 57% | 67 |
| 9 | 30 | 33% | 30% | 37% | 66 |
| 10 | 30 | 30% | 30% | 40% | 74 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 7.5 | 10.8 | 2431 | 0.89 |
| random_1 | 7.1 | 13.4 | 2404 | 1.28 |
| heuristic_1 | 12.8 | 24.2 | 3823 | 2.63 |

## Properties most often held by the winner

- B&O Railroad             100.0%  ############################
- Illinois Avenue           99.0%  ############################
- St. Charles Place         98.7%  ############################
- Tennessee Avenue          98.3%  ############################
- New York Avenue           98.3%  ############################
- Mediterranean Avenue      98.0%  ###########################-
- Pennsylvania Railroad     98.0%  ###########################-
- Atlantic Avenue           98.0%  ###########################-
- Ventnor Avenue            98.0%  ###########################-
- Boardwalk                 98.0%  ###########################-
- Vermont Avenue            97.7%  ###########################-
- Connecticut Avenue        97.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.97 per space
- util       0.96 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.98 per space
