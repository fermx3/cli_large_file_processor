import csv
from pathlib import Path
from random import choice, randint

filepath = Path("data") / "sample.csv"
filepath.parent.mkdir(parents=True, exist_ok=True)

departments = ("Engineering", "Marketing", "Sales", "HR", "Finance")

with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
    docwriter = csv.writer(csvfile)
    docwriter.writerow(["id", "name", "age", "department", "salary", "active"])

    for row_id in range(1, 100_001):
        name = f"user_{row_id}{randint(0,100_000)}"
        age = randint(18, 60)
        department = choice(departments)
        salary = randint(500, 1200)
        active = choice((True, False))
        docwriter.writerow([row_id, name, age, department, salary, active])
