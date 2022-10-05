import sys
import requests
import json

# rpc_user = "benjamin"
# rpc_password = "test123456"
token="YmVuamFtaW46dGVzdDEyMzQ1Ng=="

url = 'http://127.0.0.1:8332'

def initialize_app():
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:] # First element of args is the file name
    if len(args) == 0:
        print('You have not passed any commands in!')
    else:
        for a in args:
            if a == '--help':
                print('Basic command line program')
                print('Options:')
                print('    --help -> show this basic help menu.')
                print('    balance -> Get you wallet balance')
                print('    send -> Transfer Bitcoins')
                print('    create_addr -> Create a new address')
                print('    unspent -> List the unspent transactions')
            elif a=='create_wallet':
                create_wallet(args[1])
            elif a =='balance':
                check_balance(args[1])
            elif a =='send':
                transfer_bitcoins(args[1], args[2], args[3])
            elif a =='create_address':
                create_new_address(args[1])
            elif a =='unspent':
                list_unspent_transactions(args[1])
            elif a =='generate':
                generate(args[1], args[2])
            else:
                print('')

def create_wallet(wallet):
    headers = {
            "Authorization": "Basic " + token,
            "Content-Type": "text/plain"
         }
    data = {
        "method": "createwallet",
        "params": [wallet]
    }
    
    request = requests.post(url, headers=headers, data=json.dumps(data))
    if request.status_code == 200:
        print("Wallet successfully created")
    else:
        print("Wallet already exists")
        print(request.content)

    
def check_balance(wallet):
    headers = {
            "Authorization": "Basic " + token,
            "Content-Type": "text/plain"
         }
    data = {
        "method": "getbalance",
        "params": []
    }
    
    print(json.loads(requests.post(url+"/wallet/"+wallet, headers=headers, data=json.dumps(data)).content))
     

def create_new_address(wallet):
    # getnewaddress
    headers = {
            "Authorization": "Basic " + token,
            "Content-Type": "text/plain"
         }
    data = {
        "method": "getnewaddress",
        "params": []
    }

    print("Address created: " + str(json.loads(requests.post(url+"/wallet/"+wallet, headers=headers, data=json.dumps(data)).content)['result']))

def transfer_bitcoins(wallet, address, amount):
    # sendtoaddress
    headers = {
            "Authorization": "Basic " + token,
            "Content-Type": "text/plain"
         }
    data = {
        "method": "sendtoaddress",
        "params": [address, amount]
    }

    print(json.loads(requests.post(url+"/wallet/"+wallet, headers=headers, data=json.dumps(data)).content))

def list_unspent_transactions(wallet):
    # listunspent
    headers = {
            "Authorization": "Basic " + token,
            "Content-Type": "text/plain"
         }
    data = {
        "method": "listunspent",
        "params": []
    }

    for entry in json.loads(requests.post(url+"/wallet/"+wallet, headers=headers, data=json.dumps(data)).content)['result']:
        print(entry['amount'])

def generate(wallet, amount):
    # listunspent
    headers = {
            "Authorization": "Basic " + token,
            "Content-Type": "text/plain"
         }
    data = {
        "method": "generate",
        "params": [amount]
    }

    print(json.loads(requests.post(url+"/wallet/"+wallet, headers=headers, data=json.dumps(data)).content))


if __name__ == '__main__':
	initialize_app()