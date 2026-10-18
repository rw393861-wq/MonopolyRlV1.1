# Monopoly self-play report

Run directory: `logs/train-20261018-173930`
Games logged: 60000
Average rounds per game: 60.4

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9957 | 16.6% |
| AI_2 | 18612 | 31.0% |
| AI_3 | 15168 | 25.3% |

## End condition

- last_standing: 59834 (99.7%)
- round_limit: 166 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 30% | 28% | 59 |
| 2 | 6000 | 17% | 32% | 25% | 60 |
| 3 | 6000 | 16% | 30% | 24% | 60 |
| 4 | 6000 | 17% | 26% | 27% | 60 |
| 5 | 6000 | 18% | 31% | 26% | 60 |
| 6 | 6000 | 16% | 36% | 23% | 61 |
| 7 | 6000 | 16% | 30% | 24% | 61 |
| 8 | 6000 | 17% | 28% | 27% | 61 |
| 9 | 6000 | 16% | 35% | 26% | 61 |
| 10 | 6000 | 16% | 33% | 22% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1320 | 0.89 |
| AI_2 | 8.5 | 15.4 | 2529 | 1.47 |
| AI_3 | 6.9 | 13.4 | 2175 | 1.47 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Tennessee Avenue          98.6%  ############################
- New York Avenue           98.6%  ############################
- Illinois Avenue           98.5%  ############################
- St. Charles Place         98.5%  ############################
- B&O Railroad              98.5%  ############################
- St. James Place           98.4%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Water Works               98.0%  ############################
- Kentucky Avenue           97.9%  ############################
- Electric Company          97.9%  ############################
- Vermont Avenue            97.8%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
