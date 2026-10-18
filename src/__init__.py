class CarCounter:
    """YOLO araç takip sonuçlarından toplam araba sayısını tutar."""

    def __init__(self):
        self.counted_ids = set()

    def update(self, detections):
        for detection in detections:
            class_name = detection.get("class_name", "").lower()
            track_id = detection.get("track_id")
            crossed_line = detection.get("crossed_line", False)

            if (
                class_name == "car"
                and track_id is not None
                and crossed_line
            ):
                self.counted_ids.add(track_id)

        return len(self.counted_ids)
