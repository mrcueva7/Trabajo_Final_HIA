import sqlite3

db_path = "Base/ciudades.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS ciudades (
    CODIGO_CIUDAD TEXT PRIMARY KEY,
    CIUDAD TEXT NOT NULL,
    REGION TEXT NOT NULL,
    ALTURA TEXT NOT NULL
);
""")

cursor.execute('''
INSERT INTO ciudades (CODIGO_CIUDAD, CIUDAD, REGION, ALTURA)
VALUES 
('UIO', 'QUITO', 'SIERRA', 2850),
('CUE', 'CUENCA', 'SIERRA', 2550),
('LOH', 'LOJA', 'SIERRA', 2530),
('AMB', 'AMBATO', 'SIERRA', 2500),
('TEN', 'PUYO', 'ORIENTE', 950),
('ZAM', 'ZAMORA', 'ORIENTE', 920),
('SCY', 'SAN CRISTOBAL', 'COSTA', 730),
('OCC', 'COCA', 'ORIENTE', 300),
('NLO', 'NUEVA LOJA', 'ORIENTE', 297),
('GPS', 'BALTRA', 'COSTA', 100),
('ETR', 'SANTA ROSA', 'COSTA', 10),
('MEC', 'MANTA', 'COSTA', 6),
('GYE', 'GUAYAQUIL', 'COSTA', 4)
''')


conn.commit()
conn.close()

print("Tabla creada y datos insertados exitosamente.")


