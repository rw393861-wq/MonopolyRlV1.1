# Monopoly self-play report

Run directory: `logs/train-20261017-173707`
Games logged: 60000
Average rounds per game: 59.7

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9985 | 16.6% |
| AI_2 | 16150 | 26.9% |
| AI_3 | 18769 | 31.3% |

## End condition

- last_standing: 59836 (99.7%)
- round_limit: 164 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 18% | 30% | 27% | 58 |
| 2 | 6000 | 16% | 31% | 30% | 59 |
| 3 | 6000 | 16% | 33% | 28% | 59 |
| 4 | 6000 | 16% | 30% | 32% | 60 |
| 5 | 6000 | 17% | 24% | 39% | 60 |
| 6 | 6000 | 16% | 20% | 43% | 59 |
| 7 | 6000 | 17% | 21% | 35% | 60 |
| 8 | 6000 | 17% | 25% | 26% | 60 |
| 9 | 6000 | 16% | 29% | 22% | 61 |
| 10 | 6000 | 17% | 27% | 31% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1323 | 0.89 |
| AI_2 | 7.4 | 13.9 | 2253 | 1.42 |
| AI_3 | 8.5 | 15.9 | 2506 | 1.56 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.3%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.0%  ############################
- Water Works               97.9%  ############################
- Kentucky Avenue           97.9%  ############################
- Boardwalk                 97.8%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
