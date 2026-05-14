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
def clean_row(trade_data, column_name):

    missing_pnl_rows = trade_data[trade_data[column_name].isna()].copy() #finding the missing NaN rows
    clean_trade_data = trade_data.dropna(subset=[column_name]).copy() #drop rows where it is NaN in PnL Column 

    #return the information 
    return missing_pnl_rows, clean_trade_data

def clean_row(trade_data, column_name):
    
    if column_name not in trade_data.columns: #if ticker is not in the column, 
       return f"no {column_name} column found!" 

    missing_pnl_rows = trade_data[trade_data[column_name].isna()].copy() #finding the missing NaN rows
    clean_trade_data = trade_data.dropna(subset=[column_name]).copy() #drop rows where it is NaN in PnL Column 

    #return the information 
    return missing_pnl_rows, clean_trade_data


def convert_numeric(clean_trades_data, column_name):
    #we want the entire pnl data to be cleaned. 
    #clean_data = clean_trades_data["pnl"] wont work 
    clean_trades_data = clean_trades_data.copy() #avoid cleaning the original use.copy()

    clean_trades_data[column_name] = (
                  clean_trades_data[column_name].astype(str)
                  .str.replace("$", "", regex=False)
                  .str.replace(",", "", regex=False)
                  .str.strip() #remove whitespace 
                  )
    #Treat the thing I want to replace as normal text when using regex=False
    #if regex=True, it becomes a Regex expression for pattern matching.. i hate regex :) 
        
    #after cleaning up, we update to numeric and drop the rows with NaN in the column 
    clean_trades_data[column_name] = pd.to_numeric(clean_trades_data[column_name], errors='coerce')
    dropped_rows = clean_trades_data[clean_trades_data[column_name].isna()].copy() #copy the rows info. 
    clean_trades_data = clean_trades_data.dropna(subset=[column_name]).copy() #copy avoids pandas warning
    
    return dropped_rows, clean_trades_data


def convert_upper(clean_trade_data):
   #guard check for ticker    
   clean_trade_data = clean_trade_data.copy()
   #this ensures we dont modify the original data from the source!

   if "ticker" not in clean_trade_data.columns: #if ticker is not in the column, 
         return "no ticker column found!" 

   #convert to type as str.UPPER and strip the whitespace
   clean_trade_data['ticker'] = clean_trade_data["ticker"].astype(str).str.upper().str.strip() 
   
   #storing the invalid ticker rows with filters == "" empty string, filters where NaN becomes string NAN
   invalid_ticker_rows = clean_trade_data[(clean_trade_data["ticker"].isna()) 
                                          | (clean_trade_data["ticker"] == "") 
                                          |(clean_trade_data["ticker"] == "NAN")].copy()



   #dropping the invalid rows with ~(rules) 
   #Filter the DataFrame and keep only rows that are not in any of these conditions.
   clean_trade_data = clean_trade_data[
        ~(
            (clean_trade_data["ticker"].isna()) |
            (clean_trade_data["ticker"] == "") |
            (clean_trade_data["ticker"] == "NAN")
        )
    ].copy()

   return invalid_ticker_rows, clean_trade_data




def convert_to_caps(clean_trade_data, column_name):
   #guard check for ticker    
   clean_trade_data = clean_trade_data.copy()
   #this ensures we dont modify the original data from the source!

   if column_name not in clean_trade_data.columns: #if ticker is not in the column, 
         return f"no {column_name} column found!" 

   #convert to type as str.UPPER and strip the whitespace
   clean_trade_data[column_name] = clean_trade_data[column_name].astype(str).str.upper().str.strip() 
   
   #storing the invalid rows with filters == "" empty string, filters where NaN becomes string NAN
   invalid_rows = clean_trade_data[(clean_trade_data[column_name].isna()) 
                                          | (clean_trade_data[column_name] == "") 
                                          |(clean_trade_data[column_name] == "NAN")].copy()

   clean_trade_data = clean_trade_data[
        ~(
            (clean_trade_data[column_name].isna()) |
            (clean_trade_data[column_name] == "") |
            (clean_trade_data[column_name] == "NAN")
        )
    ].copy()
    
   return invalid_rows, clean_trade_data


