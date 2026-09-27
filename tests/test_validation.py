import pandas as pd
import pytest

from order_report.validation import validate_columns

def test_missing_required_column_raises_error():

    data = pd.DataFrame(
        {
        "order_id": [1],
        "region": ["North"],
        }
    )

    with pytest.raises(ValueError):
        validate_columns(data)