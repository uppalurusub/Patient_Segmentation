from typing import Any

import requests
import streamlit as st

from config import BASE_URL, REQUEST_TIMEOUT


def _request(method: str, endpoint: str, **kwargs: Any) -> Any:
    url = f"{BASE_URL.rstrip('/')}/{endpoint.lstrip('/')}"

    try:
        response = requests.request(
            method=method,
            url=url,
            timeout=REQUEST_TIMEOUT,
            **kwargs,
        )
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        st.error(f"API request timed out: {endpoint}")
    except requests.ConnectionError:
        st.error(f"Unable to connect to API: {BASE_URL}")
    except requests.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else "Unknown"
        st.error(f"API request failed ({status_code}): {endpoint}")
    except requests.RequestException as exc:
        st.error(f"API request error: {exc}")
    except ValueError:
        st.error(f"Invalid JSON response received from: {endpoint}")

    return None


def get_data(endpoint: str, params: dict[str, Any] | None = None) -> Any:
    return _request("GET", endpoint, params=params)


def post_data(
    endpoint: str,
    payload: dict[str, Any] | None = None,
) -> Any:
    return _request("POST", endpoint, json=payload)
