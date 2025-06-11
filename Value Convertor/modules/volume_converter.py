def convert_volume(value, from_unit, to_unit):
    # Normalize inputs
    from_unit = from_unit.lower().rstrip('s')
    to_unit = to_unit.lower().rstrip('s')

    volume_units = {
        "liter": 1,
        "milliliter": 1000,
        "cubic meter": 0.001,
        "cubic inch": 61.0237,
        "cubic foot": 0.0353147
    }

    try:
        result = value * (volume_units[to_unit] / volume_units[from_unit])
        return f"{round(result, 4)} {to_unit.capitalize()}"
    except KeyError:
        return "❌ Invalid volume unit."
