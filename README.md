# Hudl Login Test Suite

Selenium-based end-to-end tests for the Hudl login page, written in Python with pytest.

---

## Prerequisites

| Requirement | Windows | macOS |
|---|---|---|
| Python 3.9+ | [python.org](https://www.python.org/downloads/) | `brew install python` or [python.org](https://www.python.org/downloads/) |
| Google Chrome | [Download](https://www.google.com/chrome/) | [Download](https://www.google.com/chrome/) |
| Firefox (optional) | [Download](https://www.mozilla.org/firefox/) | [Download](https://www.mozilla.org/firefox/) |

Selenium 4 manages browser drivers automatically — no manual ChromeDriver or GeckoDriver installation needed.

---

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd hudl-interview-project
```

### 2. Create a virtual environment

**Windows (Command Prompt or PowerShell):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS (Terminal):**
```bash
python3 -m venv venv
source venv/bin/activate
```

Your prompt will change to show `(venv)` when the environment is active.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure credentials

Create a `.env` file in the project root:

**Windows:**
```cmd
copy NUL .env
```

**macOS:**
```bash
touch .env
```

Open `.env` in any text editor and add your Hudl credentials:

```
HUDL_USERNAME=your_email@example.com
HUDL_PASSWORD=your_password
```

> The `.env` file is not committed to version control. Never share or commit it.

---

## Running the Tests

### Run all tests (single browser)

**Windows:**
```cmd
python -m pytest --browser=chrome
```

**macOS:**
```bash
python -m pytest --browser=chrome
```

Supported values for `--browser`: `chrome` (default), `firefox`, `safari` (macOS only).

### Run all browsers at once

**Windows:**
```cmd
run_tests.bat
```

**macOS:**
```bash
chmod +x run_tests.sh   # first time only
./run_tests.sh
```

This runs Chrome and Firefox in sequence. On macOS, Safari is also run if `safaridriver` is available (see [Safari setup](#safari-macos-only) below).

### Run in headless mode

Add `--headless` to suppress browser windows:

```bash
python -m pytest --browser=chrome --headless
```

> Safari does not support headless mode.

### Run a specific test file or test

```bash
# Single file
python -m pytest tests/test_login.py

# Single test by name
python -m pytest tests/test_login.py::TestLogin::test_successful_login

# Single class
python -m pytest tests/test_login.py::TestLoginPageUI
```

---

## Test Report

After each run, an HTML report is written to:

```
reports/report.html
```

Open it in any browser to view results, including pass/fail status and error details.

---

## Safari (macOS only)

Safari requires a one-time setup:

```bash
safaridriver --enable
```

You may be prompted for your macOS password. Once enabled, Safari tests run automatically when using `./run_tests.sh`.

---

## Project Structure

```
hudl-interview-project/
├── pages/
│   ├── base_page.py       # Shared Selenium helpers
│   ├── login_page.py      # Login page locators and actions
│   └── home_page.py       # Home page locators and actions
├── tests/
│   └── test_login.py      # Login test cases
├── reports/               # Generated HTML reports
├── conftest.py            # pytest fixtures and WebDriver setup
├── pytest.ini             # pytest configuration
├── requirements.txt       # Python dependencies
├── run_tests.bat          # Run all browsers (Windows)
└── run_tests.sh           # Run all browsers (macOS/Linux)
```
