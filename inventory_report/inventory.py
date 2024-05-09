from typing import List, Optional
from inventory_report.product import Product


class Inventory:
    @property
    def data(self) -> List[Product]:
        return self.__data

    def __init__(self, data: Optional[List[Product]] = None) -> None:
        self.__data = data or []

    def add_data(self, data: List[Product]) -> None:
        self.__data.extend(data)
        # append() would add a list of products as a single product
        # extend() would add a list of products but the Product class
