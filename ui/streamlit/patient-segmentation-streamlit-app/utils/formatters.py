from typing import Any


def format_currency(value: float | int | None, decimals: int = 2) -> str:
    if value is None:
        return "-"
    return f"${value:,.{decimals}f}"


def format_number(value: float | int | None, decimals: int = 2) -> str:
    if value is None:
        return "-"
    if isinstance(value, int):
        return f"{value:,}"
    return f"{value:,.{decimals}f}"


def format_percentage(value: float | int | None, decimals: int = 2) -> str:
    if value is None:
        return "-"
    return f"{value:,.{decimals}f}%"


def format_label(value: Any) -> str:
    return str(value).replace("_", " ").strip().title()
