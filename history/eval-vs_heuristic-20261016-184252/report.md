# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261016-184252`
Games logged: 300
Average rounds per game: 102.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 25 | 8.3% |
| heuristic_1 | 140 | 46.7% |
| heuristic_2 | 135 | 45.0% |

## End condition

- round_limit: 59 (19.7%)
- last_standing: 241 (80.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 57% | 30% | 105 |
| 2 | 30 | 17% | 43% | 40% | 105 |
| 3 | 30 | 10% | 53% | 37% | 108 |
| 4 | 30 | 10% | 50% | 40% | 102 |
| 5 | 30 | 13% | 40% | 47% | 107 |
| 6 | 30 | 3% | 53% | 43% | 109 |
| 7 | 30 | 3% | 37% | 60% | 94 |
| 8 | 30 | 0% | 50% | 50% | 99 |
| 9 | 30 | 10% | 43% | 47% | 98 |
| 10 | 30 | 3% | 40% | 57% | 100 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.1 | 2.5 | 1050 | 0.24 |
| heuristic_1 | 12.3 | 18.3 | 4747 | 1.04 |
| heuristic_2 | 12.3 | 17.8 | 4614 | 1.05 |

## Properties most often held by the winner

- Short Line                91.3%  ############################
- Mediterranean Avenue      91.0%  ############################
- Baltic Avenue             90.7%  ############################
- Water Works               90.3%  ############################
- Pennsylvania Railroad     90.0%  ############################
- B&O Railroad              90.0%  ############################
- Illinois Avenue           89.3%  ###########################-
- North Carolina Avenue     89.0%  ###########################-
- Kentucky Avenue           88.7%  ###########################-
- Reading Railroad          88.0%  ###########################-
- Vermont Avenue            87.7%  ###########################-
- Marvin Gardens            87.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.90 per space
- lightblue  0.86 per space
- pink       0.86 per space
- util       0.89 per space
- orange     0.86 per space
- red        0.88 per space
- yellow     0.86 per space
- green      0.88 per space
- darkblue   0.87 per space
