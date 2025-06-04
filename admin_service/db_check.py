import psycopg2
import time

def check_db():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                dbname="admin_service",
                user="postgres",
                password="Arunnathan",
                host="admin_postgres",
                port="5432"
            )
            cur = conn.cursor()
            
            # Check if domains table exists
            cur.execute("""
                SELECT EXISTS (
                    SELECT FROM pg_tables
                    WHERE schemaname='public' AND tablename='domains'
                );
            """)
            domains_exist = cur.fetchone()[0]
            
            # Check if applications table exists
            cur.execute("""
                SELECT EXISTS (
                    SELECT FROM pg_tables
                    WHERE schemaname='public' AND tablename='applications'
                );
            """)
            applications_exist = cur.fetchone()[0]
            
            print(f"Domains table exists: {domains_exist}")
            print(f"Applications table exists: {applications_exist}")
            
            cur.close()
            conn.close()
            break
        except psycopg2.OperationalError:
            retries -= 1
            print(f"Failed to connect. Retrying in 2 seconds... ({retries} attempts left)")
            time.sleep(2)

if __name__ == "__main__":
    check_db()
