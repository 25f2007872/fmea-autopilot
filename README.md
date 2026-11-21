# FMEA Autopilot

Turn a pile of quality event forms into a ranked, traceable FMEA, automatically.

## The problem

Quality teams collect deviation and nonconformance reports as individual forms,
then spend hours by hand grouping similar events, scoring risk, and maintaining
an FMEA spreadsheet. The work is repetitive, error-prone, and quickly goes stale.

## What this does

FMEA Autopilot takes over the whole workflow, from the first form to the finished
FMEA:

1. **Ingest** quality event forms (text, DOCX, PDF)
2. **Extract** process step, failure mode, effect, cause, and current controls
3. **Group** similar events into a single failure mode
4. **Score** Severity, Occurrence (derived from event counts), and Detection,
   with written reasoning
5. **Rank** failure modes by RPN, with high-severity items always flagged
6. **Escalate** low-confidence or ambiguous cases to a human review queue
7. **Report** through a dashboard where every FMEA row traces back to its
   source events

## Design principles

- **Idempotent:** re-running on the same forms never duplicates rows or
  inflates occurrence counts.
- **Traceable:** every score links to the events and reasoning behind it.
- **Human in the loop:** the system handles routine cases; people make the
  judgment calls.
- **Observable:** structured logs and run history show what happened and why.

## Results

> _To be filled in after evaluation:_ time saved vs. manual FMEA, grouping
> accuracy against a hand-built gold set, and the share of rows needing
> human correction.

## Setup

> _Coming as the project is built._

## Note on data

All forms in this repository are synthetic. No real company data is used.

## Built for

Homingo Hackathon, Automation track (B1: Replace a department, not a task).
AI tools were used during development.
