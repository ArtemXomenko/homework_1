from datetime import datetime

def get_days_from_today(date_str: str) -> int:
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        print(f"Невірний формат дати: {date_str}. Очікується формат YYYY-MM-DD.")
        return None

