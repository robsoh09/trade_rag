import pandas as pd
from loadcsv import loadcsv
from main_cleaner import main_clean
from sql import (connect_db , 
                 db_insert_trades)

import sqlite3

pd.set_option('display.max_columns', None) #shows all columns when printing
pd.set_option('display.max_rows', None) #no row limit when printing 

CSV_FILE = "tradelog.csv"
DB_FILE = "trade.db"
#1. Load messy_trade_categories.csv 
#update main code to functions 
in_valid, missing_col,extra_col,trade_data = loadcsv(CSV_FILE)

#main program 
if in_valid: #if it is True:
    print("Column Validation passed")
    clean_up_trade, invalid_data = main_clean(trade_data)
    print(clean_up_trade)

#Compute PnL and Error trades
    total_trades = len(trade_data)
    valid_trades = len(clean_up_trade)
    removed_trades = total_trades - valid_trades
    total_pnl = clean_up_trade["pnl"].sum()

    print("Original trades:", total_trades)
    print("Valid trades:", valid_trades)
    print("Removed trades:", removed_trades)
    print("Total PnL:", total_pnl)


    try:              
        conn = connect_db(DB_FILE)
        #insert trade data row by row for RAG
        for index in range(len(clean_up_trade)):
            row = clean_up_trade.iloc[index]

            trade_id = int(row["trade_id"]) #defensive parameter settings 
            date = row["date"].strftime("%Y-%m-%d")
            ticker = str(row["ticker"])
            direction = str(row["direction"])
            pnl = float(row["pnl"])
            rule_followed = str(row["rule_followed"])
            main_tag = str(row["main_tag"])
            confidence_before_entry = str(row["confidence_before_entry"])
            one_line_lesson = str(row["one_line_lesson"])           
        
            trade_values = (trade_id, date, ticker,direction, pnl, rule_followed, main_tag, confidence_before_entry, one_line_lesson)
        
            data = db_insert_trades(trade_values,conn)
            print(f"Row {index} entered into DB")
        #open the connection  and close after all trades data has been committed
        conn.commit() 
        conn.close()

    except sqlite3.IntegrityError as error:
        print("Duplicate trade_id or database constraint error:", error)
        raise ValueError("Trade already exists in database") from error

    except sqlite3.OperationalError as error:
        print("Failed to open DB: ", error)
        raise ValueError("Data Entered before ") from error
            
else: 
    print("Column Failed Validation: ")   
    if len(missing_col) > 0: # i want to print if there is at least 1 item in the list 
       print("Missing Col: ", missing_col)

    if len(extra_col) > 0:
       print("Extra Col: ", extra_col)

    print("Ensure the data is correct first")


