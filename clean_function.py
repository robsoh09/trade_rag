"""
    wrong initial code
    clean_data = clean_trades_data["pnl"] = (
                  clean_trades_data["pnl"].astype(str)
                  .str.replace("$", "", reg ex=False)
                  .str.replace(",", "", regex=False)
                  .str.strip() #remove whitespace 
                  )

    return clean_data -> this turns the pnl column into a Series, a list like structure. 
    keyerror: Pnl appears when we try to convert to numeric and drop NaN rows since there is no pnl key anymore 

        
"""

import pandas as pd
def clean_row(trade_data):

    missing_pnl_rows = trade_data[trade_data["pnl"].isna()].copy() #finding the missing NaN rows
    clean_trade_data = trade_data.dropna(subset=["pnl"]).copy() #drop rows where it is NaN in PnL Column 

    #return the information 
    return missing_pnl_rows, clean_trade_data


def convert_numeric(clean_trades_data):
    #we want the entire pnl data to be cleaned. 
    #clean_data = clean_trades_data["pnl"] wont work 
    clean_trades_data = clean_trades_data.copy() #avoid cleaning the original use.copy()

    clean_trades_data["pnl"] = (
                  clean_trades_data["pnl"].astype(str)
                  .str.replace("$", "", regex=False)
                  .str.replace(",", "", regex=False)
                  .str.strip() #remove whitespace 
                  )
    #Treat the thing I want to replace as normal text when using regex=False
    #if regex=True, it becomes a Regex expression for pattern matching.. i hate regex :) 
        
    #after cleaning up, we update to numeric and drop the rows with NaN in the column 
    clean_trades_data["pnl"] = pd.to_numeric(clean_trades_data["pnl"], errors='coerce')
    dropped_rows = clean_trades_data[clean_trades_data["pnl"].isna()].copy() #copy the rows info. 
    clean_trades_data = clean_trades_data.dropna(subset=["pnl"]).copy() #copy avoids pandas warning
    
    return dropped_rows, clean_trades_data


def convert_upper(clean_trade_data):
   #guard check for ticker    
   clean_trade_data = clean_trade_data.copy() #make a copy of the source dataframe  and put it in clean_trade_data as a copy
   #this ensures we dont modify the original data from the source!

   if "ticker" not in clean_trade_data.columns: #if ticker is not in the column, 
         return "no ticker column found!" 

   #proceed to clean then if ticker is in 
   clean_trade_data['ticker'] = (clean_trade_data["ticker"].astype(str).str.upper().str.strip()) #change to UPPER and strip the whitespace

   #this should not modify trade_data in the main.py
   return clean_trade_data

def convert_direction(clean_trade_data):
    #guard check for ticker 
    clean_trade_data = clean_trade_data.copy() #make a copy of the source dataframe  and put it in clean_trade_data as a copy
    #this ensures we dont modify the original data from the source!
 
    if "direction" not in clean_trade_data.columns: #if direction is not in the column, 
         return "no direction column found!" 
        
    clean_trade_data["direction"] = (
                  clean_trade_data["direction"].astype(str)
                  .str.strip() #remove whitespace 
                  .str.upper()
                  )


    direction_map = { #look up each row in clean_trade_data and swap BUY for LONG, if data does not exist, it updates to NaN
        "BUY": "LONG",
        "LONG": "LONG",
        "SELL": "SHORT",
        "SHORT": "SHORT"


    }

    clean_trade_data["direction"] = clean_trade_data["direction"].map(direction_map)
    invalid_direction_rows = clean_trade_data[clean_trade_data["direction"].isna()] #not LONG or SHORT by searching for NaN values
    #.map changes the BUY to LONG. 
    clean_trade_data = clean_trade_data.dropna(subset=["direction"]).copy() #drop rows where it is NaN in PnL Column 


    return invalid_direction_rows, clean_trade_data

def convert_rule_followed(clean_trade_data):

    clean_trade_data = clean_trade_data.copy()
    if "rule_followed" not in clean_trade_data:
    #if "rule_followed" not in clean_trade_data.columns: 
        return "no rule_followed required"
    
    clean_trade_data["rule_followed"] = (
        clean_trade_data["rule_followed"].astype(str)
        .str.strip()
        .str.upper()

    )

    rule_map = {

        #.map considers all values e.g if yes is upper() YES is not in map, it becames NaN 
        # need to include all possibilities 
        "Y": "YES",
        "YES": "YES",
        "NO": "NO",
        "N": "NO",
        "TRUE": "YES",
        "FALSE": "NO"

    }
    #stuck at drop rows. 
    clean_trade_data["rule_followed"] = clean_trade_data["rule_followed"].map(rule_map)
    invalid_rule_rows = clean_trade_data[clean_trade_data["rule_followed"].isna()] #finding rows with NaN 
    clean_trade_data = clean_trade_data.dropna(subset=["rule_followed"]).copy() #drop rows where it is NaN

  
    return invalid_rule_rows, clean_trade_data