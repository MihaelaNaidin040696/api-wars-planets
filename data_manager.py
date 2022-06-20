import database_common


@database_common.connection_handler
def insert_user_credentials(cursor, username, password):
    cursor.execute(
        "INSERT INTO user_credentials (username, password)"
        "VALUES (%(username)s, %(password)s);",
        {'username': username, 'password': password}
    )


@database_common.connection_handler
def get_user(cursor, username):
    cursor.execute(
        "SELECT * FROM user_credentials "
        "WHERE username = %(username)s;",
        {"username": username}
    )
    return cursor.fetchone()


@database_common.connection_handler
def get_user_pass(cursor, username):
    cursor.execute(
        "SELECT password FROM user_credentials "
        "WHERE username = %(username)s;",
        {"username": username}
    )
    return cursor.fetchone()['password']
