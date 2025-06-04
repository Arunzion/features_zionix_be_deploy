#!/usr/bin/env python
import time
import psycopg2
from psycopg2 import OperationalError
import os
import subprocess

def wait_for_db():
    max_retries = 30
    retry_interval = 2  # seconds
    
    # Get database URL from environment
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is not set")
    
    for i in range(max_retries):
        try:
            conn = psycopg2.connect(database_url)
            conn.close()
            print("Database is ready!")
            return True
        except OperationalError as e:
            print(f"Waiting for database... ({i + 1}/{max_retries})")
            time.sleep(retry_interval)
    
    raise Exception("Could not connect to the database")

def run_migrations():
    try:
        # Wait for database to be ready
        wait_for_db()
        
        # Run Alembic migrations
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        print("Migrations completed successfully!")
        return True
    except Exception as e:
        print(f"Error running migrations: {e}")
        return False

if __name__ == "__main__":
    run_migrations()
