import csv
import sqlite3

# SQLite database file
DATABASE = 'banks.db'

# Create the banks table
def create_banks_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS banks
                 (id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL)''')

# Create the branches table
def create_branches_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS branches
                 (ifsc TEXT PRIMARY KEY,
                 bank_id INTEGER,
                 branch TEXT,
                 address TEXT,
                 city TEXT,
                 district TEXT,
                 state TEXT,
                 bank_name TEXT,
                 FOREIGN KEY(bank_id) REFERENCES banks(id))''')

# Insert a bank into the banks table
def insert_bank(conn, bank_id, bank_name):
    conn.execute('INSERT OR IGNORE INTO banks (id, name) VALUES (?, ?)', (bank_id, bank_name))

# Insert a branch into the branches table
def insert_branch(conn, ifsc, bank_id, branch, address, city, district, state, bank_name):
    conn.execute('INSERT INTO branches (ifsc, bank_id, branch, address, city, district, state, bank_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                 (ifsc, bank_id, branch, address, city, district, state, bank_name))

# Load bank data from CSV
def load_banks_data(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bank_id = int(row['bank_id'])
            bank_name = row['bank_name']
            insert_bank(conn, bank_id, bank_name)
            print("added bank " + str(bank_id))

# Load branches data from CSV
def load_branches_data(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ifsc = row['ifsc']
            bank_id = int(row['bank_id'])
            branch = row['branch']
            address = row['address']
            city = row['city']
            district = row['district']
            state = row['state']
            bank_name = row['bank_name']
            insert_branch(conn, ifsc, bank_id, branch, address, city, district, state, bank_name)
            print("added branch" + branch)

# Main script
if __name__ == '__main__':
    # Connect to SQLite database
    conn = sqlite3.connect(DATABASE)
    
    # Create tables if they do not exist
    create_banks_table(conn)
    create_branches_table(conn)
    
    # Load bank data from CSV
    load_banks_data('banks.csv')
    
    # Load branches data from CSV
    load_branches_data('bank_branches.csv')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
