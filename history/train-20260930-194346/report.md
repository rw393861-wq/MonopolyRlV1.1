# Monopoly self-play report

Run directory: `logs/train-20260930-194346`
Games logged: 60000
Average rounds per game: 60.1

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10063 | 16.8% |
| AI_2 | 15385 | 25.6% |
| AI_3 | 16532 | 27.6% |

## End condition

- last_standing: 59823 (99.7%)
- round_limit: 177 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 28% | 29% | 59 |
| 2 | 6000 | 17% | 25% | 30% | 60 |
| 3 | 6000 | 16% | 26% | 35% | 59 |
| 4 | 6000 | 17% | 34% | 28% | 61 |
| 5 | 6000 | 17% | 25% | 33% | 61 |
| 6 | 6000 | 17% | 27% | 26% | 62 |
| 7 | 6000 | 17% | 24% | 27% | 60 |
| 8 | 6000 | 17% | 20% | 25% | 60 |
| 9 | 6000 | 16% | 22% | 22% | 60 |
| 10 | 6000 | 17% | 27% | 20% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1331 | 0.89 |
| AI_2 | 7.0 | 13.3 | 2191 | 1.40 |
| AI_3 | 7.5 | 13.8 | 2298 | 1.43 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- Illinois Avenue           98.4%  ############################
- St. James Place           98.4%  ############################
- St. Charles Place         98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Kentucky Avenue           97.9%  ############################
- Water Works               97.9%  ############################
- Electric Company          97.8%  ############################
- Vermont Avenue            97.7%  ############################

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
