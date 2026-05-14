"""
main df cleaner 
"""
from clean_fun import (
    convert_upper,
    convert_direction,
    convert_rule_followed,
    convert_numeric,
    convert_to_caps,
    clean_row,
    convert_date,
    check_duplicate,
)

def  main_clean(trade_data):

    invalid_tickers, ticker_upper = convert_upper(trade_data)   
    invalid_dir, check_dir_col = convert_direction(ticker_upper, "direction")
    invalid_rules, rules_to_caps = convert_to_caps(check_dir_col, "rule_followed")
    invalid_rows, clean_up_rows = convert_rule_followed(rules_to_caps, "rule_followed")
    invalid_pnl, clean_up_pnl = clean_row(clean_up_rows,"pnl")
    invalid_num, clean_up_nums = convert_numeric(clean_up_pnl, "pnl")
    invalid_date, clean_up_date = convert_date(clean_up_nums, "date")
    invalid_trade, clean_up_trade = check_duplicate(clean_up_date, "trade_id")

    #return invalid information
    invalid_data = {

        "invalid_tickers": invalid_tickers,
        "invalid_dir": invalid_dir,
        "invalid_rules": invalid_rules,
        "invalid_rows": invalid_rows,
        "invalid_pnl": invalid_pnl,
        "invalid_num": invalid_num,
        "invalid_date": invalid_date,
        "invalid_trade": invalid_trade,
    }

    return clean_up_trade, invalid_data