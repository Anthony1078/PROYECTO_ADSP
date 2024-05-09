import pandas as pd
import numpy as np
from datetime import datetime, timedelta

n_rows = 50000

# Generar fechas aleatorias
start_date = datetime.strptime('01-01-2020', '%d-%m-%Y')
end_date = datetime.strptime('31-12-2022', '%d-%m-%Y')
date_range = (end_date - start_date).days

np.random.seed(0)
dates = [start_date + timedelta(days=np.random.randint(0, date_range)) for _ in range(n_rows)]
dates.sort()

month_names = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO",
               "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]

seasons_dict = {
    1: "VERANO", 2: "VERANO", 3: "VERANO",
    4: "OTOÑO", 5: "OTOÑO", 6: "OTOÑO",
    7: "INVIERNO", 8: "INVIERNO", 9: "INVIERNO",
    10: "PRIMAVERA", 11: "PRIMAVERA", 12: "PRIMAVERA"
}

months = [month_names[date.month - 1] for date in dates]
seasons = [seasons_dict[date.month] for date in dates]
sales_counts = np.random.randint(1, 101, n_rows)
product_prices = np.random.uniform(10, 120, n_rows).round(2)

manga_names = {
    "Acción": [
        "One Punch Man", "Houseki no Kuni", "Vinland Saga", "Kingdom",
        "Fullmetal Alchemist", "Vagabond", "One Piece"
    ],
    "Ciencia ficción": [
        "Code Geass", "Cowboy Bebop", "Darling in the FranXX", "Dr. Stone",
        "Ergo Proxy", "Mobile Suit Gundam", "Neon Genesis Evangelion", "Psycho-Pass"
    ],
    "Drama": [
        "Life", "Chronos DEEP", "Kasane", "Vitamin", "Liar Game",
        "Los carruajes de Bradherley", "Watashi-tachi no Shiawase na Jikan", "Bitter Virgin"
    ],
    "Romance": [
        "Madmoiselle Butterfly", "Lip Smoke", "Warau Kanoko-sama", 
        "Watashitachi no Shiawase na Jikan", "Hana wo Meshimase", 
        "Tomodachi no Hanashi", "Oiran Girl"
    ]
}

product_categories = np.random.choice(list(manga_names.keys()), n_rows)


nombre_producto = [np.random.choice(manga_names[category]) for category in product_categories]


etiqueta_values = ["LIQUIDACION", "NUEVO", "OFERTA"]
etiqueta = np.random.choice(etiqueta_values, n_rows)


discounts = []
for label in etiqueta:
    if label in ["LIQUIDACION", "OFERTA"]:
        discounts.append(f"{np.random.randint(2, 51)}%")
    else:
        # En el caso de 'NUEVO', se deja un 20% de posibilidades de que tenga descuento
        discounts.append(f"{np.random.randint(2, 51)}%" if np.random.rand() > 0.2 else "")


department = ['LIMA'] * n_rows
province = ['LIMA'] * n_rows
districts = ['LIMA', 'ANCON', 'ATE', 'BARRANCO', 'BREÑA', 'CARABAYLLO', 'CHACLACAYO', 'CHORRILLOS', 
             'CIENEGUILLA', 'COMAS', 'EL AGUSTINO', 'INDEPENDENCIA', 'JESUS MARIA', 'LA MOLINA', 
             'LA VICTORIA', 'LINCE', 'LOS OLIVOS', 'LURIGANCHO', 'LURIN', 'MAGDALENA DEL MAR', 
             'MIRAFLORES', 'PACHACAMAC', 'PUCUSANA', 'PUEBLO LIBRE', 'PUENTE PIEDRA', 
             'PUNTA HERMOSA', 'PUNTA NEGRA', 'RIMAC', 'SAN BARTOLO', 'SAN BORJA', 'SAN ISIDRO', 
             'SAN JUAN DE LURIGANCHO', 'SAN JUAN DE MIRAFLORES', 'SAN LUIS', 'SAN MARTIN DE PORRES', 
             'SAN MIGUEL', 'SANTA ANITA', 'SANTA MARIA DEL MAR', 'SANTA ROSA', 'SANTIAGO DE SURCO', 
             'SURQUILLO', 'VILLA EL SALVADOR', 'VILLA MARIA DEL TRIUNFO']
district = np.random.choice(districts, n_rows)

# Crear el DataFrame
df = pd.DataFrame({
    "Fecha_venta": [date.strftime('%d-%m-%Y') for date in dates],
    "Mes_venta": months,
    "Estacion_año": seasons,
    "Cantidad_ventas": sales_counts,
    "Precio_producto": product_prices,
    "Nombre_producto": nombre_producto,
    "Categoría_producto": product_categories,
    "Descuentos": discounts,
    "Etiqueta": etiqueta,
    "Edad_prom_cliente": np.random.randint(12, 86, n_rows),
    "Genero_cliente": np.random.choice(['MASCULINO', 'FEMENINO'], n_rows),
    "Departamento": department,
    "Provincia": province,
    "Distrito": district
})

# Formato en .
df['Precio_producto'] = df['Precio_producto'].apply(lambda x: f"{x:.2f}".replace(',', '.'))

file_path = 'Data_Set_Ventas_Mangas.xlsx'
df.to_excel(file_path, index=False)

print("ARCHIVO GENERADO CORRECTAMENTE")
