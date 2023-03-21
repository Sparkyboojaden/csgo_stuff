import psycopg2
from sqlalchemy import create_engine, BigInteger, Float, Boolean, Text, DateTime
from config import pg_host, pg_db, pg_user, pg_pass
import numpy as np
import pandas as pd

#takes dataframe, 
def update_table(df,table_name):
    conn = psycopg2.connect(
        host= pg_host,
        database=pg_db,
        user=pg_user,
        password=pg_pass
    )

    engine = create_engine('postgresql://'+pg_user+':'+pg_pass+'@'+pg_host+':5432/'+pg_db+'')

    dtype_map = {
        np.dtype('int64'): BigInteger(),
        np.dtype('float64'): Float(),
        np.dtype('datetime64[ns]'): DateTime(),
        np.dtype('bool'): Boolean(),
        np.dtype('object'): Text(),
    }

    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')

    # insert data into the table
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False, dtype=dtype_map)