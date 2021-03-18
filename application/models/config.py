import web

db_host = 'localhost'
db_name = 'web_admin'
db_user = 'admin'
db_pw = 'admin.2021'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )