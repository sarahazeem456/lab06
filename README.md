# lab06
Automated unit testing and CI pipeline implementation using pytest and GitHub Actions.

# Software Quality Engineering - Automated Testing & CI

This repository contains an automated unit testing suite implemented with **Python** and **pytest**, integrated with a continuous integration (CI) pipeline using **GitHub Actions**.

---

## 📌 Project Overview

The project validates business logic functions against boundary constraints, expected outcomes, and error handling. It demonstrates:
- Designing unit test cases for diverse functional scenarios.
- Catching assertion errors and inspecting test diagnostics.
- Automating test execution on push/PR events via GitHub Actions.

---

## 📂 Repository Structure

```text
├── .github/
│   └── workflows/
│       └── tests.yml          # GitHub Actions CI workflow
├── bank_account.py            # Core application logic
├── test_bank_account.py       # pytest test suite
└── README.md                  # Project documentation
