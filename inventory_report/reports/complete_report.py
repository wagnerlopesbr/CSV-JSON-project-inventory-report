from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def find_stocked_products_by_company(self) -> Counter[str]:
        company_names = [
            product.company_name
            for inventory in self.inventories
            for product in inventory.data
        ]
        return Counter(company_names)

    def generate(self) -> str:
        oldest_manufacturing_date = self.find_oldest_manufacturing_date()
        closest_expiration_date = self.find_closest_expiration_date()
        largest_inventory_co = self.find_largest_inventory_company()
        stocked_products_by_company = self.find_stocked_products_by_company()

        output = (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {largest_inventory_co}\n"
            f"Stocked products by company:\n"
        )

        for company, count in stocked_products_by_company.items():
            output += f"- {company}: {count}\n"

        return output
