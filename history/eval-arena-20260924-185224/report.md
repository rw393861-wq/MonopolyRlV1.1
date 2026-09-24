# Monopoly self-play report

Run directory: `logs/eval-arena-20260924-185224`
Games logged: 300
Average rounds per game: 63.8

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 40 | 13.3% |
| random_1 | 91 | 30.3% |
| heuristic_1 | 169 | 56.3% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 37% | 47% | 73 |
| 2 | 30 | 20% | 17% | 63% | 59 |
| 3 | 30 | 13% | 27% | 60% | 60 |
| 4 | 30 | 13% | 40% | 47% | 65 |
| 5 | 30 | 7% | 40% | 53% | 62 |
| 6 | 30 | 10% | 33% | 57% | 63 |
| 7 | 30 | 17% | 13% | 70% | 65 |
| 8 | 30 | 10% | 33% | 57% | 63 |
| 9 | 30 | 7% | 33% | 60% | 65 |
| 10 | 30 | 20% | 30% | 50% | 63 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.6 | 7.8 | 1425 | 0.95 |
| random_1 | 8.4 | 16.9 | 2958 | 1.60 |
| heuristic_1 | 15.6 | 28.4 | 4432 | 2.61 |

## Properties most often held by the winner

- Virginia Avenue           99.7%  ############################
- New York Avenue           99.7%  ############################
- Ventnor Avenue            99.7%  ############################
- Reading Railroad          99.3%  ############################
- St. Charles Place         99.3%  ############################
- States Avenue             99.3%  ############################
- Tennessee Avenue          99.3%  ############################
- Illinois Avenue           99.0%  ############################
- Electric Company          98.7%  ############################
- Pennsylvania Railroad     98.7%  ############################
- St. James Place           98.3%  ############################
- North Carolina Avenue     98.3%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.99 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
