from flask import Flask, render_template, request
from modules.currency_converter import convert_currency
from modules.temperature_converter import convert_temperature
from modules.length_converter import convert_length
from modules.weight_converter import convert_weight
from modules.speed_converter import convert_speed
from modules.time_converter import convert_time
from modules.area_converter import convert_area
from modules.volume_converter import convert_volume
from modules.data_converter import convert_data
from modules.calorie_converter import convert_calorie
from modules.frequency_converter import convert_frequency
from modules.angle_converter import convert_angle
from modules.power_converter import convert_power
from modules.pressure_converter import convert_pressure
from modules.density_converter import convert_density

app = Flask(__name__)


# Landing Page Route
@app.route("/")
def landing():
    return render_template("landing.html")  # Shows landing page

# Value Converter Home Page
@app.route("/home")
def home():
    return render_template("index.html")  # Shows main converter page

# Individual Pages
@app.route("/currency")
def currency():
    return render_template("currency.html")

@app.route("/temperature")
def temperature():
    return render_template("temperature.html")

@app.route("/length")
def length():
    return render_template("length.html")

@app.route("/weight")
def weight():
    return render_template("weight.html")

@app.route("/speed")
def speed():
    return render_template("speed.html")

@app.route("/time")
def time():
    return render_template("time.html")

@app.route("/area")
def area():
    return render_template("area.html")

@app.route("/volume")
def volume():
    return render_template("volume.html")

@app.route("/data")
def data_storage():
    return render_template("data.html")

@app.route("/calorie")
def calorie():
    return render_template("calorie.html")

@app.route("/frequency")
def frequency():
    return render_template("frequency.html")

@app.route("/angle")
def angle():
    return render_template("angle.html")

@app.route("/power")
def power():
    return render_template("power.html")

@app.route("/pressure")
def pressure():
    return render_template("pressure.html")

# Conversion Routes
@app.route("/convert_currency", methods=["POST"])
def convert_currency_route():
    amount = float(request.form["amount"])
    from_currency = request.form["from_currency"]
    to_currency = request.form["to_currency"]
    result = convert_currency(amount, from_currency, to_currency)
    return render_template("currency.html", result=result)

@app.route("/convert_temperature", methods=["POST"])
def convert_temperature_route():
    temp = float(request.form["temperature"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_temperature(temp, from_unit, to_unit)
    return render_template("temperature.html", result=result)

@app.route("/convert_length", methods=["POST"])
def convert_length_route():
    length = float(request.form["length"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_length(length, from_unit, to_unit)
    return render_template("length.html", result=result)

@app.route("/convert_weight", methods=["POST"])
def convert_weight_route():
    weight = float(request.form["weight"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_weight(weight, from_unit, to_unit)
    return render_template("weight.html", result=result)

@app.route("/convert_speed", methods=["POST"])
def convert_speed_route():
    speed = float(request.form["speed"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_speed(speed, from_unit, to_unit)
    return render_template("speed.html", result=result)

@app.route("/convert_time", methods=["POST"])
def convert_time_route():
    time = float(request.form["time"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_time(time, from_unit, to_unit)
    return render_template("time.html", result=result)

@app.route("/convert_area", methods=["POST"])
def convert_area_route():
    area = float(request.form["area"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_area(area, from_unit, to_unit)
    return render_template("area.html", result=result)

@app.route("/convert_volume", methods=["POST"])
def convert_volume_route():
    volume = float(request.form["volume"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_volume(volume, from_unit, to_unit)
    return render_template("volume.html", result=result)

@app.route("/convert_data", methods=["POST"])
def convert_data_route():
    value = float(request.form["data"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_data(value, from_unit, to_unit)
    return render_template("data.html", result=result)

@app.route("/convert_calorie", methods=["POST"])
def convert_calorie_route():
    amount = float(request.form["amount"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_calorie(amount, from_unit, to_unit)
    return render_template("calorie.html", result=result)

@app.route("/convert_frequency", methods=["POST"])
def convert_frequency_route():
    amount = float(request.form["amount"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_frequency(amount, from_unit, to_unit)
    return render_template("frequency.html", result=result)

@app.route("/convert_angle", methods=["POST"])
def convert_angle_route():
    value = float(request.form["angle"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_angle(value, from_unit, to_unit)
    return render_template("angle.html", result=result)

@app.route("/convert_power", methods=["POST"])
def convert_power_route():
    value = float(request.form["power"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_power(value, from_unit, to_unit)
    return render_template("power.html", result=result)

@app.route("/convert_pressure", methods=["POST"])
def convert_pressure_route():
    value = float(request.form["pressure"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    result = convert_pressure(value, from_unit, to_unit)
    return render_template("pressure.html", result=result)

@app.route("/density")
def density():
    return render_template("density.html")

# Route to process density conversion
@app.route("/convert_density", methods=["POST"])
def convert_density_route():
        value = float(request.form["density"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_density(value, from_unit, to_unit)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
