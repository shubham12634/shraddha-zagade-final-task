import re
from typing import Any, Dict


class JsonPreprocessor:
    """
    A utility class for preprocessing JSON-like Python objects.

    Provides methods to:
    - Normalize dictionary keys
    - Remove null (None) values
    """

    def normalize_keys(self, json_obj: Any) -> Any:
        """
        Normalize all dictionary keys in a JSON-like object.

        Rules:
        - Convert keys to strings
        - Strip spaces
        - Convert to lowercase
        - Replace spaces and hyphens with underscores
        - Collapse multiple underscores

        Works recursively on dicts and lists.
        """
        def _normalize_key(key: Any) -> str:
            key_str = str(key).strip().lower()
            key_str = re.sub(r"[ -]+", "_", key_str)
            key_str = re.sub(r"_+", "_", key_str)
            return key_str

        if isinstance(json_obj, dict):
            normalized: Dict[str, Any] = {}
            for key, value in json_obj.items():
                normalized[_normalize_key(key)] = self.normalize_keys(value)
            return normalized

        if isinstance(json_obj, list):
            return [self.normalize_keys(item) for item in json_obj]

        return json_obj

    def strip_nulls(self, json_obj: Any) -> Any:
        """
        Remove all None (null) values from a JSON-like object.

        Works recursively on dicts and lists.
        """
        if isinstance(json_obj, dict):
            cleaned: Dict[Any, Any] = {}
            for key, value in json_obj.items():
                if value is not None:
                    cleaned[key] = self.strip_nulls(value)
            return cleaned

        if isinstance(json_obj, list):
            return [self.strip_nulls(item) for item in json_obj if item is not None]

        return json_obj


# ---------- Input JSON defined here ----------
data = {
    " User Name ": "Alice",
    "Age": None,
    "Phone-Number": "12345",
    "Details": {
        "City Name": "NY",
        "Zip": None
    },
    "Tags": [None, "Admin", "User"]
}

# ---------- Processing ----------
processor = JsonPreprocessor()
result = processor.strip_nulls(processor.normalize_keys(data))

# ---------- Output ----------
print(result)
