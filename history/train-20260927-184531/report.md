# Monopoly self-play report

Run directory: `logs/train-20260927-184531`
Games logged: 60000
Average rounds per game: 60.0

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10132 | 16.9% |
| AI_2 | 16414 | 27.4% |
| AI_3 | 16356 | 27.3% |

## End condition

- last_standing: 59846 (99.7%)
- round_limit: 154 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 29% | 29% | 59 |
| 2 | 6000 | 16% | 24% | 31% | 59 |
| 3 | 6000 | 16% | 30% | 26% | 60 |
| 4 | 6000 | 17% | 31% | 28% | 60 |
| 5 | 6000 | 18% | 28% | 31% | 61 |
| 6 | 6000 | 17% | 28% | 20% | 61 |
| 7 | 6000 | 17% | 24% | 22% | 59 |
| 8 | 6000 | 17% | 24% | 32% | 59 |
| 9 | 6000 | 17% | 31% | 25% | 61 |
| 10 | 6000 | 18% | 24% | 29% | 62 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1342 | 0.90 |
| AI_2 | 7.5 | 13.9 | 2286 | 1.42 |
| AI_3 | 7.4 | 13.7 | 2259 | 1.42 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           97.9%  ############################
- Water Works               97.8%  ############################
- Boardwalk                 97.8%  ############################

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
