import sqlite3 
import pandas as pd

conn = sqlite3.connect("expense_tracker.db")
cursor = conn.cursor()

#creating table for expense tracker
cursor.execute('''
Create Table IF NOT EXISTS expenses_tracker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL,
    description TEXT
)   
''')

#for adding data in database
class DB:
    def add_data(self,amount,category,date,description):
        conn = sqlite3.connect("expense_tracker.db")
        cursor = conn.cursor()
        cursor.execute('''
insert into expenses_tracker (amount,category,date,description) values (?,?,?,?)
                    ''',(amount,category,date,description))
        conn.commit()
        conn.close()
        

    def get_data(self):
        conn = sqlite3.connect("expense_tracker.db")
        r = pd.read_sql_query("SELECT * FROM expenses_tracker",conn)
        return r
        conn.close()
    
    def delete_data(self,id):
        conn = sqlite3.connect("expense_tracker.db")
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM expenses_tracker WHERE id = ?''',(id,))
        conn.commit()
        conn.close
    def category_total(self):
        conn = sqlite3.connect("expense_tracker.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT category , SUM(amount) FROM expenses_tracker GROUP BY category''')
        data = cursor.fetchall()
        return pd.DataFrame(data, columns=["Category", "Total Amount"])
        conn.commit()
        conn.close       

