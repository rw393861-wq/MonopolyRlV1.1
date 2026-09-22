# Monopoly self-play report

Run directory: `logs/train-20260922-182434`
Games logged: 60000
Average rounds per game: 59.8

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10218 | 17.0% |
| AI_2 | 17133 | 28.6% |
| AI_3 | 15835 | 26.4% |

## End condition

- last_standing: 59866 (99.8%)
- round_limit: 134 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 29% | 24% | 60 |
| 2 | 6000 | 17% | 27% | 24% | 59 |
| 3 | 6000 | 16% | 32% | 22% | 59 |
| 4 | 6000 | 17% | 26% | 26% | 60 |
| 5 | 6000 | 18% | 22% | 32% | 60 |
| 6 | 6000 | 17% | 24% | 36% | 60 |
| 7 | 6000 | 18% | 32% | 30% | 60 |
| 8 | 6000 | 18% | 37% | 24% | 60 |
| 9 | 6000 | 16% | 30% | 23% | 61 |
| 10 | 6000 | 18% | 28% | 24% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.4 | 1352 | 0.90 |
| AI_2 | 7.8 | 13.8 | 2338 | 1.44 |
| AI_3 | 7.2 | 13.6 | 2216 | 1.45 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- New York Avenue           98.6%  ############################
- St. Charles Place         98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Kentucky Avenue           98.0%  ############################
- Electric Company          98.0%  ############################
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
