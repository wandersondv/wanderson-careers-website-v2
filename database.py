from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://atyoq63j1r7wyjb8u3h9:pscale_pw_PvuYsU6LD9fQ9zQWecAoFBkxoWZgYw5C4MQ4H0FbLrZ@aws.connect.psdb.cloud/wandersoncareers?charset=utf8mb4"

engine = create_engine( db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print("type(result):", type(result))
  result_all = result.all()
  print("type(result.all())",type(result_all))
  print("result.all():", result_all)
  