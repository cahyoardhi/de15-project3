from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv('./source/users_w_postal_code.csv', sep=',')
engine = create_engine('postgresql://postgres:digitalskola@127.0.0.1:5432/postgres')
df.to_sql('from_file_table', engine)
df_read = pd.read_sql('SELECT * FROM from_file_table', engine)
print(df_read)