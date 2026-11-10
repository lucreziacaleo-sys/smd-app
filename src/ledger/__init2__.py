from rich.console import Console
from rich.table import Table

table = Table(title="Spending by category")
table.add_column("Category")
table.add_column("EUR", justify="right")

for category, total in sorted(totals_by(spending, "category").items(), key=lambda item: item[1]):
            table.add_row(category, f"{-total:,.2f}")
            Console().print(table)