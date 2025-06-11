def convert_frequency(amount, from_unit, to_unit):
    # Normalize units (case-insensitive and strip plural 's')
    from_unit = from_unit.lower().rstrip('s')
    to_unit = to_unit.lower().rstrip('s')

    conversion_factors = {
        "hertz": 1,
        "kilohertz": 1e3,
        "megahertz": 1e6,
        "gigahertz": 1e9
    }

    try:
        result = amount * (conversion_factors[to_unit] / conversion_factors[from_unit])
        return f"{round(result, 6)} {to_unit.capitalize()}"
    except KeyError:
        return "❌ Invalid frequency unit."
