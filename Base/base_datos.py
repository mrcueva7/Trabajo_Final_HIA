import sqlite3

conn = sqlite3.connect("ciudades.db")
cursor = conn.cursor()

# Creamos Tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS ciudades (
    id PRIMARY KEY,
    CODIGO_CIUDAD TEXT NOY NULL,
    CIUDAD TEXT NOT NULL,
    REGION TEXT NOT NULL,
    ALTURA TEXT NOT NULL
);
""")

# Insertamos datos en la tabla
ciudad_region = [
    (1, 'UIO', 'QUITO', 'SIERRA', 2850),
    (2, 'CUE', 'CUENCA', 'SIERRA', 2550),
    (3, 'LOH', 'LOJA', 'SIERRA', 2530),
    (4, 'AMB', 'AMBATO', 'SIERRA', 2500),
    (5, 'TEN', 'PUYO', 'ORIENTE', 950),
    (6, 'ZAM', 'ZAMORA', 'ORIENTE', 920),
    (7, 'SCY', 'SAN CRISTOBAL', 'COSTA', 730),
    (8, 'OCC', 'COCA', 'ORIENTE', 300),
    (9, 'NLO', 'NUEVA LOJA', 'ORIENTE', 297),
    (10, 'GPS', 'BALTRA', 'COSTA', 100),
    (11, 'ETR', 'SANTA ROSA', 'COSTA', 10),
    (12, 'MEC', 'MANTA', 'COSTA', 6),
    (13, 'GYE', 'GUAYAQUIL', 'COSTA', 4)
]

cursor.executemany('''
INSERT OR REPLACE INTO ciudades (id, CODIGO_CIUDAD, CIUDAD, REGION, ALTURA) 
VALUES (?, ?, ?, ?, ?)
''', ciudad_region)

conn.commit()
conn.close()

print("Tabla creada y datos insertados exitosamente.")


