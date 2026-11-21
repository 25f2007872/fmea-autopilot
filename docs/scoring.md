# Scoring scales

All scores are integers from 1 to 10. RPN = Severity × Occurrence × Detection.

## Severity (effect on product, patient, or customer)

| Score | Meaning |
| --- | --- |
| 1-2 | No noticeable effect; cosmetic or documentation-only |
| 3-4 | Minor effect; caught internally, minor rework |
| 5-6 | Moderate effect; batch or product rework, delay, customer inconvenience |
| 7-8 | Serious effect; product rejected or recalled, regulatory finding likely |
| 9-10 | Safety risk or critical regulatory non-compliance |

## Occurrence (how often the failure mode appears in the event data)

Derived from the number of grouped events in the data window, not guessed.

| Score | Events for this failure mode |
| ----- | ---------------------------- |
| 1-2   | 1 event                      |
| 3-4   | 2-3 events                   |
| 5-6   | 4-6 events                   |
| 7-8   | 7-10 events                  |
| 9-10  | More than 10 events          |

## Detection (how likely current controls are to catch it before impact)

| Score | Meaning                                                          |
| ----- | ---------------------------------------------------------------- |
| 1-2   | Controls almost certainly detect it (automated check, hard stop) |
| 3-4   | Strong controls; a reliable inspection step exists               |
| 5-6   | Moderate controls; relies on manual checks                       |
| 7-8   | Weak controls; detected only by chance or downstream             |
| 9-10  | No control; detected only after the customer is affected         |

## Review rules

- Any failure mode with Severity of 9 or 10 is always flagged for human review, regardless of RPN.
- Any row built from low-confidence extractions is flagged for review.
- Scores are proposals; a reviewer can override them, and the override is logged.
