#coding=utf-8

import trade_ut as trade
import api_ut as api
import time
import matplotlib.pyplot as plt

def test_sell(pair, qty, sell_price):
    sell_id = trade.trusted_sell(pair, qty, sell_price)
    return sell_id

def main():
    # BTCUSDT, ETHUSDT, LTCUSDT
    # price, qty, timestamp = trade.get_trades('LTCUSDT')
    # print(len(price))
    # plt.figure()
    # plt.plot(timestamp, price)
    # plt.show()

    # test account balances
    balance = trade.trusted_get_account_balance()
    print balance['USDT']
    print balance['LTC']

    # sell_id = test_sell('LTCUSDT', '0.0011', '500')
    # print "selling~, id= "+str(sell_id)
    # coin = 'LTCUSDT'
    # print trade.get_last_price(coin.split('USDT')[0])
    # result = api.get_open_orders('LTCUSDT')
    # for i in result:
    #     print i
    #     order_id = i['order_id']
    #     print order_id
        # print trade.trusted_get_open_orders('LTCUSDT', 123123)
        # print trade.trusted_cancel_order('LTCUSDT', order_id)
        # print trade.test_order_closed('LTCUSDT', order_id, 3)
    # sell_time = time.time() + 6#00
    # while True:
    #     if 1<0 or time.time()>sell_time:
    #         print 'ha'
    #         break


if __name__ == '__main__':
    main()
