The combination of an IP address and a port is strictly known as an endpoint and is sometimes called a socket. This usage originates with RFC793, the original TCP specification.

A TCP connection is defined by two endpoints aka sockets. It is the socket pair (the 4-tuple consisting of the client IP address, client port number, server IP address, and server port number) that specifies the two endpoints that uniquely identifies each TCP connection in an internet. (TCP-IP Illustrated Volume 1, W. Richard Stevens)

An endpoint (socket) is defined by the combination of a network address and a port identifier. Note that address/port does not completely identify a socket. 

### A Connection Needs Two Sockets
A TCP connection involves two endpoints:
- The IP address and port number of the local machine.
- The IP address and port number of the remote machine.

Together, these form a "pair" that uniquely identifies the connection. This pair is also called a 4-tuple:
(Client IP, Client Port, Server IP, Server Port)

### **1. What is a Network Address?**
A **network address** (like an IP address) is like the "street address" of a device on a network. It tells other devices where to send data. However, an IP address alone doesn’t specify *which service* or application on the device should receive the data.

### **2. What is a Port?**
A **port** is like an "apartment number" at the network address. It helps differentiate between different services running on the same device. For example:
- **Port 80**: Typically used for web traffic (HTTP).
- **Port 25**: Typically used for email (SMTP).

By using ports, a device can host many services at the same time. Each service is assigned a different port, like rooms in a building.

### **3. Virtualisation of Endpoints**
Ports allow the **same network address** (IP address) to handle **multiple endpoints** (services or applications) at the same time. This is why we call ports "virtualised endpoints":
- A **physical network interface** (like a network card) has one IP address, but it can handle many connections at once because of ports.
- Without ports, a device could only handle one connection per network address.

### **4. Multiple Concurrent Connections**
When multiple clients (like users visiting a website) connect to the same server, this is possible because:
- Each client is assigned a unique combination of **IP address and port number** on their end.
- The server distinguishes these connections using the **4-tuple** (Client IP, Client Port, Server IP, Server Port).

### **Example**
Imagine a web server with IP address **192.168.1.1**:
- User A connects to the server on **port 80** for HTTP. User A's connection is identified by:
  - Client: (192.168.1.100, 34567)
  - Server: (192.168.1.1, 80)
- User B also connects to the server on **port 80** for HTTP. User B's connection is identified by:
  - Client: (192.168.1.101, 45678)
  - Server: (192.168.1.1, 80)

Both users can connect at the same time because their connections are uniquely identified by their 4-tuple (local and remote IP/port pair).

- Ports let one network address (IP) host multiple services (web, email, etc.) simultaneously.
- Ports also allow multiple users to connect to the same service without interference.
- This system of differentiation is what we mean by **virtualised endpoints**.

### Why the Confusion?
The confusion arises because many programming libraries (e.g., in C, Python, Java) use the term socket object to represent:

- Both the listener socket (for accepting connections).
- And the connection socket (for handling an established connection).

However, these two types of sockets are conceptually different:

- The listener socket is tied to a specific IP address and port and listens for incoming connections.
- The connection socket is dynamically created for each established connection and is defined by the unique 4-tuple.
