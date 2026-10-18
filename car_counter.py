class CarCounter:
    """YOLO tracking ID'leri üzerinden geçen araçları bir kez sayar."""

    def __init__(self):
        self.counted_ids = set()

    def update(self, detections):
        """
        detections örneği:
        [
            {"track_id": 1, "class_name": "car", "crossed_line": True},
            {"track_id": 2, "class_name": "truck", "crossed_line": True},
        ]
        """
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
