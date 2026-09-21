# Monopoly self-play report

Run directory: `logs/eval-arena-20260921-200023`
Games logged: 300
Average rounds per game: 65.0

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 57 | 19.0% |
| random_1 | 84 | 28.0% |
| heuristic_1 | 159 | 53.0% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 23% | 20% | 57% | 69 |
| 2 | 30 | 10% | 23% | 67% | 66 |
| 3 | 30 | 20% | 47% | 33% | 62 |
| 4 | 30 | 20% | 33% | 47% | 63 |
| 5 | 30 | 13% | 40% | 47% | 65 |
| 6 | 30 | 23% | 20% | 57% | 71 |
| 7 | 30 | 13% | 23% | 63% | 69 |
| 8 | 30 | 23% | 20% | 57% | 64 |
| 9 | 30 | 23% | 33% | 43% | 66 |
| 10 | 30 | 20% | 20% | 60% | 56 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.1 | 7.4 | 1648 | 0.93 |
| random_1 | 7.7 | 15.8 | 2973 | 1.50 |
| heuristic_1 | 14.6 | 28.3 | 4227 | 2.54 |

## Properties most often held by the winner

- Vermont Avenue            99.0%  ############################
- Connecticut Avenue        98.7%  ############################
- St. Charles Place         98.7%  ############################
- St. James Place           98.7%  ############################
- New York Avenue           98.3%  ############################
- Water Works               98.3%  ############################
- Park Place                98.3%  ############################
- Pennsylvania Railroad     98.0%  ############################
- Atlantic Avenue           98.0%  ############################
- Ventnor Avenue            98.0%  ############################
- Marvin Gardens            98.0%  ############################
- Reading Railroad          97.7%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.97 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.97 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.98 per space
