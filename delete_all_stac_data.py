import os

import dotenv
import psycopg
from pypgstac.db import PgstacDB

dotenv.load_dotenv()


def main():
    """Delete all STAC data from the database."""
    db = PgstacDB()
    db_name = os.getenv("PGDATABASE", "unknown")

    confirmation = input(
        f"Are you sure you want to delete all STAC data in database '{db_name}'? (y/N): ",
    )
    if confirmation.lower() == "y":
        print("Deleting all STAC items")
        try:
            db.query_one("DELETE FROM pgstac.items")
        except psycopg.ProgrammingError as e:
            print(e)
        print("Successfully deleted all STAC items")
        print("Deleting all STAC collections")
        try:
            db.query_one("DELETE FROM pgstac.collections")
        except psycopg.ProgrammingError as e:
            print(e)
        print("Successfully deleted all STAC collections")
    else:
        print("Operation cancelled")


if __name__ == "__main__":
    main()
