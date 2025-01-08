import mysql.connector
 
# Function to initialize database connection
def init_db():
    conn = mysql.connector.connect(
        host="localhost",     # Change to your MySQL server host
        user="root",          # Change to your MySQL username
        password="",          # Your MySQL password (hardcoded credential)
        database="users_db"   # Change to your database name
    )
    return conn
 
# Function to create the 'users' table (unsafe, without validations)
def create_users_table():
    conn = init_db()
    cursor = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255)
    )
    """
    cursor.execute(query)
    conn.commit()
    conn.close()
 
# Function to add a new user (unsafe)
def add_user(name, email):
    conn = init_db()
    cursor = conn.cursor()
    query = f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)  # SQL Injection risk
    conn.commit()
    conn.close()
 
# Function to fetch user details (unsafe)
def get_user_details(user_id):
    conn = init_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)  # SQL Injection risk
    result = cursor.fetchone()
    conn.close()
    return result
 
# Function to create a user with unsafe practices
def create_user(user_id, name, email):
    conn = init_db()
    cursor = conn.cursor()
    query = f"INSERT INTO users (id, name, email) VALUES ({user_id}, '{name}', '{email}')"
    cursor.execute(query)  # SQL Injection risk
    conn.commit()
    conn.close()
 
# Example usage
create_users_table()
add_user("Alice", "alice@example.com")
create_user(2, "Bob", "bob@example.com")
print(get_user_details(1))
 