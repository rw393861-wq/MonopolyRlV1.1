# Monopoly self-play report

Run directory: `logs/train-20260921-194835`
Games logged: 60000
Average rounds per game: 60.1

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10025 | 16.7% |
| AI_2 | 16844 | 28.1% |
| AI_3 | 17566 | 29.3% |

## End condition

- last_standing: 59827 (99.7%)
- round_limit: 173 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 24% | 34% | 58 |
| 2 | 6000 | 16% | 23% | 37% | 59 |
| 3 | 6000 | 16% | 28% | 30% | 60 |
| 4 | 6000 | 16% | 26% | 29% | 59 |
| 5 | 6000 | 17% | 29% | 30% | 60 |
| 6 | 6000 | 17% | 23% | 32% | 61 |
| 7 | 6000 | 17% | 32% | 26% | 60 |
| 8 | 6000 | 18% | 38% | 23% | 61 |
| 9 | 6000 | 16% | 29% | 27% | 60 |
| 10 | 6000 | 17% | 29% | 25% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1340 | 0.90 |
| AI_2 | 7.7 | 14.2 | 2328 | 1.49 |
| AI_3 | 8.0 | 14.8 | 2404 | 1.47 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- New York Avenue           98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          97.9%  ############################
- Kentucky Avenue           97.8%  ############################
- Indiana Avenue            97.8%  ############################
- Water Works               97.8%  ############################

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
