# Monopoly self-play report

Run directory: `logs/train-20261011-191559`
Games logged: 60000
Average rounds per game: 59.9

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9950 | 16.6% |
| AI_2 | 18021 | 30.0% |
| AI_3 | 16501 | 27.5% |

## End condition

- last_standing: 59846 (99.7%)
- round_limit: 154 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 30% | 30% | 59 |
| 2 | 6000 | 15% | 35% | 26% | 59 |
| 3 | 6000 | 16% | 31% | 30% | 60 |
| 4 | 6000 | 16% | 36% | 25% | 60 |
| 5 | 6000 | 18% | 34% | 24% | 61 |
| 6 | 6000 | 17% | 30% | 31% | 60 |
| 7 | 6000 | 17% | 29% | 24% | 60 |
| 8 | 6000 | 17% | 31% | 24% | 59 |
| 9 | 6000 | 16% | 22% | 29% | 61 |
| 10 | 6000 | 16% | 22% | 32% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1312 | 0.89 |
| AI_2 | 8.2 | 15.5 | 2437 | 1.51 |
| AI_3 | 7.5 | 13.7 | 2289 | 1.41 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.5%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.0%  ############################
- Water Works               98.0%  ############################
- Kentucky Avenue           97.8%  ############################
- Indiana Avenue            97.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.96 per space
