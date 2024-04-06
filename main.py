from typing import Union
from fastapi import FastAPI
import clickhouse_connect


app = FastAPI()
client = clickhouse_connect.get_client(host='localhost',database='default')

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/mf/{scheme_name}")
def read_item(scheme_name: str):
    print("scheme_name",scheme_name)
    # result = client.query(f"SELECT * FROM mf WHERE scheme_name ILIKE '%{scheme_name}%' limit 10;").result_rows
    # result = client.query(f"SELECT * FROM mf WHERE multiSearchAny(lower(scheme_name),{scheme_name.split()}) limit 10;").result_rows
    splitted_scheme_name = scheme_name.split()
        # hasToken(lower(scheme_name), 'avx') AND hasToken(lower(scheme_name), 'sve');
    # hastoken_statement = f"SELECT * FROM mf WHERE"
    # for name in splitted_scheme_name:
    #     hastoken_statement += f" hasToken(lower(scheme_name), '{name}') AND"
    # hastoken_statement = hastoken_statement[:-3]
    # print("hastoken_statement",hastoken_statement)
    # result = client.query(hastoken_statement).result_rows

    sql_ilike_and_statement = f"SELECT * FROM mf WHERE"
    for name in splitted_scheme_name:
        sql_ilike_and_statement += f" scheme_name ILIKE '%{name}%' AND"
    sql_ilike_and_statement = sql_ilike_and_statement[:-3]
    print("sql_ilike_and_statement",sql_ilike_and_statement)
    result = client.query(sql_ilike_and_statement).result_rows
    print(client.query("explain "+sql_ilike_and_statement).result_rows)
    return result