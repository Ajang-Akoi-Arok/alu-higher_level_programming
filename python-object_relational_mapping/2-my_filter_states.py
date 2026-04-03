#!/usr/bin/python3
"""Displays all values in states table where name matches argument safely."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to database
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Create cursor
    cur = con.cursor()
    
    # Safe parameterized query (prevents SQL injection)
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))
    
    # Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Clean up
    cur.close()
    con.close()
