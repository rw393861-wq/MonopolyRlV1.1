# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260923-185013`
Games logged: 300
Average rounds per game: 113.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 16 | 5.3% |
| heuristic_1 | 130 | 43.3% |
| heuristic_2 | 154 | 51.3% |

## End condition

- round_limit: 82 (27.3%)
- last_standing: 218 (72.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 53% | 40% | 102 |
| 2 | 30 | 7% | 30% | 63% | 128 |
| 3 | 30 | 3% | 50% | 47% | 112 |
| 4 | 30 | 3% | 30% | 67% | 130 |
| 5 | 30 | 7% | 47% | 47% | 116 |
| 6 | 30 | 3% | 60% | 37% | 118 |
| 7 | 30 | 7% | 37% | 57% | 92 |
| 8 | 30 | 3% | 43% | 53% | 113 |
| 9 | 30 | 0% | 40% | 60% | 110 |
| 10 | 30 | 13% | 43% | 43% | 112 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.4 | 1.3 | 1256 | 0.02 |
| heuristic_1 | 11.5 | 14.6 | 4530 | 0.68 |
| heuristic_2 | 13.8 | 16.5 | 4785 | 0.81 |

## Properties most often held by the winner

- Reading Railroad          86.7%  ############################
- Water Works               86.7%  ############################
- Electric Company          85.3%  ############################
- Pennsylvania Railroad     85.0%  ###########################-
- Short Line                84.7%  ###########################-
- Virginia Avenue           84.7%  ###########################-
- States Avenue             84.7%  ###########################-
- Baltic Avenue             84.3%  ###########################-
- Mediterranean Avenue      84.3%  ###########################-
- Tennessee Avenue          84.3%  ###########################-
- Boardwalk                 84.0%  ###########################-
- St. Charles Place         84.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.84 per space
- rail       0.85 per space
- lightblue  0.82 per space
- pink       0.84 per space
- util       0.86 per space
- orange     0.82 per space
- red        0.82 per space
- yellow     0.81 per space
- green      0.82 per space
- darkblue   0.82 per space
