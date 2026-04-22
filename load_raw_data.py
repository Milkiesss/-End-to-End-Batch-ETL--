# Импортируем необходимые библиотеки
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

print(os.getenv("POSTGRES_USER"), os.getenv("POSTGRES_PORT"))

engine = create_engine(
     f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)
 

# Получаем абсолютный путь к папке с исходными данными
# os.path.dirname(__file__) — текущая директория скрипта
# Затем добавляем подпапки "data" и "raw"
# Результат: например, "C:\Study\End-to-End Batch ETL-пайплайн\data\raw"
raw_data_path = os.path.join(os.path.dirname(__file__), "data", "raw")

# Проходим по всем файлам в папке с исходными данными

for filename in os.listdir(raw_data_path):
    if filename.endswith(".csv"):
        table_name = filename.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '')
        
        filepath = os.path.join(raw_data_path, filename)
        print(f"Загружаем {filename} в таблицу {table_name}...")

        df = pd.read_csv(filepath, encoding="utf-8")
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"{filename} успешно загружен в таблицу {table_name}.")
        
print("Все файлы успешно загружены.")

