
import logging
from pathlib import Path
import pandas as pd

logger = logging.getLogger(__name__)


def create_overview_report(data: pd.DataFrame) -> pd.DataFrame:

    total_sales = round(data["discounted_value"].sum(), 2)
    number_of_orders = data["order_id"].nunique()
    number_of_returns = int(data["returned"].sum())

    return pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                total_sales,
                number_of_orders,
                number_of_returns,
            ],
        }
    )


def create_category_report(data: pd.DataFrame) -> pd.DataFrame:

    report = (
        data.groupby("product_category", as_index=False)
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

    report["total_sales"] = report["total_sales"].round(2)
    report["return_rate"] = (
        report["returns"] / report["order_count"]
    ).round(3)

    return report.sort_values(
        "total_sales", ascending=False
    ).reset_index(drop=True)


def create_region_report(data: pd.DataFrame) -> pd.DataFrame:

    report = (
        data.groupby("region", as_index=False)
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

    report["total_sales"] = report["total_sales"].round(2)
    report["return_rate"] = (
        report["returns"] / report["order_count"]
    ).round(3)

    return report.sort_values(
        "total_sales", ascending=False
    ).reset_index(drop=True)


def create_returns_by_category_report(
    data: pd.DataFrame,
) -> pd.DataFrame:

    report = (
        data.groupby("product_category", as_index=False)
        .agg(
            order_count=("order_id", "nunique"),
            returns=("returned", "sum"),
        )
    )

    report["return_rate"] = (
        report["returns"] / report["order_count"]
    ).round(3)

    return report.sort_values(
        "return_rate", ascending=False
    ).reset_index(drop=True)


def save_report(report: pd.DataFrame, output_path: Path) -> None:

    output_path.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(output_path, index=False)
    logger.info("Rapport sparad: %s", output_path)
