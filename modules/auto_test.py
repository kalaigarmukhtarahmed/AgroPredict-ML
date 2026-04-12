import random

def generate_auto_test(model):
    crops = ['rice', 'wheat', 'maize', 'coffee', 'cotton']

    temp = random.randint(20, 40)
    rain = random.randint(200, 1200)
    hum = random.randint(40, 90)
    ph = round(random.uniform(5, 8), 1)

    user_crop = random.choice(crops)

    predicted = model.predict([[temp, rain, hum, ph]])[0]

    if user_crop.lower() == predicted.lower():
        result = "✔ Suitable"
        suggestion = "Correct crop"
    else:
        result = "❌ Not Suitable"
        suggestion = f"Recommended Crop: {predicted}"

    return {
        "temp": temp,
        "rain": rain,
        "hum": hum,
        "ph": ph,
        "user_crop": user_crop,
        "prediction": predicted,
        "result": result,
        "suggestion": suggestion
    }