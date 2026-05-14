"""sql connection 
"""
import sqlite3

def connect_db(db_name):
     
     try: 
      
            with sqlite3.connect(db_name) as conn: 
            #with sqlite3.connect(':memory') as conn: using memory as db storage
             print("Connected to database")  

            return conn              
     
     except sqlite3.OperationalError as error:
            print("Failed to open DB: ", error)


def db_insert_trades(trade_values, conn):
     
    sql_row = """INSERT INTO trades (
               trade_id,
               date,
               ticker,
               direction,
               pnl,
               rule_followed,
               main_tag,
               confidence_before_entry,
               one_line_lesson
               )
             VALUES (?,?,?,?,?,?,?,?,?)
               
         """ 
    cursor = conn.cursor()
    #insert rows into sql from clean_up_trade
    cursor.execute(sql_row,trade_values)


    return conn

def sql_count(conn):
     
     sql = """SELECT COUNT(*) FROM trades;
              """
     cursor = conn.cursor()
     cursor.execute(sql)
     rows = cursor.fetchone()[0]


     return rows


def get_pnl(conn):
     
     sql = """SELECT SUM(pnl) FROM trades;
              """
     
     cursor = conn.cursor()
     cursor.execute(sql)
     row = cursor.fetchone()[0]

     return row


def get_trades(conn):

    #SELECT trades where these columns and order by date    
   sql = """SELECT
       trade_id,
       date,
       ticker,
       direction,
       pnl,
       rule_followed,
       main_tag,
       confidence_before_entry,
       one_line_lesson
       FROM trades
       ORDER BY date;"""
       
   cursor = conn.cursor()
   cursor.execute(sql)
   rows = cursor.fetchall()

   return rows
