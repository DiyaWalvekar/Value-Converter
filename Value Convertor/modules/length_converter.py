def convert_length(value, from_unit, to_unit):
    # Normalize units
    from_unit = from_unit.lower().rstrip('s')
    to_unit = to_unit.lower().rstrip('s')

    conversion_rates = {
        "meter": 1,  # base
        "kilometer": 1e-3,
        "centimeter": 100,
        "millimeter": 1000,
        "mile": 0.000621371,
        "yard": 1.09361,
        "foot": 3.28084,
        "inch": 39.3701
    }

    if from_unit == to_unit:
        return f"{round(value, 6)} {to_unit}"

    if from_unit in conversion_rates and to_unit in conversion_rates:
        # Convert from source to base (meters), then to target
        value_in_meters = value / conversion_rates[from_unit]
        converted_value = value_in_meters * conversion_rates[to_unit]
        return f"{round(converted_value, 6)} {to_unit}"
    
    return "❌ Invalid length unit."
