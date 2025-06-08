import sqlite3
import os

def check_database():
    db_path = 'db.sqlite3'
    try:
        # Try to connect to the database
        conn = sqlite3.connect(db_path, timeout=1)
        cursor = conn.cursor()
        
        # Check if we can write to the database
        try:
            cursor.execute('BEGIN IMMEDIATE')
            cursor.execute('ROLLBACK')
            print("Database is not locked and is writable")
        except sqlite3.OperationalError as e:
            print(f"Database is locked: {e}")
            
        # Get active connections
        cursor.execute("SELECT * FROM sqlite_master LIMIT 1")
        print("Successfully queried the database")
        
        # Close connection properly
        cursor.close()
        conn.close()
        print("Database connection closed successfully")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check_database()
