# Monopoly self-play report

Run directory: `logs/eval-arena-20261006-200556`
Games logged: 300
Average rounds per game: 63.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 11 | 3.7% |
| random_1 | 88 | 29.3% |
| heuristic_1 | 201 | 67.0% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 30% | 63% | 65 |
| 2 | 30 | 3% | 37% | 60% | 54 |
| 3 | 30 | 3% | 40% | 57% | 65 |
| 4 | 30 | 3% | 17% | 80% | 63 |
| 5 | 30 | 3% | 23% | 73% | 60 |
| 6 | 30 | 7% | 27% | 67% | 72 |
| 7 | 30 | 0% | 40% | 60% | 67 |
| 8 | 30 | 3% | 27% | 70% | 61 |
| 9 | 30 | 7% | 20% | 73% | 67 |
| 10 | 30 | 0% | 33% | 67% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 1.1 | 2.2 | 769 | 0.52 |
| random_1 | 8.2 | 16.0 | 2923 | 1.48 |
| heuristic_1 | 18.3 | 33.0 | 5112 | 2.89 |

## Properties most often held by the winner

- Electric Company         100.0%  ############################
- St. James Place          100.0%  ############################
- New York Avenue           99.3%  ############################
- Pennsylvania Railroad     99.0%  ############################
- Tennessee Avenue          99.0%  ############################
- B&O Railroad              99.0%  ############################
- Reading Railroad          98.7%  ############################
- Indiana Avenue            98.7%  ############################
- Baltic Avenue             98.3%  ############################
- Vermont Avenue            98.3%  ############################
- Connecticut Avenue        98.3%  ############################
- Water Works               98.3%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.98 per space
- darkblue   0.98 per space
