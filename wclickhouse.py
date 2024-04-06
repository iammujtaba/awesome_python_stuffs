import clickhouse_connect
from datetime import datetime
import pandas as pd

client = clickhouse_connect.get_client(host='localhost',database='default')
client.command("CREATE TABLE IF NOT EXISTS mf (created_at DateTime,updated_at DateTime,wschemecode String,isin String,scheme_code String,scheme_name String,display_name String) ENGINE = MergeTree() ORDER BY created_at;")

path = "/Users/programmer/Downloads/mutual_funds.csv"
data = pd.read_csv(path)
data.dropna(inplace=True)
data = data.to_dict(orient="records")
for d in data:
    d['created_at'] = datetime.strptime(d['created_at'].split("T")[0],"%Y-%m-%d")
    d['updated_at'] = datetime.strptime(d['updated_at'].split("T")[0],"%Y-%m-%d")

columns = list(d.keys())
for d in data:
    client.insert("mf",data=[list(d.values())],column_names=columns)

    # client.insert("mf",data=data,column_names=columns)

# search for a scheme name
scheme_name = "Axis"
client.query(f"SELECT * FROM mf WHERE scheme_name LIKE '%{scheme_name}%' limit 10;").result_rows
client.query("SET allow_experimental_inverted_index = true;")
client.query("ALTER TABLE mf ADD INDEX scheme_name_lowercase(lower(scheme_name)) TYPE inverted;")
client.query(f"ALTER TABLE mf MATERIALIZE INDEX scheme_name_lowercase;")
