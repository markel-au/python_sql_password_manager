import psycopg2

def connection_db(): 
    # Enter password under ******** field. 
    connection = psycopg2.connect("dbname=2858e66d7777 user=postgres password=docker") 
    return connection
