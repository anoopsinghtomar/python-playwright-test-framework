# python-playwright-test-framework

A scalable, reusable, and enterprise-ready UI automation framework built with Python, Playwright, and Pytest, following the Page Object Model (POM) design pattern.

## Core Technologies 

| Purpose                  | Tool             |
|--------------------------|------------------|
| Programming Language     | Python 3.12+     |
| UI Automation            | Playwright       |
| Test Runner              | pytest           |
| HTML Reports             | pytest-html      |
| Parallel Execution       | pytest-xdist     |
| Environment Management   | python-dotenv    |
| Test Data Generation     | Faker            |
| Configuration Management | Pydantic         |
| Application & Test Logs  | Logging          |
| Version Control          | Git              |

## Installation Steps

1. Create the python playwright automation framework in github account and clone in local
2. Create the folder structure for the framework:

### Framework Structure

```
playwright-python-test-framework/
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── pytest.ini
├── .gitignore
├── .env
│
├── config/
│   ├── config.py
│   ├── settings.py
│   └── environments.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── locators/
│   ├── login_locators.py
│   ├── dashboard_locators.py
│   └── cart_locators.py
│
├── tests/
│   ├── smoke/
│   ├── regression/
│   ├── sanity/
│   └── api/
│
├── fixtures/
│   ├── browser_fixture.py
│   ├── data_fixture.py
│   └── user_fixture.py
│
├── utils/
│   ├── logger.py
│   ├── helper.py
│   ├── waits.py
│   ├── screenshot.py
│   └── retry.py
│
├── data/
│   ├── users.json
│   ├── testdata.json
│   └── products.json
│
├── reports/
│
├── screenshots/
│
├── logs/
│
├── traces/
│
└── .github/
    └── workflows/
        └── automation.yml
```

3. Create the virtual environment and activate the virtual environment

```Powershell
py -m venv .venv

.\.venv\Scripts\Activate

Optional: Run below if PowerShell is blocking the activate script from running:
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

```

4. Install your dependencies from requirements.txt:

```Bash
pip install -r requirements.txt
playwright install
```

5. 
 