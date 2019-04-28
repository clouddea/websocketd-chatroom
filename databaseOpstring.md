databaseOpstring = """
        CREATE TABLE if not exists public.chatroom
        (
            id serial NOT NULL,
            client_id integer NOT NULL,
            enter_time timestamp(6) without time zone NOT NULL,
            nick_name character varying(100) COLLATE pg_catalog."default" NOT NULL
        )
    """
def execute(execString, isSelect = False):
    con = psycopg2.connect(database = "postgres", user = "postgres", password = "admin", host = "localhost", port = 5432)
    cur = con.cursor()
    cur.execute(execString)
    ret = None
    if isSelect:
        ret = cur.fetchall()
    con.commit()
    con.close()
    return  ret

execute(databaseOpstring)                #进行表的创建"""


execute("insert into chatroom (client_id, nick_name, enter_time) values(%s, '%s', LOCALTIMESTAMP)"%(id,nickName))

execute("delete from chatroom where client_id = %s"%(id,))