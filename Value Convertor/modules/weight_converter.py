def convert_weight(amount, from_unit, to_unit):
    # Normalize unit names (case-insensitive, remove plurals)
    from_unit = from_unit.strip().lower().rstrip("s")
    to_unit = to_unit.strip().lower().rstrip("s")

    conversion_factors = {
        "kilogram": 1,
        "gram": 0.001,
        "milligram": 0.000001,
        "metric ton": 1000,
        "pound": 0.453592,
        "ounce": 0.0283495
    }

    # Check for valid units
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "❌ Invalid weight unit."

    # Convert to kilograms
    amount_in_kg = amount * conversion_factors[from_unit]

    # Convert from kg to target unit
    result = amount_in_kg / conversion_factors[to_unit]

    return f"{round(result, 5)} {to_unit.capitalize()}"
