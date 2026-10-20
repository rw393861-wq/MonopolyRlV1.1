# Monopoly self-play report

Run directory: `logs/train-20261020-184919`
Games logged: 60000
Average rounds per game: 60.3

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10289 | 17.1% |
| AI_2 | 16565 | 27.6% |
| AI_3 | 17264 | 28.8% |

## End condition

- last_standing: 59806 (99.7%)
- round_limit: 194 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 18% | 28% | 29% | 59 |
| 2 | 6000 | 17% | 28% | 27% | 59 |
| 3 | 6000 | 16% | 32% | 27% | 60 |
| 4 | 6000 | 16% | 32% | 24% | 61 |
| 5 | 6000 | 18% | 26% | 36% | 60 |
| 6 | 6000 | 18% | 25% | 36% | 62 |
| 7 | 6000 | 18% | 28% | 29% | 61 |
| 8 | 6000 | 17% | 25% | 26% | 60 |
| 9 | 6000 | 17% | 27% | 25% | 61 |
| 10 | 6000 | 18% | 27% | 28% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.4 | 1355 | 0.90 |
| AI_2 | 7.5 | 14.2 | 2317 | 1.45 |
| AI_3 | 7.9 | 14.6 | 2398 | 1.47 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Electric Company          98.0%  ############################
- Pennsylvania Railroad     98.0%  ############################
- Kentucky Avenue           97.9%  ############################
- Water Works               97.9%  ############################
- Indiana Avenue            97.8%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
