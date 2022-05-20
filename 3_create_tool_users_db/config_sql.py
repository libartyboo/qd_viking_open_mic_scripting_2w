def tb_name(project):
    return f"users_{project}"


def tb_users(tb_n):
    return f''' CREATE TABLE IF NOT EXISTS {tb_n}( 
    id INTEGER PRIMARY KEY NOT NULL, 
    first_name TEXT,
    last_name TEXT,
    user_email TEXT,
    user_password TEXT)'''


def sql_create_user(project, fname, lname, em, passw):
    return f'''INSERT INTO {tb_name(project)} (first_name, last_name, user_email, user_password) 
    VALUES ('{fname}', '{lname}', '{em}', '{passw}')'''


def sql_get_all(project):
    return f''' SELECT * FROM {tb_name(project)}'''
