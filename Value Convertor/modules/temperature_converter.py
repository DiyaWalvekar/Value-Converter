def convert_temperature(value, from_unit, to_unit):
    # Normalize units
    from_unit = from_unit.strip().lower()
    to_unit = to_unit.strip().lower()

    # Aliases for flexibility
    aliases = {
        "c": "celsius", "celsius": "celsius",
        "f": "fahrenheit", "fahrenheit": "fahrenheit",
        "k": "kelvin", "kelvin": "kelvin"
    }

    try:
        from_unit = aliases[from_unit]
        to_unit = aliases[to_unit]
    except KeyError:
        return "❌ Invalid temperature unit."

    # Conversion logic
    if from_unit == to_unit:
        return f"{round(value, 2)} {to_unit.capitalize()}"

    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return f"{round((value * 9/5) + 32, 2)} Fahrenheit"
        elif to_unit == "kelvin":
            return f"{round(value + 273.15, 2)} Kelvin"

    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return f"{round((value - 32) * 5/9, 2)} Celsius"
        elif to_unit == "kelvin":
            return f"{round((value - 32) * 5/9 + 273.15, 2)} Kelvin"

    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return f"{round(value - 273.15, 2)} Celsius"
        elif to_unit == "fahrenheit":
            return f"{round((value - 273.15) * 9/5 + 32, 2)} Fahrenheit"

    return "❌ Invalid temperature conversion."
