# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261006-200559`
Games logged: 300
Average rounds per game: 102.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 5 | 1.7% |
| heuristic_1 | 151 | 50.3% |
| heuristic_2 | 144 | 48.0% |

## End condition

- round_limit: 60 (20.0%)
- last_standing: 240 (80.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 53% | 43% | 109 |
| 2 | 30 | 0% | 53% | 47% | 98 |
| 3 | 30 | 0% | 50% | 50% | 113 |
| 4 | 30 | 7% | 53% | 40% | 108 |
| 5 | 30 | 0% | 53% | 47% | 94 |
| 6 | 30 | 3% | 43% | 53% | 93 |
| 7 | 30 | 0% | 50% | 50% | 96 |
| 8 | 30 | 0% | 60% | 40% | 108 |
| 9 | 30 | 3% | 47% | 50% | 106 |
| 10 | 30 | 0% | 40% | 60% | 98 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 1.4 | 0.5 | 727 | 0.00 |
| heuristic_1 | 13.4 | 17.5 | 4822 | 0.98 |
| heuristic_2 | 12.9 | 17.2 | 4794 | 1.00 |

## Properties most often held by the winner

- Baltic Avenue             91.7%  ############################
- Mediterranean Avenue      91.3%  ############################
- B&O Railroad              90.7%  ############################
- Short Line                89.0%  ###########################-
- North Carolina Avenue     89.0%  ###########################-
- Electric Company          88.7%  ###########################-
- Pennsylvania Railroad     88.3%  ###########################-
- Illinois Avenue           88.3%  ###########################-
- Pennsylvania Avenue       88.3%  ###########################-
- Tennessee Avenue          88.0%  ###########################-
- Kentucky Avenue           88.0%  ###########################-
- Marvin Gardens            88.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.92 per space
- rail       0.89 per space
- lightblue  0.85 per space
- pink       0.86 per space
- util       0.88 per space
- orange     0.88 per space
- red        0.87 per space
- yellow     0.87 per space
- green      0.88 per space
- darkblue   0.85 per space
