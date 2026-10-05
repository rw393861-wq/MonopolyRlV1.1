# Monopoly self-play report

Run directory: `logs/train-20261005-214322`
Games logged: 60000
Average rounds per game: 60.4

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10027 | 16.7% |
| AI_2 | 15523 | 25.9% |
| AI_3 | 18307 | 30.5% |

## End condition

- last_standing: 59849 (99.7%)
- round_limit: 151 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 28% | 26% | 60 |
| 2 | 6000 | 17% | 27% | 27% | 61 |
| 3 | 6000 | 15% | 28% | 27% | 60 |
| 4 | 6000 | 17% | 24% | 36% | 61 |
| 5 | 6000 | 17% | 23% | 31% | 61 |
| 6 | 6000 | 17% | 31% | 31% | 61 |
| 7 | 6000 | 16% | 24% | 40% | 59 |
| 8 | 6000 | 18% | 27% | 26% | 60 |
| 9 | 6000 | 17% | 24% | 28% | 61 |
| 10 | 6000 | 18% | 24% | 32% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1342 | 0.89 |
| AI_2 | 7.1 | 13.3 | 2221 | 1.42 |
| AI_3 | 8.3 | 15.2 | 2507 | 1.47 |

## Properties most often held by the winner

- Reading Railroad          98.5%  ############################
- Illinois Avenue           98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.5%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.2%  ############################
- Electric Company          98.1%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Kentucky Avenue           98.0%  ############################
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
