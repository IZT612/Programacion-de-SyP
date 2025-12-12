def movil_schema(movil) -> dict:
    # El id en base de datos es _id
    return {"id": str(movil["_id"]),
            "precio_coste": movil["precio_coste"],
            "precio_venta": movil["precio_venta"],
            "id_persona": movil["id_persona"]}

def moviles_schema(moviles) -> list:
    return [movil_schema(movil) for  movil in moviles] 
