import pandas as pd
from check_col import check_columns
"""
function to validate columns in the df and return true
"""
def loadcsv(CSV_FILE):

    trade_data = pd.read_csv(CSV_FILE)
    #expected data col in DataFrame. checks the captured data. if no
    expected_col = ['trade_id', 'date',  'ticker', 'direction', 'pnl', 'rule_followed', 'main_tag', 'confidence_before_entry', 'one_line_lesson']
    expected_set = set(expected_col)
    captured_set = set(trade_data.columns.tolist())
    
    in_valid, missing_col, extra_col = check_columns(expected_set, captured_set)
    return in_valid, missing_col,extra_col,trade_data
