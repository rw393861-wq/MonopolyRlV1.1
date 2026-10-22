# Monopoly self-play report

Run directory: `logs/train-20261022-185731`
Games logged: 60000
Average rounds per game: 60.2

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10106 | 16.8% |
| AI_2 | 16556 | 27.6% |
| AI_3 | 16404 | 27.3% |

## End condition

- last_standing: 59832 (99.7%)
- round_limit: 168 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 26% | 25% | 58 |
| 2 | 6000 | 16% | 25% | 28% | 59 |
| 3 | 6000 | 17% | 24% | 31% | 60 |
| 4 | 6000 | 17% | 32% | 26% | 60 |
| 5 | 6000 | 18% | 32% | 24% | 61 |
| 6 | 6000 | 17% | 22% | 27% | 61 |
| 7 | 6000 | 17% | 27% | 24% | 60 |
| 8 | 6000 | 17% | 27% | 34% | 61 |
| 9 | 6000 | 16% | 30% | 30% | 61 |
| 10 | 6000 | 17% | 32% | 26% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.3 | 1344 | 0.91 |
| AI_2 | 7.6 | 13.8 | 2319 | 1.42 |
| AI_3 | 7.5 | 14.1 | 2287 | 1.47 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.4%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Indiana Avenue            98.0%  ############################
- Water Works               97.9%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
