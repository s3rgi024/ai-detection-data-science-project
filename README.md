# 🛒 E-Commerce Customer Churn & UX Analytics

Este repositorio contiene el desarrollo del **Proyecto Final de Ciencia de Datos**, enfocado en la exploración, limpieza y análisis de la tasa de cancelación de usuarios (*Churn*) en plataformas de comercio electrónico.

---

## 🎯 Objetivo del Proyecto

Analizar el comportamiento y la satisfacción de los usuarios en una plataforma digital de E-Commerce mediante técnicas de analítica de datos[cite: 1]. El objetivo es identificar las causas operativas, de usabilidad (UX) y de servicio que motivan la pérdida de clientes, proporcionando información clave para la toma de decisiones estratégicas de retención[cite: 1, 2].

### 💻 Conexión con la Ingeniería de Sistemas
En el ecosistema del desarrollo de software y servicios SaaS, la construcción de plataformas digitales no concluye con el despliegue del código[cite: 1]. Comprender los patrones de comportamiento de los usuarios permite a los ingenieros proponer optimizaciones en la arquitectura del sistema, diseñar alertas automáticas de insatisfacción y mejorar la experiencia de usuario (UX)[cite: 1].

---

## 📚 Estructura de la Ruta de Aprendizaje

El proyecto está estructurado en tres módulos de ejecución[cite: 1, 2]:

* **Módulo 1 — Fundamentos y Preparación de Datos (Fase Actual):** Selección de la fuente cruda, exploración de variables, sanitización de textos, imputación de nulos y casteo de tipos numéricos[cite: 1, 2].
* **Módulo 2 — Estadística Descriptiva y Preprocesamiento:** Análisis exploratorio (EDA), evaluación de correlaciones entre variables y detección de patrones de insatisfacción[cite: 1, 2].
* **Módulo 3 — Modelado, Storytelling y Toma de Decisiones:** Presentación de hallazgos analíticos y formulación de estrategias orientadas al producto digital[cite: 1, 2].

---

## 📊 Dataset Utilizado

* **Nombre:** E-Commerce Customer Churn Analysis and Prediction[cite: 1]
* **Fuente:** Kaggle (Creado por *Ankit Verma*)[cite: 1]
* **Registros:** 5,630 clientes y 20 variables de estudio[cite: 1]
* **Variables Clave:** `CustomerID`, `Churn`, `Tenure`, `PreferredLoginDevice`, `SatisfactionScore`, `WarehouseToHome`, `Complain`, entre otras[cite: 1].

---

## 🛠️ Pipeline de Limpieza Aplicado (Módulo 1)

El script de preprocesamiento `data_prep_churn.py` ejecuta automáticamente las siguientes fases de depuración[cite: 1]:

1. **Estandarización de Encabezados:** Conversión de nombres de columnas a formato *Snake Case* (ej. `PreferredLoginDevice` $\rightarrow$ `preferred_login_device`)[cite: 1].
2. **Eliminación de Redundancias:** Verificación e inspección de registros duplicados[cite: 1].
3. **Sanitización de Cadenas:** Eliminación de espacios en blanco residuales al inicio y final de campos de texto (`.str.strip()`)[cite: 1].
4. **Tratamiento de Nulos:** Imputación de valores faltantes en variables numéricas utilizando la mediana estandarizada[cite: 1].
5. **Casteo de Tipos Discretos:** Conversión de métricas enteras a `int` (ej. `tenure`, `day_since_last_order`)[cite: 1].

---

## 📁 Estructura del Repositorio

```text
ecommerce-customer-churn/
│
├── data/
│   ├── raw_ecommerce_churn.xlsx     # Dataset original crudo descargado de Kaggle[cite: 1]
│   └── clean_ecommerce_churn.csv   # Dataset depurado listo para el Módulo 2[cite: 1, 2]
│
├── data_prep_churn.py               # Script automatizado de descarga y limpieza (Módulo 1)[cite: 1]
└── README.md                        # Documentación general del proyecto[cite: 1]