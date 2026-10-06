# Monopoly self-play report

Run directory: `logs/train-20261006-195358`
Games logged: 60000
Average rounds per game: 60.4

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9976 | 16.6% |
| AI_2 | 17250 | 28.8% |
| AI_3 | 16123 | 26.9% |

## End condition

- last_standing: 59836 (99.7%)
- round_limit: 164 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 25% | 28% | 59 |
| 2 | 6000 | 16% | 31% | 26% | 60 |
| 3 | 6000 | 16% | 30% | 24% | 60 |
| 4 | 6000 | 17% | 31% | 26% | 60 |
| 5 | 6000 | 18% | 28% | 29% | 61 |
| 6 | 6000 | 17% | 23% | 33% | 61 |
| 7 | 6000 | 16% | 34% | 24% | 61 |
| 8 | 6000 | 16% | 30% | 21% | 61 |
| 9 | 6000 | 15% | 30% | 23% | 61 |
| 10 | 6000 | 18% | 25% | 35% | 62 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1324 | 0.88 |
| AI_2 | 7.9 | 14.2 | 2388 | 1.40 |
| AI_3 | 7.3 | 13.8 | 2266 | 1.44 |

## Properties most often held by the winner

- Reading Railroad          98.7%  ############################
- New York Avenue           98.6%  ############################
- Illinois Avenue           98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.5%  ############################
- St. James Place           98.5%  ############################
- B&O Railroad              98.4%  ############################
- Pennsylvania Railroad     98.3%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           98.1%  ############################
- Water Works               97.9%  ############################
- Indiana Avenue            97.8%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
