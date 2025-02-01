
from app.database import db_instance
import os

def main():
    db_instance.delete_all_tables_and_metadata()
    os.system("pytest app/test/router/manage.py")  

if __name__=='__main__':
    main()