# Monopoly self-play report

Run directory: `logs/train-20261002-193916`
Games logged: 60000
Average rounds per game: 60.1

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10016 | 16.7% |
| AI_2 | 16205 | 27.0% |
| AI_3 | 17527 | 29.2% |

## End condition

- last_standing: 59833 (99.7%)
- round_limit: 167 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 24% | 30% | 59 |
| 2 | 6000 | 16% | 30% | 26% | 60 |
| 3 | 6000 | 16% | 27% | 31% | 59 |
| 4 | 6000 | 17% | 26% | 24% | 60 |
| 5 | 6000 | 17% | 36% | 23% | 60 |
| 6 | 6000 | 18% | 30% | 30% | 62 |
| 7 | 6000 | 17% | 21% | 38% | 60 |
| 8 | 6000 | 17% | 21% | 37% | 60 |
| 9 | 6000 | 16% | 23% | 28% | 60 |
| 10 | 6000 | 17% | 32% | 25% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1325 | 0.89 |
| AI_2 | 7.4 | 13.8 | 2273 | 1.43 |
| AI_3 | 8.0 | 14.9 | 2386 | 1.50 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- New York Avenue           98.5%  ############################
- Reading Railroad          98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           98.0%  ############################
- Vermont Avenue            97.8%  ############################
- Indiana Avenue            97.7%  ############################

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
