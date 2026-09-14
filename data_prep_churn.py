import os
import shutil
import pandas as pd
import kagglehub

# 1. Rutas locales
repo_data_dir = "data"
os.makedirs(repo_data_dir, exist_ok=True)

raw_excel_path = os.path.join(repo_data_dir, "raw_ecommerce_churn.xlsx")
clean_csv_path = os.path.join(repo_data_dir, "clean_ecommerce_churn.csv")

# 2. Descargar si no existe
if not os.path.exists(raw_excel_path):
    print("-> Descargando dataset desde Kaggle...")
    download_path = kagglehub.dataset_download("ankitverma2010/ecommerce-customer-churn-analysis-and-prediction")
    
    downloaded_files = os.listdir(download_path)
    excel_file = [f for f in downloaded_files if f.endswith('.xlsx') or f.endswith('.xls')][0]
    cache_file_path = os.path.join(download_path, excel_file)
    
    shutil.copy(cache_file_path, raw_excel_path)
    print(f"-> Dataset ORIGINAL guardado en: '{raw_excel_path}'")
else:
    print(f"-> El dataset original ya existe en: '{raw_excel_path}'")

# 3. Cargar la hoja 'E Commerce Dataset' (Índice 1)
df_original = pd.read_excel(raw_excel_path, sheet_name=1)

# 4. Proceso de Limpieza (Módulo 1)
df = df_original.copy()

# A. Normalización de columnas a Snake Case
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# B. Eliminar duplicados
df = df.drop_duplicates()

# C. Limpieza de espacios en columnas de texto
string_columns = df.select_dtypes(include=['object', 'str']).columns
for col in string_columns:
    df[col] = df[col].astype(str).str.strip()

# D. Imputación de valores nulos con la mediana
num_cols_with_nulls = df.select_dtypes(include=['float64', 'int64']).columns[df.select_dtypes(include=['float64', 'int64']).isnull().any()]
for col in num_cols_with_nulls:
    df[col] = df[col].fillna(df[col].median())

# E. Casteo de variables numéricas discretas a enteros
for col in ['tenure', 'warehouse_to_home', 'day_since_last_order', 'hour_spend_on_app', 'number_of_device_registered', 'number_of_address', 'coupon_used', 'order_count']:
    if col in df.columns:
        df[col] = df[col].astype(int)

# 5. Exportar CSV limpio
df.to_csv(clean_csv_path, index=False)
print(f"-> Dataset LIMPIO guardado exitosamente en: '{clean_csv_path}'")
print(f"Dimensiones del dataset limpio: {df.shape[0]} filas, {df.shape[1]} columnas")