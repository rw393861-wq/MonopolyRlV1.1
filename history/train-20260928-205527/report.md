# Monopoly self-play report

Run directory: `logs/train-20260928-205527`
Games logged: 60000
Average rounds per game: 60.4

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10041 | 16.7% |
| AI_2 | 16946 | 28.2% |
| AI_3 | 17443 | 29.1% |

## End condition

- last_standing: 59866 (99.8%)
- round_limit: 134 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 30% | 25% | 60 |
| 2 | 6000 | 16% | 28% | 27% | 60 |
| 3 | 6000 | 16% | 29% | 26% | 60 |
| 4 | 6000 | 17% | 30% | 25% | 60 |
| 5 | 6000 | 18% | 25% | 31% | 61 |
| 6 | 6000 | 17% | 31% | 32% | 61 |
| 7 | 6000 | 16% | 18% | 37% | 60 |
| 8 | 6000 | 17% | 29% | 29% | 60 |
| 9 | 6000 | 17% | 29% | 34% | 60 |
| 10 | 6000 | 17% | 34% | 25% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1333 | 0.90 |
| AI_2 | 7.7 | 14.1 | 2338 | 1.47 |
| AI_3 | 8.0 | 15.0 | 2404 | 1.53 |

## Properties most often held by the winner

- Reading Railroad          98.7%  ############################
- Illinois Avenue           98.7%  ############################
- New York Avenue           98.5%  ############################
- St. Charles Place         98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.4%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Kentucky Avenue           98.1%  ############################
- Electric Company          98.0%  ############################
- Water Works               97.9%  ############################
- Indiana Avenue            97.9%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
