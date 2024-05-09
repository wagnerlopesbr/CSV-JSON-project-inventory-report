from typing import List
from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory import Inventory


def process_report_request(file_paths: List[str], report_type: str) -> str:
    if report_type not in ["simple", "complete"]:
        raise ValueError("Report type is invalid.")

    # List comprehension to create a list of Inventory objects
    inventories = [
        # FROM BACK TO FRONT (5 to 1)
        Inventory(
            # 3-> ...then uses "JsonImporter"...
            JsonImporter(file_path).import_data()
            # 2 -> ...if the "file_path" ends with ".json"...
            if file_path.endswith(".json")
            # 1 -> ...otherwise uses "CsvImporter"
            else CsvImporter(file_path).import_data()
        )
        # 4 -> ...Iterates each "file_path" in "file_paths" list...
        for file_path in file_paths
        # 5 -> Filters file paths that ends with ".json" or ".csv"...
        if file_path.endswith((".json", ".csv"))
    ]

    # Instantiate the report object based on the report type
    report = SimpleReport() if report_type == "simple" else CompleteReport()

    # List comprehension to add the inventories to the report
    [report.add_inventory(inventory) for inventory in inventories]

    # Uses the "generate" (from SimpleReport/CompleteReport) method
    return report.generate()
