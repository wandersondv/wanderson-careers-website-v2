from sqlalchemy import create_engine, text
import os


db_connection_string = os.environ['DB_CONNECTION_STR']
#print(os.getenv("DB_CONNECTION_STR"))
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
    
  

    
      
    
  
