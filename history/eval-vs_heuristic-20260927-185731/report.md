# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260927-185731`
Games logged: 300
Average rounds per game: 104.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 39 | 13.0% |
| heuristic_1 | 137 | 45.7% |
| heuristic_2 | 124 | 41.3% |

## End condition

- last_standing: 231 (77.0%)
- round_limit: 69 (23.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 57% | 27% | 97 |
| 2 | 30 | 20% | 40% | 40% | 91 |
| 3 | 30 | 0% | 37% | 63% | 116 |
| 4 | 30 | 23% | 47% | 30% | 102 |
| 5 | 30 | 10% | 47% | 43% | 93 |
| 6 | 30 | 10% | 37% | 53% | 104 |
| 7 | 30 | 7% | 60% | 33% | 107 |
| 8 | 30 | 7% | 70% | 23% | 122 |
| 9 | 30 | 13% | 30% | 57% | 106 |
| 10 | 30 | 23% | 33% | 43% | 106 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.6 | 4.4 | 1647 | 0.16 |
| heuristic_1 | 11.7 | 16.4 | 4584 | 0.91 |
| heuristic_2 | 11.4 | 16.4 | 4444 | 0.85 |

## Properties most often held by the winner

- Baltic Avenue             91.3%  ############################
- Mediterranean Avenue      91.0%  ############################
- Pennsylvania Railroad     91.0%  ############################
- Reading Railroad          88.7%  ###########################-
- St. Charles Place         88.7%  ###########################-
- B&O Railroad              88.7%  ###########################-
- Marvin Gardens            88.3%  ###########################-
- Short Line                87.7%  ###########################-
- Virginia Avenue           87.0%  ###########################-
- Oriental Avenue           86.7%  ###########################-
- Water Works               86.7%  ###########################-
- New York Avenue           86.3%  ##########################--

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.89 per space
- lightblue  0.85 per space
- pink       0.87 per space
- util       0.86 per space
- orange     0.86 per space
- red        0.85 per space
- yellow     0.86 per space
- green      0.84 per space
- darkblue   0.83 per space
