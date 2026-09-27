import pandas as pd

from order_report.processing import process_orders

def test_order_value_is_calculated_correctly():

    data = pd.DataFrame(
        {
            "region": ["North"],
            "product_category": ["Electronics"],
            "quantity": [2],
            "unit_price": [100],
            "discount": [0],
            "returned": [False],
        }
    )

    result = process_orders(data)

    assert result.loc[0, "order_value"] == 200


def test_discounted_value_is_calculated_correctly():

    data = pd.DataFrame(
        {
            "region": ["North"],
            "product_category": ["Electronics"],
            "quantity": [2],
            "unit_price": [100],
            "discount": [0.10],
            "returned": [False],
        }
    )

    result = process_orders(data)

    assert result.loc[0, "order_value"] == 200
    assert result.loc[0, "discounted_value"] == 180