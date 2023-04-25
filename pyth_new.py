from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "gcp-latha.dataset.py_tab"

schema = [
    bigquery.SchemaField("first_name", "STRING", mode="REQUIRED"),
	bigquery.SchemaField("second_name", "STRING", mode="REQUIRED"),
	bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
	bigquery.SchemaField("phone_number", "INTEGER", mode="REQUIRED"),
    #bigquery.SchemaField("pincode", "INTEGER", mode="REQUIRED"),
]

rows_to_insert=[('latha','kosuru',23,95180027),
                ('latha','kosuru',23,95180027)]
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
errors = client.insert_rows(table,rows_to_insert)
if errors==[]:
    print("Data inserted successfully")
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)




