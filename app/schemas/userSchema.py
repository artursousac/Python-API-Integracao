def individual(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }


def list(users) -> list:
    return [individual(user) for user in users]
