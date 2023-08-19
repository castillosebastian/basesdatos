import json

# Data for the TALLER table
tables_data = {
    "TALLER": {
        "columns": {
        "id_taller": { "type": "integer", "PK": True },
        "nombre": { "type": "VARCHAR(20)" },
        "calle": { "type": "VARCHAR(15)" },
        "calle_nro": { "type": "integer" },
        "dni_resp": { "type": "integer", "FK": True, "UK": True, "Not None": True }
        },
        "data": [
        { "id_taller": 1, "nombre": "tallerT1", "calle": "Av. Sol", "calle_nro": 2358, "dni_resp": 10000 },
        { "id_taller": 2, "nombre": "tallerT2", "calle": "Las Magnolias", "calle_nro": 2580, "dni_resp": 20000 },
        { "id_taller": 3, "nombre": "tallerT3", "calle": "Las Sombras", "calle_nro": 4289, "dni_resp": 30000 }
        ]
    },  
    "CELULA": {
        "columns": {
        "id_celula": { "type": "integer", "PK": True },
        "descripcion": { "type": "VARCHAR(10)" },
        "id_taller": { "type": "integer", "FK": True }
        },
        "data": [
        { "id_celula": 3, "descripcion": "celulaC1", "id_taller": 1 },
        { "id_celula": 4, "descripcion": "celulaC2", "id_taller": 3 },
        { "id_celula": 5, "descripcion": "celulaC3", "id_taller": 2 },
        { "id_celula": 6, "descripcion": "celulaC4", "id_taller": 3 }
        ]
    },
    "MAQUINA": {
        "columns": {
        "id_maquina": { "type": "integer", "PK": True },
        "nombre": { "type": "VARCHAR(10)" },
        "tipo": { "type": "VARCHAR(2)" },
        "id_celula": { "type": "integer", "FK": True }
        },
        "data": [
        { "id_maquina": 1, "nombre": "maquinaM1", "tipo": "T1", "id_celula": 5 },
        { "id_maquina": 2, "nombre": "maquinaM2", "tipo": "T1", "id_celula": 3 },
        { "id_maquina": 3, "nombre": "maquinaM3", "tipo": "T2", "id_celula": 4 }
        ]
    },
    "OPERARIO": {
        "columns": {
        "dni": { "type": "integer", "PK": True },
        "nombre": { "type": "VARCHAR(20)" },
        "apellido": { "type": "VARCHAR(20)" },
        "responsable_taller": { "type": "integer", "Not None": True, "Check": "0,1" },
        "salario": { "type": "integer" },
        "id_taller": { "type": "integer", "FK": True }
        },
        "data": [
        { "dni": 35000, "nombre": "Juan Cortez", "apellido": "Cortez", "responsable_taller": 0, "salario": 350000, "id_taller": 3 },
        { "dni": 36000, "nombre": "Marcelo Lopez", "apellido": "Lopez", "responsable_taller": 0, "salario": 278500, "id_taller": 1 },
        { "dni": 40000, "nombre": "Alex Valdez", "apellido": "Valdez", "responsable_taller": 0, "salario": 340000, "id_taller": 2 },
        { "dni": 10000, "nombre": "Pedro Rios", "apellido": "Rios", "responsable_taller": 1, "salario": 458000, "id_taller": 1 },
        { "dni": 20000, "nombre": "Marcos Medina", "apellido": "Medina", "responsable_taller": 1, "salario": 500000, "id_taller": 2 },
        { "dni": 30000, "nombre": "Francisco Ramirez", "apellido": "Ramirez", "responsable_taller": 1, "salario": 512500, "id_taller": 3 }
        ]
    },
    "OP_ASIGNADO_CEL": {
        "columns": {
        "dni": { "type": "integer", "PK": True, "FK": True },
        "id_celula": { "type": "integer", "PK": True, "FK": True },
        "fecha_desde": { "type": "date", "PK": True },
        "fecha_hasta": { "type": "date" }
        },
        "data": [
        { "dni": 35000, "id_celula": 4, "fecha_desde": "01/01/2022", "fecha_hasta": "31/12/2022" },
        { "dni": 35000, "id_celula": 6, "fecha_desde": "01/01/2023", "fecha_hasta": None },
        { "dni": 36000, "id_celula": 3, "fecha_desde": "10/08/2023", "fecha_hasta": None },
        { "dni": 40000, "id_celula": 5, "fecha_desde": "15/12/2022", "fecha_hasta": None }
        ]
    },
    "TEL_TALLER": {
        "columns": {
        "id_taller": { "type": "integer", "PK": True, "FK": True },
        "nro_tel": { "type": "integer", "PK": True }
        },
        "data": [
        { "id_taller": 1, "nro_tel": 156222333 },
        { "id_taller": 1, "nro_tel": 4258693 },
        { "id_taller": 2, "nro_tel": 158889995 },
        { "id_taller": 3, "nro_tel": 154845484 }
        ]
    }
}

# Write the data to taller.json
# Iterate through tables_data and write each table to a separate JSON file
for table_name, table_data in tables_data.items():
    filename = f'{table_name.lower()}.json'
    with open(filename, 'w') as file:
        json.dump({table_name: table_data}, file, indent=4)