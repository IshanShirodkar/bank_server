import sqlite3

# SQLite database file
DATABASE = 'banks.db'

# Query to check banks data
CHECK_BANKS_QUERY = 'SELECT * FROM banks'

# Query to check branches data
CHECK_BRANCHES_QUERY = 'SELECT * FROM branches'

# Function to fetch all rows from a table
def fetch_all_rows(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

# Main test script
if __name__ == '__main__':
    # Connect to SQLite database
    conn = sqlite3.connect(DATABASE)
    
    # Check banks data
    banks_rows = fetch_all_rows(conn, CHECK_BANKS_QUERY)
    print('Banks data:')
    for row in banks_rows:
        print(row)
    print(f'Total banks: {len(banks_rows)}')
    print()
    
    # Check branches data
    branches_rows = fetch_all_rows(conn, CHECK_BRANCHES_QUERY)
    print('Branches data:')
    for row in branches_rows:
        print(row)
    print(f'Total branches: {len(branches_rows)}')
    print()
    
    # Close connection
    conn.close()
