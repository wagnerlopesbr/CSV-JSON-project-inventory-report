from typing import List, Optional
from inventory_report.product import Product


class Inventory:
    @property
    def data(self) -> List[Product]:
        return self.__data

    def __init__(self, data: Optional[List[Product]] = None) -> None:
        self.__data = data or []

    def add_data(self, product: Product) -> None:
        self.__data.append(product)
        # append() would add a list of products as a single product
        # extend() would add a list of products but the Product class
        #   would have to be iterable (which it isn't) and I can't change it
