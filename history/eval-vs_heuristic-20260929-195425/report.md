# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260929-195425`
Games logged: 300
Average rounds per game: 98.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 43 | 14.3% |
| heuristic_1 | 121 | 40.3% |
| heuristic_2 | 136 | 45.3% |

## End condition

- last_standing: 247 (82.3%)
- round_limit: 53 (17.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 33% | 57% | 96 |
| 2 | 30 | 17% | 27% | 57% | 99 |
| 3 | 30 | 10% | 47% | 43% | 85 |
| 4 | 30 | 3% | 40% | 57% | 113 |
| 5 | 30 | 27% | 37% | 37% | 93 |
| 6 | 30 | 17% | 57% | 27% | 105 |
| 7 | 30 | 13% | 37% | 50% | 91 |
| 8 | 30 | 17% | 43% | 40% | 104 |
| 9 | 30 | 10% | 40% | 50% | 98 |
| 10 | 30 | 20% | 43% | 37% | 103 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.5 | 4.0 | 1909 | 0.24 |
| heuristic_1 | 11.0 | 16.1 | 3842 | 0.90 |
| heuristic_2 | 12.3 | 18.4 | 4099 | 1.03 |

## Properties most often held by the winner

- St. Charles Place         92.7%  ############################
- Baltic Avenue             91.0%  ###########################-
- Short Line                90.3%  ###########################-
- Oriental Avenue           90.0%  ###########################-
- Virginia Avenue           89.7%  ###########################-
- St. James Place           89.7%  ###########################-
- North Carolina Avenue     89.3%  ###########################-
- Vermont Avenue            89.0%  ###########################-
- Electric Company          89.0%  ###########################-
- New York Avenue           89.0%  ###########################-
- Water Works               89.0%  ###########################-
- Marvin Gardens            89.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.89 per space
- lightblue  0.89 per space
- pink       0.89 per space
- util       0.89 per space
- orange     0.89 per space
- red        0.88 per space
- yellow     0.88 per space
- green      0.87 per space
- darkblue   0.87 per space
