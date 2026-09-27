import logging
from pathlib import Path
import pandas as pd

logger = logging.getLogger(__name__)

def create_overview_report(data: pd.DataFrame) -> pd.DataFrame:

    total_sales = data["discounted_value"].sum()
    number_of_orders = data["order_id"].nunique()
    number_of_returns = data["returned"].sum()

    return pd.DataFrame(
        {
            "total_sales": [total_sales],
            "number_of_orders": [number_of_orders],
            "number_of_returns": [number_of_returns],
        }
    )

def create_category_report(data: pd.DataFrame) -> pd.DataFrame:

    return (
        data.groupby("product_category")
        .agg(
            total_sales=("discounted_value", "sum"),
            number_of_orders=("order_id", "nunique"),
        )
        .reset_index()
    )

def create_region_report(data: pd.DataFrame) -> pd.DataFrame:

    return (
        data.groupby("region")
        .agg(
            total_sales=("discounted_value", "sum"),
            number_of_orders=("order_id", "nunique"),
        )
        .reset_index()
    )

def save_report(report: pd.DataFrame, output_path: Path) -> None:

    output_path.parent.mkdir(parents=True, exist_ok=True)

    report.to_csv(output_path, index=False)

    logger.info("Rapport sparad %s", output_path)