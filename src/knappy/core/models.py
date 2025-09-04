import csv
from pydantic import (
    BaseModel,
    ValidationError,
)


class Items(BaseModel):
    # model_config = ConfigDict(strict=True)
    name: str
    value: int
    cost: float


def validate_items(csv_data: str):
    """
    Validates a JSON string containing a list of items.
    Returns a list of Items models on success, None on failure.
    """
    try:
        with open(csv_data) as f:
            reader = csv.DictReader(f)
            validated_data = [
                Items.model_validate(csv_data) for row in reader
            ]
        return validated_data
    except ValidationError as e:
        print(f"Data validation failed!\n{e}")
        return None
