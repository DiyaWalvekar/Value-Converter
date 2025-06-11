def convert_power(value, from_unit, to_unit):
    # Normalize input
    from_unit = from_unit.lower().rstrip('s')
    to_unit = to_unit.lower().rstrip('s')

    conversion_factors = {
        "watt": {"watt": 1, "kilowatt": 0.001, "horsepower": 0.00134102},
        "kilowatt": {"watt": 1000, "kilowatt": 1, "horsepower": 1.34102},
        "horsepower": {"watt": 745.7, "kilowatt": 0.7457, "horsepower": 1}
    }

    try:
        result = value * conversion_factors[from_unit][to_unit]
        return f"{round(result, 4)} {to_unit.capitalize()}"
    except KeyError:
        return "❌ Invalid power unit."
