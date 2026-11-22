def build_user_query(username):
    """Build a SQL query for a user-supplied username."""
    return f"SELECT * FROM users WHERE name = '{username}'"
