# Monopoly self-play report

Run directory: `logs/eval-arena-20261015-185625`
Games logged: 300
Average rounds per game: 62.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 56 | 18.7% |
| random_1 | 93 | 31.0% |
| heuristic_1 | 151 | 50.3% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 33% | 47% | 62 |
| 2 | 30 | 10% | 27% | 63% | 60 |
| 3 | 30 | 17% | 23% | 60% | 65 |
| 4 | 30 | 17% | 40% | 43% | 67 |
| 5 | 30 | 23% | 30% | 47% | 66 |
| 6 | 30 | 17% | 43% | 40% | 63 |
| 7 | 30 | 27% | 37% | 37% | 68 |
| 8 | 30 | 23% | 37% | 40% | 59 |
| 9 | 30 | 20% | 13% | 67% | 52 |
| 10 | 30 | 13% | 27% | 60% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.1 | 7.5 | 1635 | 0.68 |
| random_1 | 8.5 | 17.5 | 2991 | 1.68 |
| heuristic_1 | 13.9 | 28.2 | 4167 | 2.54 |

## Properties most often held by the winner

- Reading Railroad          99.3%  ############################
- Virginia Avenue           99.3%  ############################
- Indiana Avenue            99.3%  ############################
- St. Charles Place         99.0%  ############################
- St. James Place           99.0%  ############################
- Tennessee Avenue          99.0%  ############################
- New York Avenue           99.0%  ############################
- Illinois Avenue           98.7%  ############################
- Water Works               98.7%  ############################
- Mediterranean Avenue      98.3%  ############################
- Connecticut Avenue        98.3%  ############################
- Electric Company          98.3%  ############################

## Colour group pull rate (winner)

- brown      0.98 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
