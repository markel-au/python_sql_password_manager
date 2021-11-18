import psycopg2

def connection_db(): 
    # Enter password under ******** field. 
    connection = psycopg2.connect("dbname=/var/run/postgresql user=postgres password=docker") 
    return connection
