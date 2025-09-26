# QA Portfolio Project 1

A compact portfolio project that demonstrates hands-on QA skills across **functional**, **integration**, and **API/CLI** testing using **Python + pytest**.  
The repository includes a clear test structure, reusable fixtures, and example configurations suited for showcasing testing approach and execution.

---

## Objectives
- Demonstrate practical QA workflow: test design → execution → reporting.
- Show proficiency in pytest (fixtures, parametrization, markers, configuration).
- Provide a reproducible setup for local runs and CI.

---

## Tech Stack
- **Language:** Python  
- **Test Runner:** pytest  
- **Config:** `pytest.ini`, `conftest.py`  
- **(Optional Reports):** `pytest-html`

---

## Project Structure
```
qa-portfolio-project-1/
├─ config/          # test data, environment configs, endpoints, constants
├─ modules/         # helpers, API/CLI clients, utilities
├─ tests/           # test suites (functional, integration, API)
├─ conftest.py      # shared fixtures, hooks
├─ pytest.ini       # pytest config (markers, options)
└─ become_qa_auto.db# sample DB/data (if used in tests)
```

---

## Getting Started

### 1) Clone the repository
```bash
git clone https://github.com/demianna-prometheus/qa-portfolio-project-1.git
cd qa-portfolio-project-1
```

### 2) Set up Python environment
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3) Install dependencies
If you have a `requirements.txt`:
```bash
pip install -r requirements.txt
```

Otherwise, install minimal tools:
```bash
pip install pytest requests
# Optional reporting:
pip install pytest-html allure-pytest
```

---

## Running Tests

### Run all tests
```bash
pytest -q
```

### Run selectively
```bash
# By file / test / node id
pytest tests/test_example.py::test_happy_path -q

# By marker (declared in pytest.ini)
pytest -m "ui" -q
```

### Generate reports
```bash
# HTML
pytest --html=report.html --self-contained-html

---

### Contact
For questions or suggestions, feel free to open an issue or reach out via GitHub.
