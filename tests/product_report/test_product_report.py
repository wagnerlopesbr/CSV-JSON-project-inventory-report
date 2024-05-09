from inventory_report.product import Product


def test_product_report() -> None:
    test_product = Product(
        id="1",
        product_name="Gabigol de Pelúcia",
        company_name="Flamengo",
        manufacturing_date="2024-05-09",
        expiration_date="2034-05-09",
        serial_number="123456",
        storage_instructions="Cuidar com carinho",
    )

    assert (
        str(test_product)
        == "The product 1 - Gabigol de Pelúcia with serial number 123456 " +
        "manufactured on 2024-05-09 by the company Flamengo " +
        "valid until 2034-05-09 must be stored according to " +
        "the following instructions: Cuidar com carinho."
    )
