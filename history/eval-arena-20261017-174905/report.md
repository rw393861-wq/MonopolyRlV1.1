# Monopoly self-play report

Run directory: `logs/eval-arena-20261017-174905`
Games logged: 300
Average rounds per game: 60.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 36 | 12.0% |
| random_1 | 74 | 24.7% |
| heuristic_1 | 190 | 63.3% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 23% | 63% | 65 |
| 2 | 30 | 13% | 40% | 47% | 55 |
| 3 | 30 | 10% | 17% | 73% | 53 |
| 4 | 30 | 17% | 30% | 53% | 67 |
| 5 | 30 | 20% | 27% | 53% | 60 |
| 6 | 30 | 13% | 33% | 53% | 64 |
| 7 | 30 | 10% | 27% | 63% | 55 |
| 8 | 30 | 3% | 13% | 83% | 68 |
| 9 | 30 | 17% | 23% | 60% | 57 |
| 10 | 30 | 3% | 13% | 83% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.3 | 4.4 | 1097 | 0.33 |
| random_1 | 6.8 | 15.1 | 2630 | 1.54 |
| heuristic_1 | 17.4 | 33.3 | 4742 | 2.65 |

## Properties most often held by the winner

- St. Charles Place         99.3%  ############################
- Pennsylvania Railroad     99.3%  ############################
- St. James Place           99.3%  ############################
- New York Avenue           99.3%  ############################
- Kentucky Avenue           99.3%  ############################
- Short Line                99.3%  ############################
- Reading Railroad          99.0%  ############################
- Electric Company          99.0%  ############################
- Tennessee Avenue          99.0%  ############################
- Indiana Avenue            99.0%  ############################
- Vermont Avenue            98.7%  ############################
- States Avenue             98.7%  ############################

## Colour group pull rate (winner)

- brown      0.98 per space
- rail       0.99 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
