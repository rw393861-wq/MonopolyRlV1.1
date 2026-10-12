# Monopoly self-play report

Run directory: `logs/eval-arena-20261012-222836`
Games logged: 300
Average rounds per game: 64.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 82 | 27.3% |
| random_1 | 64 | 21.3% |
| heuristic_1 | 154 | 51.3% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 20% | 53% | 63 |
| 2 | 30 | 27% | 20% | 53% | 62 |
| 3 | 30 | 33% | 23% | 43% | 65 |
| 4 | 30 | 43% | 23% | 33% | 62 |
| 5 | 30 | 33% | 17% | 50% | 63 |
| 6 | 30 | 10% | 27% | 63% | 65 |
| 7 | 30 | 10% | 20% | 70% | 65 |
| 8 | 30 | 20% | 27% | 53% | 65 |
| 9 | 30 | 30% | 20% | 50% | 67 |
| 10 | 30 | 40% | 17% | 43% | 64 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 7.3 | 10.7 | 2271 | 1.02 |
| random_1 | 5.9 | 13.1 | 2278 | 1.32 |
| heuristic_1 | 14.2 | 28.4 | 4145 | 2.58 |

## Properties most often held by the winner

- Connecticut Avenue        99.0%  ############################
- B&O Railroad              99.0%  ############################
- St. Charles Place         98.7%  ############################
- Virginia Avenue           98.7%  ############################
- Ventnor Avenue            98.7%  ############################
- Oriental Avenue           98.3%  ############################
- New York Avenue           98.3%  ############################
- Water Works               98.3%  ############################
- Reading Railroad          98.0%  ############################
- Vermont Avenue            98.0%  ############################
- St. James Place           98.0%  ############################
- Tennessee Avenue          98.0%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
