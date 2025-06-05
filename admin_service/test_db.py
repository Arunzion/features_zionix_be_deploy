from sqlalchemy import create_engine, text
from app.core.config import settings

def test_connection():
    try:
        # Create a direct connection for testing using settings
        connection_string = settings.DATABASE_URL
        engine = create_engine(connection_string)
        
        # Try to connect and execute a simple query
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Database connection successful!")
            
            # Check for existence of tables
            result = connection.execute(text("""
                SELECT tablename 
                FROM pg_catalog.pg_tables
                WHERE schemaname = 'public';
            """))
            tables = [row[0] for row in result]
            print("Existing tables:", tables)
            
    except Exception as e:
        print("Database connection failed!")
        print("Error:", str(e))

if __name__ == "__main__":
    test_connection()
