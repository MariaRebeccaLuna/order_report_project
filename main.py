
import logging

from order_report.config import CONFIG
from order_report.loading import load_orders
from order_report.validation import validate_columns
from order_report.processing import process_orders
from order_report.reporting import (
    create_overview_report,
    create_category_report,
    create_region_report,
    create_returns_by_category_report,
    save_report,
)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    data = load_orders(CONFIG.input_path)
    validate_columns(data)
    data = process_orders(data)

    overview = create_overview_report(data)
    category_report = create_category_report(data)
    region_report = create_region_report(data)
    returns_report = create_returns_by_category_report(data)

    save_report(
        overview,
        CONFIG.output_dir / "overview.csv",
    )
    save_report(
        category_report,
        CONFIG.output_dir / "sales_by_category.csv",
    )
    save_report(
        region_report,
        CONFIG.output_dir / "sales_by_region.csv",
    )
    save_report(
        returns_report,
        CONFIG.output_dir / "returns_by_category.csv",
    )


if __name__ == "__main__":
    main()
