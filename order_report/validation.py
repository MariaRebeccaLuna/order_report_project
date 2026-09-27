import logging
import pandas as pd

logger = logging.getLogger(__name__)

REQUIRED_COLUMNS = [
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "product_category",
    "quantity",
    "unit_price",
    "discount",
    "returned",
]

def validate_columns(data: pd.DataFrame) -> None:

    missing_columns = [
        column 
        for column in REQUIRED_COLUMNS
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Saknade obligatoriska kolumner: {missing_columns}"
        )

    logger.info("Validering av obligatoriska kolumner lyckades")