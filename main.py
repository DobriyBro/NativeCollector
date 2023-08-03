from web3 import Web3
print ("\n\n\n╔══╗╔═══╗╔╗╔╗╔═══╗╔════╗╔══╗╔══╗╔╗──╔╗──╔═══╗╔╗╔╗")
print ("║╔═╝║╔═╗║║║║║║╔═╗║╚═╗╔═╝║╔╗║║╔╗║║║──║║──║╔══╝║║║║")
print ("║║──║╚═╝║║╚╝║║╚═╝║──║║──║║║║║╚╝║║║──║║──║╚══╗║╚╝║")
print ("║║──║╔╗╔╝╚═╗║║╔══╝──║║──║║║║║╔╗║║║──║║──║╔══╝╚═╗║")
print ("║╚═╗║║║║──╔╝║║║─────║║──║╚╝║║║║║║╚═╗║╚═╗║╚══╗─╔╝║")
print ("╚══╝╚╝╚╝──╚═╝╚╝─────╚╝──╚══╝╚╝╚╝╚══╝╚══╝╚═══╝─╚═╝\n\n")
print ("t.me/crypt0alley\n\n")
file = open("private.txt", "r")
file1 = open("address.txt", "r")
# Загрузка аккаунта получателя
print ("Введите адрес получателя: \n")
reciever_adress = input()
reciever_adress = Web3.to_checksum_address(reciever_adress)
a = 1
b = len(open('address.txt').readlines())

while True:

    sender_address = file1.readline()

    sender_address = sender_address.replace("\n","")

    sender_private_key = file.readline()

    sender_private_key = sender_private_key.replace("\n","")

    if not sender_address:
        break

    if not sender_private_key:
        break
    #Подключение к блокчейну (указывается URL узла)
    web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed3.binance.org'))
    gas = (web3.eth.gas_price)

    sender_address = Web3.to_checksum_address(sender_address)

    # Проверка баланса
    balance = web3.eth.get_balance(sender_address)
    totalgas = gas*31500
    balance_gas = (balance - totalgas)

    # Проверка условия, что баланс не кошельке больше, чем стоимость комиссии

    if (balance_gas > 0):
        # Получение текущего номера блока
        nonce = web3.eth.get_transaction_count(sender_address)

        # Создание транзакции
        transaction = {
            'to': reciever_adress,
            'value': int(balance_gas),
            'gas': 31500,
            'gasPrice': gas,
            'nonce': nonce,
        }

        # Подпись транзакции
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)

        # Отправка транзакции
        transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Ожидание подтверждения транзакции
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)




    web3 = Web3(Web3.HTTPProvider('https://rpc.arb1.arbitrum.gateway.fm'))
    gas = (web3.eth.gas_price)

    sender_address = Web3.to_checksum_address(sender_address)

    # Проверка баланса
    balance = web3.eth.get_balance(sender_address)
    totalgas = gas * 320362
    balance_gas = (balance - totalgas)

    # Проверка условия, что баланс не кошельке больше, чем стоимость комиссии
    if (balance_gas > 0):
        # Получение текущего номера блока
        nonce = web3.eth.get_transaction_count(sender_address)

        # Создание транзакции
        transaction = {
            'to': reciever_adress,
            'value': int(balance_gas),
            'gas': 320362,
            'gasPrice': gas,
            'nonce': nonce,
        }

        # Подпись транзакции
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)

        # Отправка транзакции
        transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Ожидание подтверждения транзакции
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)




    web3 = Web3(Web3.HTTPProvider('https://rpc-mainnet.matic.quiknode.pro'))
    gas = (web3.eth.gas_price)

    sender_address = Web3.to_checksum_address(sender_address)

    # Проверка баланса
    balance = web3.eth.get_balance(sender_address)
    totalgas = gas * 315000
    balance_gas = (balance - totalgas)

    # Проверка условия, что баланс не кошельке больше, чем стоимость комиссии
    if (balance_gas > 0):
        # Получение текущего номера блока
        nonce = web3.eth.get_transaction_count(sender_address)

        # Создание транзакции
        transaction = {
            'to': reciever_adress,
            'value': int(balance_gas),
            'gas': 315000,
            'gasPrice': gas,
            'nonce': nonce,
            'chainId': 137
        }

        # Подпись транзакции
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)

        # Отправка транзакции
        transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Ожидание подтверждения транзакции
        # transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)




    web3 = Web3(Web3.HTTPProvider('https://optimism.publicnode.com'))
    gas = (web3.eth.gas_price)

    sender_address = Web3.to_checksum_address(sender_address)

    # Проверка баланса
    balance = web3.eth.get_balance(sender_address)
    totalgas = gas * 350000
    balance_gas = (balance - totalgas)


    # Проверка условия, что баланс не кошельке больше, чем стоимость комиссии
    if (balance_gas > 0):
        # Получение текущего номера блока
        nonce = web3.eth.get_transaction_count(sender_address)

        # Создание транзакции
        transaction = {
            'to': reciever_adress,
            'value': int(balance_gas),
            'gas': 31500,
            'gasPrice': gas,
            'nonce': nonce,
            'chainId': 10
        }

        # Подпись транзакции
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)

        # Отправка транзакции
        transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Ожидание подтверждения транзакции
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
    web3 = Web3(Web3.HTTPProvider('https://optimism.publicnode.com'))
    gas = (web3.eth.gas_price)

    sender_address = Web3.to_checksum_address(sender_address)

    # Проверка баланса
    balance = web3.eth.get_balance(sender_address)
    totalgas = gas * 350000
    balance_gas = (balance - totalgas)


    # Проверка условия, что баланс не кошельке больше, чем стоимость комиссии
    if (balance_gas > 0):
        # Получение текущего номера блока
        nonce = web3.eth.get_transaction_count(sender_address)

        # Создание транзакции
        transaction = {
            'to': reciever_adress,
            'value': int(balance_gas),
            'gas': 31500,
            'gasPrice': gas,
            'nonce': nonce,
            'chainId': 10
        }

        # Подпись транзакции
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)

        # Отправка транзакции
        transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Ожидание подтверждения транзакции
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)



    web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/avalanche'))
    gas = (web3.eth.gas_price)

    sender_address = Web3.to_checksum_address(sender_address)

    # Проверка баланса
    balance = web3.eth.get_balance(sender_address)
    totalgas = gas * 31500
    balance_gas = (balance - totalgas)


    # Проверка условия, что баланс не кошельке больше, чем стоимость комиссии
    if (balance_gas > 0):
        # Получение текущего номера блока
        nonce = web3.eth.get_transaction_count(sender_address)

        # Создание транзакции
        transaction = {
            'to': reciever_adress,
            'value': int(balance_gas),
            'gas': 31500,
            'gasPrice': gas,
            'nonce': nonce,
            'chainId': 43114
        }

        # Подпись транзакции
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)

        # Отправка транзакции
        transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Ожидание подтверждения транзакции
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)

        print (a, "/", b, "Завершено")
        a = a + 1
print("Готово")
input()