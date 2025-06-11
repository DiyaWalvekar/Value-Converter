def convert_time(value, from_unit, to_unit):
    # Normalize units
    from_unit = from_unit.lower().rstrip('s')
    to_unit = to_unit.lower().rstrip('s')

    conversion_factors = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400
    }

    try:
        result = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        return f"{round(result, 4)} {to_unit}s"
    except KeyError:
        return "❌ Invalid time unit."
