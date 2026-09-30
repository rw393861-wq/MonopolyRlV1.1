# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260930-195546`
Games logged: 300
Average rounds per game: 93.0

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 30 | 10.0% |
| heuristic_1 | 132 | 44.0% |
| heuristic_2 | 138 | 46.0% |

## End condition

- last_standing: 257 (85.7%)
- round_limit: 43 (14.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 47% | 47% | 90 |
| 2 | 30 | 17% | 37% | 47% | 104 |
| 3 | 30 | 17% | 50% | 33% | 80 |
| 4 | 30 | 17% | 40% | 43% | 79 |
| 5 | 30 | 10% | 43% | 47% | 94 |
| 6 | 30 | 3% | 47% | 50% | 110 |
| 7 | 30 | 7% | 50% | 43% | 83 |
| 8 | 30 | 10% | 37% | 53% | 98 |
| 9 | 30 | 10% | 43% | 47% | 93 |
| 10 | 30 | 3% | 47% | 50% | 99 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.5 | 5.1 | 1512 | 0.33 |
| heuristic_1 | 12.0 | 18.4 | 4450 | 1.10 |
| heuristic_2 | 12.2 | 17.6 | 4320 | 1.12 |

## Properties most often held by the winner

- Electric Company          93.3%  ############################
- Tennessee Avenue          93.3%  ############################
- B&O Railroad              93.0%  ############################
- Water Works               92.7%  ############################
- Baltic Avenue             92.3%  ############################
- St. Charles Place         92.3%  ############################
- Pennsylvania Railroad     92.0%  ############################
- St. James Place           91.7%  ############################
- Mediterranean Avenue      91.3%  ###########################-
- Reading Railroad          91.0%  ###########################-
- Kentucky Avenue           91.0%  ###########################-
- North Carolina Avenue     91.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.92 per space
- rail       0.91 per space
- lightblue  0.90 per space
- pink       0.90 per space
- util       0.93 per space
- orange     0.92 per space
- red        0.90 per space
- yellow     0.90 per space
- green      0.90 per space
- darkblue   0.90 per space
