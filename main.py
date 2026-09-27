import logging

from order_report.config import CONFIG
from order_report.loading import load_orders
from order_report.validation import validate_columns
from order_report.processing import process_orders
from order_report.reporting import (
    create_overview_report,
    create_category_report,
    create_region_report,
    save_report, 
)

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s"
    )

    data = load_orders(CONFIG.input_path)

    validate_columns(data)

    print("Valideringen lyckades!")

    data = process_orders(data)

    overview = create_overview_report(data)
    category_report = create_category_report(data)
    region_report = create_region_report(data)

    save_report(
        overview, 
        CONFIG.output_dir / "overview.csv"
    )

    save_report(
        category_report,
        CONFIG.output_dir / "category_report.csv"
    )

    save_report(
        region_report,
        CONFIG.output_dir / "region_report.csv"
    )

    #print("\nÖversikt:")
    #print(overview)

    #print("\nFörsäljning per kategori:")
    #print(category_report)

    #print("\nFörsäljning per region:")
    #print(region_report)
    #print(data[["order_id", "quantity", "unit_price", "discount", "order_value", "discounted_value"]].head())
    #print(data.head())

if __name__ == "__main__":
    main()