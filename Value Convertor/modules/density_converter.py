def convert_data(value, from_unit, to_unit):
    # Normalize units (case-insensitive & singular)
    from_unit = from_unit.lower().rstrip('s')
    to_unit = to_unit.lower().rstrip('s')

    # Decimal (SI) data units
    data_units = {
        "bit": 1/8,
        "byte": 1,
        "kilobyte": 1e3,
        "megabyte": 1e6,
        "gigabyte": 1e9,
        "terabyte": 1e12,
        "petabyte": 1e15
    }

    try:
        result = value * (data_units[to_unit] / data_units[from_unit])
        return f"{round(result, 6)} {to_unit.capitalize()}"
    except KeyError:
        return "❌ Invalid data unit provided."
