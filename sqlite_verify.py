from sql import connect_db, sql_count, get_pnl, get_trades


DB_NAME = "trade.db"


conn = connect_db(DB_NAME)

trade_count = sql_count(conn)
print("Trade count:", trade_count)

total_pnl = get_pnl(conn)
print("Total PnL:", total_pnl)

trades = get_trades(conn)
print("Trades:")
print(trades)

conn.close()