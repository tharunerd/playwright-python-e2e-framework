# Playwright Python E2E Automation Framework

A scalable End-to-End Test Automation Framework built using Python, Playwright, and Pytest.

This project demonstrates:

* UI Automation Testing
* API Testing
* Page Object Model (POM)
* Pytest Framework Design
* CI/CD Integration using GitHub Actions
* Docker Support
* Parallel Test Execution
* HTML & Allure Reporting
* Environment-based Configuration

---

# Tech Stack

| Technology     | Usage                |
| -------------- | -------------------- |
| Python         | Programming Language |
| Playwright     | Browser Automation   |
| Pytest         | Test Framework       |
| Requests       | API Testing          |
| Allure         | Advanced Reporting   |
| Pytest HTML    | HTML Reports         |
| GitHub Actions | CI/CD Pipeline       |
| Docker         | Containerization     |

---

# Project Structure

```text
playwright-python-e2e-framework/
│
├── .github/
│   └── workflows/
│
├── api/
│   ├── __init__.py
│   └── test_users_api.py
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── reports/
├── screenshots/
│
├── test_data/
│   └── users.json
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── utils/
│   ├── __init__.py
│   ├── config.py
│   ├── helpers.py
│   └── logger.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Dockerfile
├── .env
├── README.md
└── LICENSE
```

---

# Features

## UI Automation

* Login Validation
* Inventory Validation
* Add to Cart Flow
* Checkout Flow
* End-to-End Purchase Validation

## API Automation

* REST API Validation
* Status Code Verification
* Response Validation
* JSON Schema Validation

## Reporting

* HTML Reports
* Allure Reports
* Screenshot Capture on Failures

## CI/CD

* GitHub Actions Integration
* Automated Test Execution on Push
* Parallel Test Execution

---

# Application Under Test

Website Used:

[https://www.saucedemo.com/](https://www.saucedemo.com/)

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/tharunerd/playwright-python-e2e-framework.git
```

## Navigate to Project

```bash
cd playwright-python-e2e-framework
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\Activate.ps1
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Playwright Browsers

```bash
playwright install
```

---

# Run Tests

## Run All Tests

```bash
pytest
```

## Run Tests in Headed Mode

```bash
pytest --headed
```

## Run Tests in Parallel

```bash
pytest -n 4
```

---

# Generate HTML Report

```bash
pytest --html=reports/report.html
```

---

# Generate Allure Report

## Generate Results

```bash
pytest --alluredir=reports/allure-results
```

## Open Allure Report

```bash
allure serve reports/allure-results
```

---

# Environment Configuration

Environment variables are managed using `.env`.

Example:

```env
BASE_URL=https://www.saucedemo.com/
```

---

# Design Patterns Used

* Page Object Model (POM)
* Data-Driven Testing
* Reusable Utility Architecture
* Environment-Based Configuration

---

# Future Enhancements

* Docker Integration
* Jenkins Pipeline
* Cross Browser Execution
* Retry Mechanism
* Slack Notifications
* Advanced Logging
* Test Tagging & Filtering

---

# CI/CD Pipeline

GitHub Actions workflow will:

* Install dependencies
* Install Playwright browsers
* Execute tests
* Generate reports automatically

---

# Author

Tharun Kumar Akula 
Automation Test Engineer | Playwright | Python | API Testing | CI/CD
Feel free to contribute or collabirate with this repo 