def convert_direction(clean_trade_data, column_name):
    #guard check for ticker 
    clean_trade_data = clean_trade_data.copy() #make a copy of the source dataframe  and put it in clean_trade_data as a copy
    #this ensures we dont modify the original data from the source!
 
    if column_name not in clean_trade_data: #if direction is not in the column, 
         return "no direction column found!" 
        
    clean_trade_data[column_name] = (
                  clean_trade_data[column_name].astype(str)
                  .str.strip() #remove whitespace 
                  .str.upper()
                  )


    direction_map = { #look up each row in clean_trade_data and swap BUY for LONG, if data does not exist, it updates to NaN
        "BUY": "LONG",
        "LONG": "LONG",
        "SELL": "SHORT",
        "SHORT": "SHORT"


    }

    clean_trade_data[column_name] = clean_trade_data[column_name].map(direction_map)
    invalid_direction_rows = clean_trade_data[clean_trade_data[column_name].isna()] #not LONG or SHORT by searching for NaN values
    #.map changes the BUY to LONG. if no matches, it changes to Nan!
    clean_trade_data = clean_trade_data[
        ~(clean_trade_data[column_name].isna() # | (clean_trade_data['rule_followed'] == ))
    )].copy()

    return invalid_direction_rows, clean_trade_data

def convert_rule_followed(clean_trade_data, column_name):

    clean_trade_data = clean_trade_data.copy()
    if column_name not in clean_trade_data:
    #if column_name not in clean_trade_data.columns: 
        return f"No {column_name} in data"
    
    clean_trade_data[column_name] = (
        clean_trade_data[column_name].astype(str)
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
    clean_trade_data[column_name] = clean_trade_data[column_name].map(rule_map)
    invalid_rule_rows = clean_trade_data[clean_trade_data[column_name].isna()] #finding rows with NaN 

    clean_trade_data = clean_trade_data[
        ~(clean_trade_data[column_name].isna() # | (clean_trade_data['rule_followed'] == ))
    )].copy()
  
    return invalid_rule_rows, clean_trade_data

def convert_date(clean_trade_data, column_name): 
    clean_trade_data = clean_trade_data.copy()
    if column_name not in clean_trade_data:
    #if column_name not in clean_trade_data.columns: 
        return f"No {column_name} in data"
    
    clean_trade_data[column_name] = pd.to_datetime( 
         clean_trade_data[column_name],errors="coerce", format="mixed", dayfirst=True
        )
    #detect Not a Time for each date first and add to invalid_date_rows
    invalid_date_rows = clean_trade_data[clean_trade_data[column_name].isna()]

    #then create a cleanup copy 
    clean_trade_data = clean_trade_data[
        ~(clean_trade_data[column_name].isna() # | (clean_trade_data['rule_followed'] == ))
    )].copy()
    

    return invalid_date_rows, clean_trade_data


def check_duplicate(clean_trade_data, column_name):
    clean_trade_data = clean_trade_data.copy()
    if column_name not in clean_trade_data:
    #if column_name not in clean_trade_data.columns: 
        return f"No {column_name} in data"
    
    clean_trade_data[column_name] = clean_trade_data[column_name].astype(int)

    duplicate_rows = clean_trade_data[clean_trade_data.duplicated(subset=[column_name], keep='first')] #get the duplicated row in the table
    #and keep in duplicate_rows 
    
    clean_trade_data = clean_trade_data.drop_duplicates(subset=[column_name], keep='first').copy()

    #drop the duplicate rows and make a new copy to return to function caller. 

    return duplicate_rows, clean_trade_data



    