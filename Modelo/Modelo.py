import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import accuracy_score

pd.set_option('display.max_columns', None)
warnings.filterwarnings('ignore')

file_url = 'https://raw.githubusercontent.com/Anthony1078/PROYECTO_ADSP/master/Dataset/Data_Set_Ventas_Mangas.xlsx'
data = pd.read_excel(file_url)

VARIABLES = ['Fecha_venta', 'Cantidad_ventas', 'Categoría_producto'];
TARGET = ['Genero_cliente']

X = data[VARIABLES]
y = data[TARGET]

# Codificar las variables categóricas
X_encoded = pd.get_dummies(X)

# Mapear la variable objetivo a valores numéricos
y_mapped = data[TARGET]['Genero_cliente'].map({'MASCULINO': 0, 'FEMENINO': 1})

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_mapped, test_size=0.2, random_state=42)

model = xgb.XGBClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)