# Monopoly self-play report

Run directory: `logs/train-20260925-190128`
Games logged: 60000
Average rounds per game: 60.5

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10253 | 17.1% |
| AI_2 | 16663 | 27.8% |
| AI_3 | 16269 | 27.1% |

## End condition

- last_standing: 59827 (99.7%)
- round_limit: 173 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 18% | 26% | 28% | 59 |
| 2 | 6000 | 17% | 29% | 28% | 60 |
| 3 | 6000 | 16% | 32% | 29% | 60 |
| 4 | 6000 | 17% | 32% | 24% | 60 |
| 5 | 6000 | 17% | 24% | 25% | 61 |
| 6 | 6000 | 17% | 24% | 29% | 60 |
| 7 | 6000 | 17% | 27% | 30% | 62 |
| 8 | 6000 | 18% | 29% | 24% | 61 |
| 9 | 6000 | 16% | 26% | 28% | 59 |
| 10 | 6000 | 18% | 30% | 27% | 62 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1359 | 0.91 |
| AI_2 | 7.6 | 14.2 | 2329 | 1.46 |
| AI_3 | 7.4 | 13.7 | 2289 | 1.42 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- St. Charles Place         98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- New York Avenue           98.5%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Water Works               98.0%  ############################
- Indiana Avenue            97.8%  ############################

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
