from sql import connect_db, sql_count ,get_pnl,get_trades
DB_NAME = 'trade.db'
conn = connect_db(DB_NAME)
print(conn)


info = sql_count(conn)
print(info)

pnl = get_pnl(conn)
print(pnl)

get_trade = get_trades(conn)
print(get_trade)