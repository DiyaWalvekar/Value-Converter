def convert_pressure(value, from_unit, to_unit):
    # Normalize input
    from_unit = from_unit.lower().rstrip('s')
    to_unit = to_unit.lower().rstrip('s')

    conversion_factors = {
        "pascal": {"pascal": 1, "bar": 1e-5, "atmosphere": 9.8692e-6},
        "bar": {"pascal": 100000, "bar": 1, "atmosphere": 0.986923},
        "atmosphere": {"pascal": 101325, "bar": 1.01325, "atmosphere": 1}
    }

    try:
        result = value * conversion_factors[from_unit][to_unit]
        return f"{round(result, 4)} {to_unit.capitalize()}"
    except KeyError:
        return "❌ Invalid pressure unit."
