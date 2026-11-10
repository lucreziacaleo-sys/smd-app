"""ledger: balances and spending from a CSV file of transactions."""

import argparse
import csv
from collections import defaultdict
from decimal import Decimal


def read_transactions(path):
    """Reads the CSV file and returns one dict per row, with the amount as a Decimal."""
    with open(path, newline="") as f:
        transactions = list(csv.DictReader(f))
    for t in transactions:
        t["amount"] = Decimal(t["amount"])
    return transactions


def totals_by(transactions, column):
    """Adds up the amounts for each value of `column` (account, category...)."""
    totals = defaultdict(Decimal)
    for t in transactions:
        totals[t[column]] += t["amount"]
    return dict(totals)


def main() -> None:
    parser = argparse.ArgumentParser(prog="ledger", description=__doc__)
    parser.add_argument("command", choices=["balance", "spending"])
    parser.add_argument("file", nargs="?", default="data/transactions.csv")
    args = parser.parse_args()

    transactions = read_transactions(args.file)
    if args.command == "balance":
        for account, total in sorted(totals_by(transactions, "account").items()):
            print(f"{account:<10} {total:>10}")
    else:
        spending = [t for t in transactions if t["amount"] < 0 and t["category"] != "transfer"]
        for category, total in sorted(totals_by(spending, "category").items(), key=lambda item: item[1]):
            print(f"{category:<14} {total:>10}")


print(0.1 + 0.2)
print(Decimal("0.1") + Decimal("0.2"))



