# Monopoly self-play report

Run directory: `logs/train-20261021-190143`
Games logged: 60000
Average rounds per game: 59.8

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9874 | 16.5% |
| AI_2 | 16929 | 28.2% |
| AI_3 | 16417 | 27.4% |

## End condition

- last_standing: 59854 (99.8%)
- round_limit: 146 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 33% | 26% | 59 |
| 2 | 6000 | 17% | 34% | 24% | 59 |
| 3 | 6000 | 17% | 30% | 25% | 60 |
| 4 | 6000 | 17% | 23% | 31% | 61 |
| 5 | 6000 | 16% | 20% | 39% | 60 |
| 6 | 6000 | 17% | 21% | 38% | 60 |
| 7 | 6000 | 17% | 32% | 25% | 61 |
| 8 | 6000 | 16% | 34% | 27% | 60 |
| 9 | 6000 | 16% | 32% | 19% | 60 |
| 10 | 6000 | 16% | 24% | 20% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.5 | 9.0 | 1311 | 0.88 |
| AI_2 | 7.7 | 14.6 | 2340 | 1.49 |
| AI_3 | 7.5 | 14.0 | 2290 | 1.43 |

## Properties most often held by the winner

- Reading Railroad          98.5%  ############################
- Illinois Avenue           98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           98.0%  ############################
- Water Works               97.9%  ############################
- Vermont Avenue            97.8%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
