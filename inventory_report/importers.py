from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json
import csv


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as f:
            return [Product(**product) for product in json.load(f)]


class CsvImporter(Importer):
    # commented code does the same as the return line inside the "with" block
    def import_data(self) -> List[Product]:
        # products = []
        with open(self.path, "r", newline="") as f:
            return [Product(**product) for product in csv.DictReader(f)]
        #     reader = csv.DictReader(f)
        #     for row in reader:
        #         product = Product(
        #             id=row["id"],
        #             product_name=row["product_name"],
        #             company_name=row["company_name"],
        #             manufacturing_date=row["manufacturing_date"],
        #             expiration_date=row["expiration_date"],
        #             serial_number=row["serial_number"],
        #             storage_instructions=row["storage_instructions"]
        #         )
        #         products.append(product)
        # return products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
