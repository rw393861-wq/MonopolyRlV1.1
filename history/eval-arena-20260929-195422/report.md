# Monopoly self-play report

Run directory: `logs/eval-arena-20260929-195422`
Games logged: 300
Average rounds per game: 63.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 61 | 20.3% |
| random_1 | 83 | 27.7% |
| heuristic_1 | 156 | 52.0% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 30% | 50% | 65 |
| 2 | 30 | 23% | 23% | 53% | 63 |
| 3 | 30 | 30% | 23% | 47% | 69 |
| 4 | 30 | 23% | 23% | 53% | 60 |
| 5 | 30 | 10% | 43% | 47% | 71 |
| 6 | 30 | 23% | 33% | 43% | 61 |
| 7 | 30 | 17% | 20% | 63% | 58 |
| 8 | 30 | 20% | 30% | 50% | 64 |
| 9 | 30 | 17% | 33% | 50% | 62 |
| 10 | 30 | 20% | 17% | 63% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.5 | 7.2 | 1804 | 0.57 |
| random_1 | 7.6 | 14.9 | 2592 | 1.44 |
| heuristic_1 | 14.3 | 27.5 | 4120 | 2.81 |

## Properties most often held by the winner

- Indiana Avenue            99.0%  ############################
- Illinois Avenue           99.0%  ############################
- Pennsylvania Railroad     98.7%  ############################
- Reading Railroad          98.3%  ############################
- Vermont Avenue            98.3%  ############################
- Electric Company          98.3%  ############################
- St. James Place           98.3%  ############################
- Kentucky Avenue           98.3%  ############################
- Connecticut Avenue        98.0%  ############################
- St. Charles Place         98.0%  ############################
- Virginia Avenue           98.0%  ############################
- Tennessee Avenue          98.0%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.97 per space
- orange     0.98 per space
- red        0.99 per space
- yellow     0.97 per space
- green      0.96 per space
- darkblue   0.98 per space
