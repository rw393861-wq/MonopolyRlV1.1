# Monopoly self-play report

Run directory: `logs/eval-arena-20261019-202735`
Games logged: 300
Average rounds per game: 61.0

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 69 | 23.0% |
| random_1 | 86 | 28.7% |
| heuristic_1 | 145 | 48.3% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 17% | 70% | 65 |
| 2 | 30 | 20% | 50% | 30% | 62 |
| 3 | 30 | 27% | 30% | 43% | 57 |
| 4 | 30 | 37% | 23% | 40% | 61 |
| 5 | 30 | 20% | 27% | 53% | 71 |
| 6 | 30 | 23% | 27% | 50% | 59 |
| 7 | 30 | 20% | 40% | 40% | 62 |
| 8 | 30 | 17% | 33% | 50% | 62 |
| 9 | 30 | 30% | 23% | 47% | 54 |
| 10 | 30 | 23% | 17% | 60% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.1 | 7.4 | 1817 | 0.61 |
| random_1 | 7.8 | 16.7 | 2850 | 1.53 |
| heuristic_1 | 13.4 | 27.1 | 3881 | 2.49 |

## Properties most often held by the winner

- Reading Railroad          99.3%  ############################
- B&O Railroad              99.0%  ############################
- Marvin Gardens            99.0%  ############################
- Illinois Avenue           98.7%  ############################
- Ventnor Avenue            98.7%  ############################
- St. James Place           98.3%  ############################
- Tennessee Avenue          98.3%  ############################
- New York Avenue           98.3%  ############################
- St. Charles Place         98.0%  ############################
- States Avenue             98.0%  ############################
- Pennsylvania Railroad     98.0%  ############################
- Indiana Avenue            98.0%  ############################

## Colour group pull rate (winner)

- brown      0.94 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.97 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.96 per space
- darkblue   0.96 per space
