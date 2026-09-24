# Monopoly self-play report

Run directory: `logs/train-20260924-184438`
Games logged: 60000
Average rounds per game: 60.0

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9950 | 16.6% |
| AI_2 | 15720 | 26.2% |
| AI_3 | 18066 | 30.1% |

## End condition

- last_standing: 59861 (99.8%)
- round_limit: 139 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 25% | 31% | 59 |
| 2 | 6000 | 16% | 27% | 31% | 59 |
| 3 | 6000 | 15% | 26% | 36% | 59 |
| 4 | 6000 | 16% | 31% | 25% | 60 |
| 5 | 6000 | 17% | 27% | 28% | 61 |
| 6 | 6000 | 18% | 24% | 34% | 60 |
| 7 | 6000 | 17% | 30% | 30% | 61 |
| 8 | 6000 | 17% | 30% | 25% | 60 |
| 9 | 6000 | 15% | 23% | 25% | 60 |
| 10 | 6000 | 17% | 20% | 35% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1322 | 0.89 |
| AI_2 | 7.2 | 13.6 | 2230 | 1.42 |
| AI_3 | 8.2 | 15.0 | 2448 | 1.51 |

## Properties most often held by the winner

- Illinois Avenue           98.7%  ############################
- Reading Railroad          98.6%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Electric Company          98.0%  ############################
- Indiana Avenue            97.9%  ############################
- Water Works               97.8%  ############################

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
