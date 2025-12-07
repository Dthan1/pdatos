import pandas as pd
from deltalake import DeltaTable, write_deltalake
from configparser import ConfigParser
from pprint import pprint

#---- Configuracion de parser

parser = ConfigParser()                                             # Sirve para entrar a pipeline.conf y sacar las credenciales de ahi
parser.optionxform = str
parser.read("pipeline.conf")

storage_options = dict(parser["mysql-db"])
bkt_name = storage_options["bkt_name"]

#---- Lectura de Delta y convertido en dataframe

bronze_dir = f"s3://{bkt_name}/datalake/bronze/riotgames_api"
statsBronze_dir = f"{bronze_dir}/registroSebastian"

silver_dir = f"s3://{bkt_name}/datalake/silver/riotgames_api"
statsSilver_dir = f"{silver_dir}/registroSebastian"

dt_bronze = DeltaTable(statsBronze_dir, storage_options=storage_options)

df = dt_bronze.to_pandas()
#print(df.dtypes)

#---- 1era Transformacion borrar las partidas no interesantes, que en este caso son las que no tienen linea definida por lo que no son en grieta

basura = ["NONE", "nan", "null", "NA", ""]
df = df[~df["lane"].isin(basura)]

print(df.info(verbose=True, show_counts=True, memory_usage= 'deep'))

'''
print(df.isnull().sum())
filas_con_nulos = df[df.isnull().any(axis=1)]

print(filas_con_nulos)
'''