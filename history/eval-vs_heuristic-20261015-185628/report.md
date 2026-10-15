# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261015-185628`
Games logged: 300
Average rounds per game: 109.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 23 | 7.7% |
| heuristic_1 | 141 | 47.0% |
| heuristic_2 | 136 | 45.3% |

## End condition

- last_standing: 224 (74.7%)
- round_limit: 76 (25.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 50% | 40% | 109 |
| 2 | 30 | 10% | 50% | 40% | 115 |
| 3 | 30 | 7% | 43% | 50% | 100 |
| 4 | 30 | 3% | 50% | 47% | 104 |
| 5 | 30 | 7% | 57% | 37% | 127 |
| 6 | 30 | 13% | 43% | 43% | 116 |
| 7 | 30 | 10% | 50% | 40% | 102 |
| 8 | 30 | 3% | 47% | 50% | 121 |
| 9 | 30 | 13% | 27% | 60% | 89 |
| 10 | 30 | 0% | 53% | 47% | 113 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.6 | 1.8 | 1166 | 0.13 |
| heuristic_1 | 12.6 | 16.7 | 4784 | 0.89 |
| heuristic_2 | 12.7 | 17.4 | 4718 | 0.93 |

## Properties most often held by the winner

- Mediterranean Avenue      90.0%  ############################
- Baltic Avenue             90.0%  ############################
- Reading Railroad          88.0%  ###########################-
- Kentucky Avenue           87.3%  ###########################-
- Pacific Avenue            86.3%  ###########################-
- B&O Railroad              85.7%  ###########################-
- Virginia Avenue           85.3%  ###########################-
- Tennessee Avenue          85.3%  ###########################-
- Water Works               85.3%  ###########################-
- Short Line                85.3%  ###########################-
- St. James Place           85.0%  ##########################--
- States Avenue             84.3%  ##########################--

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.86 per space
- lightblue  0.82 per space
- pink       0.84 per space
- util       0.84 per space
- orange     0.85 per space
- red        0.85 per space
- yellow     0.84 per space
- green      0.85 per space
- darkblue   0.83 per space
