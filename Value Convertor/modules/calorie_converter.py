def convert_calorie(amount, from_unit, to_unit):
    # Normalize unit strings to lowercase
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    conversion_factors = {
        "calories": 1,
        "kilojoules": 4.184,
        "kilocalories": 0.001,
        "joules": 4184  # 1 kilocalorie = 4184 joules
    }

    if from_unit in conversion_factors and to_unit in conversion_factors:
        return round(amount * (conversion_factors[to_unit] / conversion_factors[from_unit]), 4)
    else:
        return "❌ Invalid conversion unit."
