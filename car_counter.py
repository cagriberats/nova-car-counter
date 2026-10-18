def count_cars(detections):
    """
    YOLO tespitleri arasından araba sınıfını sayar.
    detections: Her tespit için class_name bilgisi içeren liste.
    """
    car_count = 0

    for detection in detections:
        class_name = detection.get("class_name", "").lower()

        if class_name == "car":
            car_count += 1

    return car_count
