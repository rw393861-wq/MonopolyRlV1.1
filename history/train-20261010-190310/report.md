# Monopoly self-play report

Run directory: `logs/train-20261010-190310`
Games logged: 60000
Average rounds per game: 60.0

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10171 | 17.0% |
| AI_2 | 17341 | 28.9% |
| AI_3 | 15781 | 26.3% |

## End condition

- last_standing: 59834 (99.7%)
- round_limit: 166 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 25% | 27% | 59 |
| 2 | 6000 | 16% | 29% | 27% | 59 |
| 3 | 6000 | 16% | 31% | 27% | 59 |
| 4 | 6000 | 17% | 31% | 24% | 60 |
| 5 | 6000 | 18% | 24% | 29% | 61 |
| 6 | 6000 | 17% | 30% | 25% | 61 |
| 7 | 6000 | 17% | 39% | 24% | 60 |
| 8 | 6000 | 17% | 35% | 27% | 60 |
| 9 | 6000 | 17% | 24% | 25% | 60 |
| 10 | 6000 | 17% | 21% | 28% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1342 | 0.89 |
| AI_2 | 7.9 | 14.3 | 2368 | 1.47 |
| AI_3 | 7.2 | 13.8 | 2231 | 1.46 |

## Properties most often held by the winner

- Tennessee Avenue          98.6%  ############################
- Illinois Avenue           98.5%  ############################
- Reading Railroad          98.5%  ############################
- New York Avenue           98.5%  ############################
- St. James Place           98.4%  ############################
- St. Charles Place         98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           97.9%  ############################
- Water Works               97.9%  ############################
- Boardwalk                 97.8%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
