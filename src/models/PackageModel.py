import json


class PackageModel:
    @classmethod
    def schema_json(cls, *args, **kwargs):
        schema = {
            "title": "PackageModel",
            "type": "object",
            "properties": {}
        }
        return json.dumps(
            schema,
            indent=kwargs.get("indent"),
        )

    def __init__(self, *args, **kwargs):
        pass
