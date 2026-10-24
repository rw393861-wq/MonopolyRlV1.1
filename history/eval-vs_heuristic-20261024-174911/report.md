# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261024-174911`
Games logged: 300
Average rounds per game: 113.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 29 | 9.7% |
| heuristic_1 | 121 | 40.3% |
| heuristic_2 | 150 | 50.0% |

## End condition

- last_standing: 220 (73.3%)
- round_limit: 80 (26.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 40% | 43% | 100 |
| 2 | 30 | 30% | 20% | 50% | 131 |
| 3 | 30 | 17% | 33% | 50% | 120 |
| 4 | 30 | 10% | 47% | 43% | 109 |
| 5 | 30 | 3% | 50% | 47% | 123 |
| 6 | 30 | 0% | 47% | 53% | 102 |
| 7 | 30 | 7% | 30% | 63% | 103 |
| 8 | 30 | 3% | 50% | 47% | 120 |
| 9 | 30 | 3% | 37% | 60% | 104 |
| 10 | 30 | 7% | 50% | 43% | 121 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.0 | 2.2 | 1563 | 0.08 |
| heuristic_1 | 11.3 | 15.0 | 4532 | 0.59 |
| heuristic_2 | 13.3 | 18.4 | 5210 | 0.78 |

## Properties most often held by the winner

- Mediterranean Avenue      89.7%  ############################
- Baltic Avenue             87.0%  ###########################-
- North Carolina Avenue     86.0%  ###########################-
- Pennsylvania Railroad     85.7%  ###########################-
- B&O Railroad              85.7%  ###########################-
- Short Line                85.0%  ###########################-
- Virginia Avenue           84.7%  ##########################--
- Illinois Avenue           83.7%  ##########################--
- St. Charles Place         82.7%  ##########################--
- Kentucky Avenue           82.3%  ##########################--
- Water Works               82.3%  ##########################--
- Oriental Avenue           82.0%  ##########################--

## Colour group pull rate (winner)

- brown      0.88 per space
- rail       0.84 per space
- lightblue  0.81 per space
- pink       0.83 per space
- util       0.82 per space
- orange     0.81 per space
- red        0.82 per space
- yellow     0.81 per space
- green      0.82 per space
- darkblue   0.81 per space
