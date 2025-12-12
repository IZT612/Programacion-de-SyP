def persona_schema(persona) -> dict:
    # El id en base de datos es _id
    return {"id": str(persona["_id"]),
            "dni": persona["dni"],
            "nombre": persona["nombre"],
            "apellidos": persona["apellidos"],
            "telefono": persona["telefono"],
            "correo": persona["correo"]}

def personas_schema(personas) -> list:
    return [persona_schema(persona) for  persona in personas]