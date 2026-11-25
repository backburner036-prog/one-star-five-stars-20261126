# One Star, Five Stars for the Food

[![One Star, Five Stars for the Food](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/backburner036-prog/one-star-five-stars-20261126/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/backburner036-prog/one-star-five-stars-20261126/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

Entry for the make.fun bounty
[One Star, Five Stars for the Food](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7):
one sentence, 150 characters — a one-star review of Earth by an alien
tourist who still slips in a real compliment about the food.

## The sentence

> One star: the gravity bruised all four of my knees, the locals queue for air like it's rationed, yet the rendang made me forgive this whole damp rock.

Why this shape (from the winners' analysis in the screening file):
two beats — a specific alien grievance (gravity vs. four knees, queuing
for air like it's rationed), then the twist lands on a real named dish
(rendang), not a generic "the food was great".

## Run

```sh
python3 main.py
```

Pure Python standard library — no network. Writes one sentence to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), with a
self-check that it stays inside the sealed gate: 1–200 UTF-8 characters.
