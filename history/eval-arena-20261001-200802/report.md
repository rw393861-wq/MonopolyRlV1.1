# Monopoly self-play report

Run directory: `logs/eval-arena-20261001-200802`
Games logged: 300
Average rounds per game: 62.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 73 | 24.3% |
| random_1 | 86 | 28.7% |
| heuristic_1 | 141 | 47.0% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 23% | 27% | 50% | 61 |
| 2 | 30 | 27% | 37% | 37% | 64 |
| 3 | 30 | 33% | 10% | 57% | 61 |
| 4 | 30 | 43% | 27% | 30% | 60 |
| 5 | 30 | 17% | 43% | 40% | 66 |
| 6 | 30 | 20% | 33% | 47% | 64 |
| 7 | 30 | 20% | 30% | 50% | 63 |
| 8 | 30 | 10% | 43% | 47% | 67 |
| 9 | 30 | 17% | 20% | 63% | 59 |
| 10 | 30 | 33% | 17% | 50% | 58 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.6 | 8.7 | 1911 | 0.84 |
| random_1 | 7.8 | 15.4 | 2762 | 1.48 |
| heuristic_1 | 13.0 | 25.6 | 3850 | 2.49 |

## Properties most often held by the winner

- Tennessee Avenue          99.0%  ############################
- St. Charles Place         98.7%  ############################
- States Avenue             98.7%  ############################
- Pacific Avenue            98.7%  ############################
- Pennsylvania Railroad     98.3%  ############################
- New York Avenue           98.3%  ############################
- Atlantic Avenue           98.3%  ############################
- Reading Railroad          98.0%  ############################
- St. James Place           98.0%  ############################
- Electric Company          97.7%  ############################
- Kentucky Avenue           97.7%  ############################
- Park Place                97.7%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.97 per space
- orange     0.98 per space
- red        0.97 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
