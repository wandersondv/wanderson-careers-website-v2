from sqlalchemy import create_engine, text
#import os

db_connection_string = "mysql+pymysql://jtrybbz7sun03a3albi0:pscale_pw_AJ6fHDZ3AfDT2TOcyb5nEcE08LJ1DSwApw7ewSu7gNz@aws.connect.psdb.cloud/wandersoncareers?charset=utf8mb4"

#db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_jobs_from_db():
    with engine.connect() as conn:
          result = conn.execute(text("select * from jobs"))
          results_as_dict = result.mappings().all()
          jobs = []
          for row in results_as_dict:
            jobs.append(row)
          
          return jobs
    
  

    
      
    
  
