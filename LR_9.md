```python
from sqlalchemy import select

with engine.connect() as connection:

statement = select(students_table)

result = connection.execute(statement)

for row in result:

print(row.id, row.name, row.is_active)

statement_2 = select(students_table.c.name, students_table.c.gpa)

result_2 = connection.execute(statement_2)

for row in result_2:

print(row.name, row.gpa)
```

```python
import json

from sqlalchemy import (

create_engine, MetaData, Table, Column,

Integer, String, Float, Boolean, ForeignKey, insert

)

with open("catalog.json", "r", encoding="utf-8") as file:

	itms = json.load(file)

engine = create_engine("sqlite:///database_1.db")

metadata = MetaData()

category = Table(
"category", metadata,
Column("id", Integer, primary_key=True),
Column("name", String(100), nullable=False, unique=True),
Column("description", String(255)),
)

product = Table(
	"product", metadata,
	Column("id", Integer, primary_key=True),
	Column("product_name", String(100), nullable=False),
	Column("price", Float),
	Column("category_id", Integer, ForeignKey("category.id"), nullable=False),
	)
metadata.create_all(engine)
with engine.begin() as conn:
	cat_id = {}

for itm in itms:
	cat = itm["category"]
	cat_name = cat["name"]

	if cat_name not in cat_id:
		result = conn.execute(
			insert(category).values(
			name=cat_name,
			description=cat["description"]
			)
		)
cat_id[cat_name] = result.inserted_primary_key[0]
conn.execute(
	insert(product).values(
	product_name=itm["product_name"],
	price=itm["price"],
	category_id=cat_id[cat_name],
	)
)
```