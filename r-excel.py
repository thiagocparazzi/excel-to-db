#pip install xlrd
#pip install pandas
#python -m pip install pymongo

import pandas as pd
from pymongo import MongoClient

#lendo uma planilha do excel com python
df = pd.read_excel(r'D:\Dados\Downloads\IncompletocontratoLOAABYZ.xlsx')

#print(df)

#conectando com o banco de dados MongoDB Atlas
client = MongoClient(r'mongodb+srv://nickinho:nickinho@cluster0-1azlf.mongodb.net/test?retryWrites=true&w=majority')
db = client.cluster0

collection = db['CFTS-LOAABYZ']

collection.insert_many(df.to_dict('records'))


#transforma novamente em dataframe
df = pd.DataFrame(list(collection.find({ }, { 'WORKNUMBER': '1'})))
print(df)