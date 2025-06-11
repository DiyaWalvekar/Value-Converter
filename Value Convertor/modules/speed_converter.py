def convert_speed(value, from_unit, to_unit):
    # Normalize units
    from_unit = from_unit.lower().replace(" ", "").replace("per", "/").replace("ph", "/h").replace("kmph", "km/h")
    to_unit = to_unit.lower().replace(" ", "").replace("per", "/").replace("ph", "/h").replace("kmph", "km/h")

    # Conversion to base unit: km/h
    conversion_factors = {
        "km/h": 1,
        "m/s": 0.277778,
        "mph": 0.621371,
        "knot": 0.539957
    }

    try:
        result = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        return f"{round(result, 4)} {to_unit.upper()}"
    except KeyError:
        return "❌ Invalid speed unit."
