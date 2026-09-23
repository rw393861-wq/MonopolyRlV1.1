# Monopoly self-play report

Run directory: `logs/train-20260923-184342`
Games logged: 60000
Average rounds per game: 60.0

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10157 | 16.9% |
| AI_2 | 17506 | 29.2% |
| AI_3 | 15924 | 26.5% |

## End condition

- last_standing: 59840 (99.7%)
- round_limit: 160 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 26% | 27% | 59 |
| 2 | 6000 | 16% | 25% | 31% | 59 |
| 3 | 6000 | 16% | 21% | 32% | 60 |
| 4 | 6000 | 16% | 34% | 27% | 59 |
| 5 | 6000 | 17% | 32% | 30% | 60 |
| 6 | 6000 | 18% | 33% | 24% | 61 |
| 7 | 6000 | 16% | 28% | 21% | 61 |
| 8 | 6000 | 18% | 27% | 23% | 60 |
| 9 | 6000 | 17% | 35% | 24% | 60 |
| 10 | 6000 | 18% | 30% | 27% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1347 | 0.91 |
| AI_2 | 8.0 | 14.5 | 2412 | 1.46 |
| AI_3 | 7.2 | 13.8 | 2228 | 1.47 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.4%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.4%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           98.0%  ############################
- Water Works               97.9%  ############################
- Indiana Avenue            97.8%  ############################

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
- darkblue   0.97 per space
