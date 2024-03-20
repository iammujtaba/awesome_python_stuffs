import typesense

client = typesense.Client({
  'api_key': 'Hu52dwsas2AdxdE',
  'nodes': [{
    'host': 'localhost',
    'port': '8108',
    'protocol': 'http'
  }],
  'connection_timeout_seconds': 2
})

create_collection = client.collections.create({
  "name": "mutual_funds",
  "fields": [
    {"name": "schemeCode", "type": "string" },
    {"name": "schemeName", "type": "string" },
  ],
  "default_sorting_field": "num_employees"
})