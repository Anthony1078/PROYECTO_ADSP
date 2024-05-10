from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Cargar el modelo
modelo = joblib.load('modelo_xgboost.pkl')

# Inicializar la aplicación Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos del POST request en formato JSON
    data = request.json
    # Convertir a DataFrame para procesamiento
    df = pd.DataFrame([data])
    
    # Preprocesar datos si es necesario (codificación, transformaciones, etc.)

    # Realizar la predicción
    prediccion = modelo.predict(df)
    
    # Devolver el resultado como respuesta JSON
    return jsonify({'prediction': prediccion.tolist()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
