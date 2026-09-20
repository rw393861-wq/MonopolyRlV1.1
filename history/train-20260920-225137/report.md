# Monopoly self-play report

Run directory: `logs/train-20260920-225137`
Games logged: 5000
Average rounds per game: 58.4

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 777 | 15.5% |
| AI_2 | 1197 | 23.9% |
| AI_3 | 1588 | 31.8% |

## End condition

- last_standing: 4988 (99.8%)
- round_limit: 12 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 500 | 16% | 27% | 26% | 58 |
| 2 | 500 | 18% | 26% | 23% | 59 |
| 3 | 500 | 15% | 21% | 34% | 57 |
| 4 | 500 | 13% | 18% | 40% | 59 |
| 5 | 500 | 16% | 22% | 32% | 58 |
| 6 | 500 | 14% | 21% | 37% | 59 |
| 7 | 500 | 17% | 24% | 32% | 59 |
| 8 | 500 | 15% | 27% | 33% | 58 |
| 9 | 500 | 15% | 28% | 28% | 59 |
| 10 | 500 | 17% | 24% | 34% | 58 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.3 | 8.2 | 1203 | 0.88 |
| AI_2 | 6.5 | 12.3 | 1981 | 1.45 |
| AI_3 | 8.7 | 14.2 | 2417 | 1.37 |

## Properties most often held by the winner

- Tennessee Avenue          98.5%  ############################
- Illinois Avenue           98.5%  ############################
- New York Avenue           98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- St. Charles Place         98.2%  ############################
- Reading Railroad          98.2%  ############################
- Pennsylvania Railroad     97.9%  ############################
- Boardwalk                 97.8%  ############################
- Electric Company          97.7%  ############################
- Kentucky Avenue           97.6%  ############################
- Indiana Avenue            97.5%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.97 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
