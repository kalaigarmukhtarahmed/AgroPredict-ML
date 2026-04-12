def run_predefined_tests(model):
    test_cases = [
        [25, 1200, 80, 6.5, "rice"],
        [30, 500, 60, 6.0, "wheat"],
        [28, 700, 65, 6.2, "maize"]
    ]

    results = []

    for case in test_cases:
        temp, rain, hum, ph, user_crop = case
        pred = model.predict([[temp, rain, hum, ph]])[0]

        if user_crop == pred:
            res = "Suitable"
        else:
            res = "Not Suitable"

        results.append({
            "input": case,
            "predicted": pred,
            "result": res
        })

    return results