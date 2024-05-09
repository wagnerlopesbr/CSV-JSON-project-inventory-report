from datetime import datetime
from inventory_report.inventory import Inventory
from typing import List
from collections import Counter


class SimpleReport:
    def __init__(self) -> None:
        self.inventories: List[Inventory] = []

    def find_oldest_manufacturing_date(self) -> str:
        # List comprehension to get all manufacturing dates
        manufacturing_dates = [
            datetime.strptime(product.manufacturing_date, "%Y-%m-%d")
            for inventory in self.inventories
            for product in inventory.data
        ]
        return min(manufacturing_dates).strftime("%Y-%m-%d")

    def find_closest_expiration_date(self) -> str:
        # List comprehension to get all expiration dates
        current_date = datetime.now()
        closest_expiration_dates = [
            datetime.strptime(product.expiration_date, "%Y-%m-%d")
            for inventory in self.inventories
            for product in inventory.data
            if datetime.strptime(
                product.expiration_date, "%Y-%m-%d"
            ) > current_date
        ]
        return min(closest_expiration_dates).strftime("%Y-%m-%d")

    def find_largest_inventory_company(self) -> str:
        # Counter to get the company with the largest inventory
        inventory_co_counter = Counter(
            product.company_name
            for inventory in self.inventories
            for product in inventory.data
        )
        return max(inventory_co_counter, key=inventory_co_counter.get)

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        oldest_manufacturing_date = self.find_oldest_manufacturing_date()
        closest_expiration_date = self.find_closest_expiration_date()
        largest_inventory_co = self.find_largest_inventory_company()
        return (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {largest_inventory_co}"
        )
