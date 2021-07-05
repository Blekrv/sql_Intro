import psycopg2
from config import *
from psycopg2 import Error
try:
    connection = psycopg2.connect(
        user=USER, password=PASSWORD, host=HOST, port=PORT, database='user_db')

    cursor = connection.cursor()
    cursor.execute('SELECT VERSION()')

    create_table_query = '''CREATE TABLE if not exists user_db
        (   id SERIAL PRIMARY KEY NOT NULL,
            name TEXT          NOT NULL,
            email TEXT          NOT NULL,
            password INT        NOT NULL
        );
    '''
    # ------------------------------------------------------
    addUser = """
        INSERT INTO public.user_db
    (
        name,email,password
    )
     VALUES('Bill','Bill@gmail.com','q1w2e3r4'),
    ('Bob','Bob@gmail.com','q1w2e3r4'),
    ('John','John@yahoo.com','q1w2e3r4'),
    ('Andrew','Andrew@gmail.com','q1w2e3r4'),
    ('Emilia','Emilia@gmail.com','q1w2e3r4'),
    ('Joeka','Joeka@bingo.com','q1w2e3r4'),
    ('Peter','Peter@gmail.com','q1w2e3r4'),
    ('Alisa','Alisa@i.ua','q1w2e3r4'),
    ('Shon','Shon@yandex.com','q1w2e3r4'),
    ('Derek','Derek@mail.ru','q1w2e3r4');
    """
    cursor.execute(addUser)
    # ----------------------------------------------
    emailFind = """
        SELECT email from public.user_db WHERE email like '%gmail%';
    """
    cursor.execute(emailFind)
    show = cursor.fetchall()
    print(show)
    # --------------------------------------------
    passwordChancge = """
        UPDATE public.user_db SET password = '87654321' WHERE id = 4;
    """
    cursor.execute(passwordChancge)
    # -------------------------------------------------
    userDelete = """
        DELETE FROM public.user_db WHERE name like '%Bill%';
    """
    cursor.execute(userDelete)
    # ----------------------------------------------------------------
    userFind = """
        SELECT * from public.user_db WHERE name like 'A%';
    """
    cursor.execute(userFind)
    show = cursor.fetchall()
    print(show)
    # ---------------------------

    connection.commit()
    print('Commit Success')
except(Exception, Error) as error:
    print('Error Connection', error)
finally:
    if connection:
        print('Connection closed')
        cursor.close()
        connection.close()

