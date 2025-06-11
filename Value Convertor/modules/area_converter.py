def convert_area(value, from_unit, to_unit):
    area_units = {
        "square meter": 1,
        "square kilometer": 1e-6,
        "square mile": 3.861e-7,
        "square yard": 1.19599,
        "square foot": 10.7639,
        "hectare": 1e-4,
        "acre": 0.000247105,
        "square inch": 1550.003
    }

    # Normalize units to lowercase
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    try:
        return round(value * (area_units[to_unit] / area_units[from_unit]), 6)
    except KeyError:
        return "❌ Invalid area unit provided."
