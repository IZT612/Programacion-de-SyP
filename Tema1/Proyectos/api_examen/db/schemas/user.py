def user_schema(user) -> dict:
    # El id en base de datos es _id
    return {"username": str(user["username"]),
            "fullname": str(user["fullname"]),
            "email": str(user["email"]),
            "disabled": bool(user["disabled"]),
            "password": str(user["password"])}

def users_schema(users) -> list:
    return [user_schema(user) for  user in users]