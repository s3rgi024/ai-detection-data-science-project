import os
import shutil
import pandas as pd
import kagglehub

# 1. Definir rutas del repositorio local
repo_data_dir = "data"
os.makedirs(repo_data_dir, exist_ok=True)

raw_csv_path = os.path.join(repo_data_dir, "raw_ai_essay_submissions.csv")
clean_csv_path = os.path.join(repo_data_dir, "ai_essay_submissions_clean.csv")

# 2. Descargar el dataset usando kagglehub (si no se ha copiado aún a 'data/')
if not os.path.exists(raw_csv_path):
    print("-> Descargando dataset original desde Kaggle...")
    download_path = kagglehub.dataset_download("aliahmadmphil/student-cheating-networks-and-ai-detection-data")
    
    # Ruta del archivo descargado en la caché
    cache_file = os.path.join(download_path, "AI_Academic_Integrity_Dataset", "ai_essay_submissions.csv")
    
    # Copiar el archivo original directamente a la carpeta data/ de tu repositorio
    shutil.copy(cache_file, raw_csv_path)
    print(f"-> Dataset ORIGINAL guardado en el repo: '{raw_csv_path}'")
else:
    print(f"-> El dataset original ya existe en: '{raw_csv_path}'")

# 3. Cargar el dataset ORIGINAL desde la carpeta del repo
df_original = pd.read_csv(raw_csv_path)

# 4. Proceso de limpieza
df = df_original.copy()

df = df.drop_duplicates()
df['submission_date'] = pd.to_datetime(df['submission_date'])
df['grade'] = df['grade'].round(2)
df['ai_probability'] = df['ai_probability'].round(4)
df['similarity_score'] = df['similarity_score'].round(4)
df['word_count'] = df['word_count'].astype(int)
df['semester'] = df['semester'].str.strip()
df['assignment_type'] = df['assignment_type'].str.strip()

# 5. Guardar el dataset LIMPIO en la carpeta data/
df.to_csv(clean_csv_path, index=False)
print(f"-> Dataset LIMPIO guardado en el repo: '{clean_csv_path}'")
