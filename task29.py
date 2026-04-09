def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    active_user = {}
    for user, info in users.items():
        if "active" in info and info["active"] == True:
            active_user[user] = info
    return active_user
users = {
    "Ali": {"active": True},
    "Bob": {"active": False},
    "Charlie": {"active": True}, 
    "vali": {"active": False}, 
    "olim": {"active": True}
}
print(get_active_users(users))