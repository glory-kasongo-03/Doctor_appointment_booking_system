
# Contributing to Doctor Appointment Booking System

Thanks for your interest in contributing! 
This project uses FastAPI, Python 3.10+, and GitHub Actions for CI/CD.

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or higher
- `pip`
- `git`

### Installation

```bash
git clone https://github.com/your-username/doctor-appointment-booking.git
cd doctor-appointment-booking
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

```bash
pytest tests/
```

## Coding Standards

- Follow **PEP8**
- Use `black` for formatting
- Use `flake8` for linting

## Picking Issues

1. Check the [Issues tab](https://github.com/your-username/doctor-appointment-booking/issues)
2. Choose an issue labeled `good first issue`
3. Ask to be assigned before starting

## 🚀 Submitting a Pull Request

```bash
git checkout -b fix/issue-123-description
# make changes
pytest
git add .
git commit -m "Fix: issue description"
git push origin fix/issue-123-description
```

Open a PR to `main`, reference the issue, and wait for CI to pass.
