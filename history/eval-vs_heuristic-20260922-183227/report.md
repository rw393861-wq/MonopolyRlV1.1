# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260922-183227`
Games logged: 300
Average rounds per game: 98.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 36 | 12.0% |
| heuristic_1 | 119 | 39.7% |
| heuristic_2 | 145 | 48.3% |

## End condition

- last_standing: 245 (81.7%)
- round_limit: 55 (18.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 43% | 47% | 83 |
| 2 | 30 | 13% | 40% | 47% | 89 |
| 3 | 30 | 0% | 57% | 43% | 103 |
| 4 | 30 | 17% | 37% | 47% | 98 |
| 5 | 30 | 17% | 37% | 47% | 111 |
| 6 | 30 | 17% | 27% | 57% | 102 |
| 7 | 30 | 10% | 53% | 37% | 107 |
| 8 | 30 | 7% | 47% | 47% | 97 |
| 9 | 30 | 7% | 37% | 57% | 90 |
| 10 | 30 | 23% | 20% | 57% | 102 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.5 | 4.2 | 1726 | 0.34 |
| heuristic_1 | 11.3 | 16.2 | 3966 | 0.85 |
| heuristic_2 | 12.8 | 18.7 | 4304 | 1.06 |

## Properties most often held by the winner

- Reading Railroad          90.3%  ############################
- B&O Railroad              90.0%  ############################
- Mediterranean Avenue      89.7%  ############################
- Baltic Avenue             89.7%  ############################
- Electric Company          89.3%  ############################
- Tennessee Avenue          88.7%  ###########################-
- Marvin Gardens            88.3%  ###########################-
- New York Avenue           88.0%  ###########################-
- Atlantic Avenue           88.0%  ###########################-
- St. James Place           87.7%  ###########################-
- Short Line                87.7%  ###########################-
- Vermont Avenue            87.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.89 per space
- lightblue  0.87 per space
- pink       0.86 per space
- util       0.88 per space
- orange     0.88 per space
- red        0.86 per space
- yellow     0.87 per space
- green      0.87 per space
- darkblue   0.87 per space
