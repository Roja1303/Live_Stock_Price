from SharekhanApi.sharekhanConnect import SharekhanConnect

api_key = "Your Api Key"
login = SharekhanConnect(api_key)
vendor_key = ""         # vendor key for vendor login otherwise keep it null
version_id = ""         # version id= 1005 or 1006 otherwise keep it null
state=12345
url = login.login_url(vendor_key, version_id)
print(url)

request_token="Your request token value after login"
secret_key="Your Secret key"

"""Use generate session method when you are passing version id """
session=login.generate_session(request_token,secret_key)
# Generating access token for version id and pass parameters as it is passed below
access_token=login.get_access_token(api_key,session,state,versionId=version_id)

"""Use generate session without version id method when you are not passing version id """
sessionwithoutvesionId=login.generate_session_without_versionId(request_token,secret_key)
# Generating access token for without version id
access_token=login.get_access_token(api_key,sessionwithoutvesionId,state)

print(access_token)
access_token = "Your access token value"
sharekhan = SharekhanConnect(api_key=api_key,access_token=access_token)
print(sharekhan.requestHeaders())       # for printing request headers


# Place order history

orderparams={
 "customerId": "XXXXXXX",
 "scripCode": 2475,
 "tradingSymbol": "ONGC",
 "exchange": "NC",
 "transactionType": "B",
 "quantity": 1,
 "disclosedQty": 0,
 "price": "149.5",
 "triggerPrice": "0",
 "rmsCode": "ANY",
 "afterHour": "N",
 "orderType": "NORMAL",
 "channelUser": "XXXXXXX",
 "validity": "GFD",
 "requestType": "NEW",
 "productType": "INVESTMENT"
}
order=sharekhan.placeOrder(orderparams)
print("PlaceOrder: {}".format(order))

# modify order

orderparams={
 "orderId":"XXXXXXXXXXX",
    "customerId": "XXXXXXX",
    "scripCode": 2475,
    "tradingSymbol": "ONGC",
    "exchange": "NC",
    "transactionType": "B",
    "quantity": 1,
    "disclosedQty": 0,
    "price": "149.5",
    "triggerPrice": "0",
    "rmsCode": "SKSIMNSE1",
    "afterHour": "N",
    "orderType": "NORMAL",
    "channelUser": "XXXXXXX",
    "validity": "GFD",
    "requestType": "MODIFY",
    "productType": "INVESTMENT"
    }
order=sharekhan.modifyOrder(orderparams)
print("ModifyOrder: {}".format(order))

# cancel  order

orderparams={
 "orderId":"XXXXXXX",
 "customerId": "XXXXXXX",
 "scripCode": 2475,
 "tradingSymbol": "ONGC",
 "exchange": "NC",
 "transactionType": "B",
 "quantity": 1,
 "disclosedQty": 0,
 "price": "145.5",
 "triggerPrice": "0",
 "rmsCode": "SKSIMNSE1",
 "afterHour": "N",
 "orderType": "NORMAL",
 "channelUser": "XXXXXXX",
 "validity": "GFD",
 "requestType": "CANCEL",
 "productType": "INVESTMENT"
}
order=sharekhan.cancelOrder(orderparams)
print("CancelOrder: {}".format(order))

# Fund details

exchange="MX"
customerId="customerId <int data type>"
order=sharekhan.funds(exchange, customerId)
print("Fund Details : {}".format(order))

# Retrieves all orders for the day

customerId="customerId <int data type>"
order=sharekhan.reports(customerId)
print("Order Reports: {}".format(order))

#Retrieve history of an given order

exchange="RN"
customerId="customerId <int data type>"
orderId=1234567
order=sharekhan.exchange(exchange, customerId, orderId)
print("Order Details: {}".format(order))


# Retrieves all positions

customerId="customerId <int data type>"
order=sharekhan.trades(customerId)
print("Postion Reports: {}".format(order))


# Retrieves the trade  generated by an order

exchange="NC"
customerId="customerId <int data type>"
orderId=585194484
order=sharekhan.exchangetrades(exchange, customerId, orderId)
print("Trade Generated By an Order : {}".format(order))

# services Holdings

customerId="customerId <int data type>"
order=sharekhan.holdings(customerId)
print("Holdings : {}".format(order))

#Script Master

exchange="MX"
order=sharekhan.master(exchange)
print("Script Master : {}".format(order))

# # Historical Data

exchange="BC"
scripcode=500410
interval="daily"
order=sharekhan.historicaldata(exchange, scripcode, interval)
print("Historical Data: {}".format(order))


# websocket Programming Testing

from SharekhanApi.sharekhanWebsocket import SharekhanWebSocket

params = {
    "access_token": access_token
}

token_list = {"action": "subscribe", "key": ["feed"], "value": [""]}
feed = {"action": "feed", "key": ["depth"], "value": ["MX250715"]}
unsubscribefeed = {"action":"unsubscribe","key":["feed"],"value":["NC22,NF37833,NF37834,MX253461,RN7719"]}

sws = SharekhanWebSocket(access_token)


def on_data(wsapp, message):
    print("Ticks: {}".format(message))


def on_open(wsapp):
    print("on open")
    sws.subscribe(token_list)
    sws.fetchData(feed)
    # sws.unsubscribe(feed)
    # sws.close_connection()


def on_error(wsapp, error):
    print(error)


def on_close(wsapp):
    print("Close")


# Assign the callbacks.
sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error
sws.on_close = on_close

sws.connect()
