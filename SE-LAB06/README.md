# SE Lab 6 — Code and Branch Coverage

**Student:** Debargho Banerji  
**SRN:** PES1UG24CS141  
**Assigned application:** Movie Tickets (Problem 15)

## Files

- `movie_tickets.py` — assigned application code.
- `CodeCoverageTest_141_application.py` — test cases for statement/line coverage.
- `BranchCoverageTest_141_application.py` — test cases targeting both outcomes of decision branches.

## Setup

```bash
python -m pip install pytest coverage
```

## Run code/line coverage

Run these commands from this directory:

```bash
coverage erase
coverage run --source=movie_tickets -m pytest -q CodeCoverageTest_141_application.py
coverage report -m
```

Verified locally: 15 tests passed and `movie_tickets.py` reported 100% line coverage. Take your own terminal screenshot showing the passing tests and the coverage percentage.

## Run branch coverage

```bash
coverage erase
coverage run --branch --source=movie_tickets -m pytest -q BranchCoverageTest_141_application.py
coverage report -m
```

Verified locally: 28 tests passed and `movie_tickets.py` reported 100% branch coverage (28 branches, 0 partial). Take your own terminal screenshot showing the passing tests and the branch coverage percentage.

## Coverage notes

Line coverage measures whether executable lines were run. Branch coverage additionally measures whether both outcomes of decision points were exercised. A high line-coverage percentage does not, by itself, prove that all decision branches have been tested.

The test suites are intentionally separate to demonstrate the two measurements. Use the actual terminal report as the evidence submitted; do not edit or fabricate coverage percentages.
