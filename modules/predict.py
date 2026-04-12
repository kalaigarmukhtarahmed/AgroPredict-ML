def predict_crop(model, temp, rain, hum, ph):
    try:
        features = [[float(temp), float(rain), float(hum), float(ph)]]
        prediction = model.predict(features)[0]
        return prediction
    except:
        return "Error"