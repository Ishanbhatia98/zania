import os

from app.database import db_instance


def main():
    for file in [
        # "pytest app/test/router/manage.py",
        "pytest app/test/model/product.py"
    ]:
        db_instance.delete_all_tables_and_metadata()
        os.system(file)


if __name__ == "__main__":
    main()
