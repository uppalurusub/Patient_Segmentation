# Healthcare Analytics Streamlit App

Refactored modular Streamlit frontend for the Healthcare Analytics and Patient Segmentation API.

## Structure

```text
.
├── .streamlit/
│   └── config.toml
├── api/
│   ├── __init__.py
│   └── client.py
├── components/
│   ├── __init__.py
│   ├── request_form.py
│   ├── response_view.py
│   └── sidebar.py
├── utils/
│   ├── __init__.py
│   ├── charts.py
│   └── formatters.py
├── pages/
│   ├── clinical_page.py
│   ├── cost_page.py
│   ├── executive_page.py
│   ├── patient_page.py
│   ├── risk_page.py
│   ├── segment_page.py
│   └── utilization_page.py
├── app.py
├── config.py
└── requirements.txt
```

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

The API base URL defaults to `http://localhost:8000`. Override it with the `API_BASE_URL` environment variable.
