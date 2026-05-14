from sql import connect_db, sql_count, get_pnl, get_trades


DB_NAME = "trade.db"
trade_list = []
#connect db 
conn = connect_db(DB_NAME)

trades = get_trades(conn)
conn.close()
count = 1 #using counter as vector row id 

#create document 
for row in trades:
    #return tuple
    #prepping for dict 
    #(1, '2026-05-01', 'USAR', 'LONG', 100.0, 'YES', 'followed_plan', 'High', 'I waited for the setup and exited well')
    trade_info = {    

        "id": "trade_" + str(count),
        #strip whitespace.
        "document" : f"""Trade ID: {row[0]} Date: {row[1]}Ticker: row[2]Direction: {row[3]}PnL: {row[4]}Rule Followed: {row[5]}Main Tag: {row[6]}Confidence Before Entry: {row[7]}Lesson: {row[8]}""".strip(),
        "metadata" : {
            "trade_id": row[0],
            "date": row[1],
            "ticker": row[2],
            "direction": row[3],
            "pnl": row[4],
            "rule_followed": row[5],
            "main_tag": row[6]
            }
        }
    trade_list.append(trade_info)
    count += 1

print(trade_list[0])
print(len(trade_list))
for item in trade_list:
    print(item["id"], item["metadata"]["trade_id"])