import pandas as pd

# 1. Cargar ambos datasets desde la carpeta data/
df_raw = pd.read_csv("data/raw_ai_essay_submissions.csv")
df_clean = pd.read_csv("data/ai_essay_submissions_clean.csv")

print("=== 1. COMPARACIÓN DE DIMENSIONES (FILAS Y COLUMNAS) ===")
print(f"Original: {df_raw.shape[0]} filas, {df_raw.shape[1]} columnas")
print(f"Limpio:   {df_clean.shape[0]} filas, {df_clean.shape[1]} columnas")
print(f"Diferencia de filas (duplicados eliminados): {df_raw.shape[0] - df_clean.shape[0]}")

print("\n=== 2. COMPARACIÓN DE TIPOS DE DATOS (DTYPES) ===")
df_types = pd.DataFrame({
    'Columna': df_raw.columns,
    'Tipo Original': df_raw.dtypes.values,
    'Tipo Limpio': df_clean.dtypes.values
})
print(df_types)

print("\n=== 3. VERIFICACIÓN DE REDONDEO DE DECIMALES ===")
print("Original (primeras 3 notas):")
print(df_raw['grade'].head(3).tolist())
print("Limpio (primeras 3 notas):")
print(df_clean['grade'].head(3).tolist())

print("\n=== 4. VERIFICACIÓN DE CASTEO (word_count a INT) ===")
print(f"Original word_count dtype: {df_raw['word_count'].dtype}")
print(f"Limpio word_count dtype:   {df_clean['word_count'].dtype}")

print("\n=== 5. INTEGRIDAD Y VALORES NULOS ===")
print(f"Nulos en dataset original: {df_raw.isnull().sum().sum()}")
print(f"Nulos en dataset limpio:   {df_clean.isnull().sum().sum()}")