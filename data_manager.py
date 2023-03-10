import database_common


@database_common.connection_handler
def insert_user_credentials(cursor, username, password):
    cursor.execute('INSERT INTO user_credentials (username, password) VALUES (%(username)s, %(password)s);',
                   {'username': username, 'password': password}
                   )


@database_common.connection_handler
def get_user(cursor, username):
    cursor.execute('SELECT * FROM user_credentials WHERE username = %(username)s;',
                   {"username": username}
                   )
    return cursor.fetchone()


@database_common.connection_handler
def get_user_pass(cursor, username):
    cursor.execute('SELECT password FROM user_credentials WHERE username = %(username)s;',
                   {"username": username}
                   )
    return cursor.fetchone()['password']


@database_common.connection_handler
def insert_vote(cursor, planet_id, planet_name, user_id):
    cursor.execute(
        """
        INSERT INTO planet_votes (planet_name, user_id, planet_id)
        VALUES (%(planet_name)s, %(user_id)s, %(planet_id)s);
        """"",
        {'planet_id': planet_id,
         "planet_name": planet_name,
         "user_id": user_id}
    )


@database_common.connection_handler
def get_voting_statistics(cursor, user_id):
    cursor.execute(
        """
        SELECT planet_name, COUNT(planet_name) FROM planet_votes
        WHERE user_id = %(user_id)s
        GROUP BY planet_name;
        """,
        {'user_id': user_id}
    )
    return cursor.fetchall()
