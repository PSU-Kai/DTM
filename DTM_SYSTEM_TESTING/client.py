import socket
import glob

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    """ Starting a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    """ Finding all CSV files with 'SimOut' in the 'data' directory. """
    file_paths = glob.glob("data/*SimOut*.csv")
    for file_path in file_paths:
        """ Opening and reading the file data. """
        file = open(file_path, "r")
        data = file.read()

        """ Sending the filename to the server. """
        filename = file_path.split("/")[-1]  # Extract the filename from the file path
        client.send(filename.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Sending the file data to the server. """
        client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Closing the file. """
        file.close()

    """ Closing the connection from the server. """
    client.close()


if __name__ == "__main__":
    main()
