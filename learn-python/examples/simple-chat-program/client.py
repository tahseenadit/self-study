import configparser
import socket
import threading
import time

class ConfigDict(dict):

    def __init__(self):
        config_parser = configparser.ConfigParser()
        config_parser.read("local_config.ini")
        self.server_ip = config_parser["LOCAL_SERVER"]["host"]
        self.server_port = config_parser["LOCAL_SERVER"]["port"]

class Client:

    def _global_config(self):
        cfg = ConfigDict()
        return cfg

    def __init__(self):
        self.config = self._global_config()
        self.server_conf = (self.config.server_ip, int(self.config.server_port))

        # A socket object is created using socket.socket(), specifying AF_INET for IPv4 and SOCK_STREAM for TCP communication.
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def connect(self):
        try:
            self.client.connect(self.server_conf)
            print('Connection succesful made to the server')
            return True
        except Exception as ex:
            print('Exception occured! {}'.format(ex))
            print('\nConnection failed! Trying again...')
    
    
    def send_msg(self):
        while True:
            msg = input()
            self.client.send(msg.encode())
    
    def receive_msg(self):
        while True:
            msg = self.client.recv(1024).decode()
            time.sleep(0.001)
            print("Message from server: {}".format(msg))
    
    def chat(self):
        if self.connect:
            
            '''
            Create a new thread and give the thread the job of handling the receive_msg method

            Don't do it like below:
            new_thread= threading.Thread(target=self.receive_msg()):

            Calling with parentheses: Here, you're calling the self.receive_sms method immediately and passing the return value (likely None) 
            as the target to the thread. This means the thread won't actually execute the receive_sms method inside itself.
            
            '''
            msg_thread = threading.Thread(target=self.receive_msg)
            '''
            Regular thread:

            By default, when the main program finishes, all active non-daemon threads are still running. This means the program doesn't terminate completely 
            until all these threads finish their tasks.
            This behavior is essential when certain tasks within the threads need to complete even after the main program 
            exits (e.g., saving data, cleaning up resources).

            Daemon thread:

            When the main program exits, all actively running daemon threads are automatically stopped. This means the program terminates without 
            waiting for daemon threads to finish their work.
            This behavior is useful for background tasks that are not critical to the overall program functionality and don't need to finish before the 
            program exits (e.g., logging information, monitoring processes).
            
            '''
            msg_thread.daemon = False
            msg_thread.start()
            self.send_msg()



if __name__ == '__main__':
    client1 = Client()
    client1.chat()

