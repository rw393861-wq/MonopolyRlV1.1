# Monopoly self-play report

Run directory: `logs/train-20261019-201726`
Games logged: 60000
Average rounds per game: 60.3

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10052 | 16.8% |
| AI_2 | 15672 | 26.1% |
| AI_3 | 16238 | 27.1% |

## End condition

- last_standing: 59842 (99.7%)
- round_limit: 158 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 18% | 29% | 30% | 59 |
| 2 | 6000 | 16% | 25% | 25% | 59 |
| 3 | 6000 | 16% | 26% | 25% | 59 |
| 4 | 6000 | 17% | 27% | 25% | 60 |
| 5 | 6000 | 18% | 28% | 30% | 61 |
| 6 | 6000 | 17% | 31% | 25% | 61 |
| 7 | 6000 | 17% | 23% | 23% | 62 |
| 8 | 6000 | 16% | 23% | 26% | 61 |
| 9 | 6000 | 16% | 25% | 28% | 61 |
| 10 | 6000 | 17% | 23% | 34% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1340 | 0.90 |
| AI_2 | 7.1 | 13.6 | 2229 | 1.45 |
| AI_3 | 7.4 | 14.3 | 2293 | 1.51 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Kentucky Avenue           98.0%  ############################
- Electric Company          98.0%  ############################
- Water Works               97.9%  ############################
- Indiana Avenue            97.8%  ############################

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
