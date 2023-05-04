from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

query = """
        SELECT * FROM `elastic-bi.certified_data.pipeline_bookings` limit 10
        """
run_query = client.query(query)

print("The query data:")
for row in run_query:
    print(row)