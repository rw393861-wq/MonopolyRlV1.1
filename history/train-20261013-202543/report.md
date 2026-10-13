# Monopoly self-play report

Run directory: `logs/train-20261013-202543`
Games logged: 60000
Average rounds per game: 60.6

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10158 | 16.9% |
| AI_2 | 16622 | 27.7% |
| AI_3 | 16858 | 28.1% |

## End condition

- last_standing: 59812 (99.7%)
- round_limit: 188 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 26% | 26% | 59 |
| 2 | 6000 | 16% | 30% | 27% | 59 |
| 3 | 6000 | 16% | 26% | 30% | 60 |
| 4 | 6000 | 16% | 29% | 30% | 59 |
| 5 | 6000 | 18% | 28% | 27% | 62 |
| 6 | 6000 | 17% | 23% | 31% | 62 |
| 7 | 6000 | 17% | 25% | 29% | 61 |
| 8 | 6000 | 16% | 32% | 28% | 62 |
| 9 | 6000 | 17% | 28% | 30% | 61 |
| 10 | 6000 | 18% | 30% | 23% | 62 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1348 | 0.91 |
| AI_2 | 7.6 | 14.5 | 2352 | 1.48 |
| AI_3 | 7.7 | 14.2 | 2344 | 1.47 |

## Properties most often held by the winner

- Reading Railroad          98.7%  ############################
- Illinois Avenue           98.6%  ############################
- St. Charles Place         98.6%  ############################
- New York Avenue           98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- St. James Place           98.5%  ############################
- B&O Railroad              98.3%  ############################
- Electric Company          98.1%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Water Works               98.0%  ############################
- Boardwalk                 97.8%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
