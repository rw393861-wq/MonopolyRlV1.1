# Monopoly self-play report

Run directory: `logs/train-20261024-174248`
Games logged: 60000
Average rounds per game: 60.1

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9974 | 16.6% |
| AI_2 | 16149 | 26.9% |
| AI_3 | 15933 | 26.6% |

## End condition

- last_standing: 59838 (99.7%)
- round_limit: 162 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 26% | 26% | 59 |
| 2 | 6000 | 16% | 25% | 25% | 60 |
| 3 | 6000 | 15% | 30% | 22% | 60 |
| 4 | 6000 | 16% | 26% | 33% | 59 |
| 5 | 6000 | 17% | 33% | 26% | 61 |
| 6 | 6000 | 17% | 27% | 22% | 61 |
| 7 | 6000 | 17% | 23% | 21% | 60 |
| 8 | 6000 | 17% | 27% | 24% | 60 |
| 9 | 6000 | 17% | 25% | 32% | 61 |
| 10 | 6000 | 17% | 27% | 34% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1313 | 0.89 |
| AI_2 | 7.4 | 14.0 | 2263 | 1.50 |
| AI_3 | 7.3 | 13.1 | 2220 | 1.40 |

## Properties most often held by the winner

- Reading Railroad          98.7%  ############################
- Illinois Avenue           98.6%  ############################
- New York Avenue           98.5%  ############################
- St. Charles Place         98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.4%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           97.8%  ############################
- Vermont Avenue            97.8%  ############################
- Water Works               97.8%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
