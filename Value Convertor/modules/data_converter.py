def convert_data(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    data_units = {
        "byte": 1,
        "kilobyte": 1e3,
        "megabyte": 1e6,
        "gigabyte": 1e9,
        "terabyte": 1e12
    }

    try:
        return round(value * (data_units[to_unit] / data_units[from_unit]), 6)
    except KeyError:
        return "❌ Invalid data unit."
