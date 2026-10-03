# Monopoly self-play report

Run directory: `logs/eval-arena-20261003-183233`
Games logged: 300
Average rounds per game: 63.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 74 | 24.7% |
| random_1 | 91 | 30.3% |
| heuristic_1 | 135 | 45.0% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 43% | 37% | 67 |
| 2 | 30 | 17% | 27% | 57% | 62 |
| 3 | 30 | 33% | 30% | 37% | 66 |
| 4 | 30 | 33% | 20% | 47% | 65 |
| 5 | 30 | 23% | 47% | 30% | 60 |
| 6 | 30 | 17% | 37% | 47% | 60 |
| 7 | 30 | 27% | 23% | 50% | 65 |
| 8 | 30 | 27% | 23% | 50% | 67 |
| 9 | 30 | 23% | 20% | 57% | 60 |
| 10 | 30 | 27% | 33% | 40% | 64 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.9 | 9.5 | 2171 | 0.82 |
| random_1 | 8.4 | 17.3 | 2690 | 1.61 |
| heuristic_1 | 12.2 | 25.1 | 3680 | 2.43 |

## Properties most often held by the winner

- Baltic Avenue             99.3%  ############################
- Tennessee Avenue          99.0%  ############################
- Mediterranean Avenue      98.7%  ############################
- Reading Railroad          98.7%  ############################
- Vermont Avenue            98.7%  ############################
- Pennsylvania Railroad     98.7%  ############################
- Kentucky Avenue           98.7%  ############################
- Water Works               98.7%  ############################
- Pacific Avenue            98.7%  ############################
- Pennsylvania Avenue       98.7%  ############################
- Oriental Avenue           98.3%  ############################
- St. Charles Place         98.3%  ############################

## Colour group pull rate (winner)

- brown      0.99 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.98 per space
- darkblue   0.97 per space
