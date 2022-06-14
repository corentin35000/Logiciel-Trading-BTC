from telethon import TelegramClient, events, sync
import MetaTrader5 as mt5
import socket
import messageTelegram


# establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(login=745084, server="PacificUnionLLC-Demo", password="O03LibQ4"):
    print("initialize() failed, error code =", mt5.last_error())
    mt5.shutdown()
    quit()


# Sockets python natif
class SocketServer:
    def __init__(self, address='', port=9090):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port
        self.sock.bind((self.address, self.port))
        self.cummdata = ''

    def waitforconnection(self):
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        print('connected to', self.addr)
        return 1

    def recvmsg(self):
        self.cummdata = ''
        while True:
            data = self.conn.recv(10000)
            self.cummdata += data.decode("utf-8")
            if not data:
                break

            self.conn.send(bytes(self.cummdata, "utf-8"))  # loop back test

            return self.cummdata

    def __del__(self):
        print('sock close')
        self.sock.close()


serv = SocketServer('192.168.1.48', 9090)
serv.waitforconnection()


# Data Telegram
api_id = 9149209
api_hash = 'c5cf73353e06ce2732cd052ac34c9e0c'
client = TelegramClient('session_name', api_id, api_hash)

# TELEGRAM
@client.on(events.NewMessage(chats='Test35000'))
async def my_event_handler(event):
    # Affiche le message complet qui était recue sur le canal telegram.
    print("-----------------NEW MESSAGE ---------------")
    print(event.raw_text)
    print("-----------------END MESSAGE ---------------")

    # Check messages
    if messageTelegram.check_new_signaux(event):
        print("FAIRE TACHE")

client.start()
client.run_until_disconnected()
