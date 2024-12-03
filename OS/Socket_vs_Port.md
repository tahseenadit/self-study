The combination of an IP address and a port is strictly known as an endpoint and is sometimes called a socket. This usage originates with RFC793, the original TCP specification.

A TCP connection is defined by two endpoints aka sockets. It is the socket pair (the 4-tuple consisting of the client IP address, client port number, server IP address, and server port number) that specifies the two endpoints that uniquely identifies each TCP connection in an internet. (TCP-IP Illustrated Volume 1, W. Richard Stevens)

An endpoint (socket) is defined by the combination of a network address and a port identifier. Note that address/port does not completely identify a socket. 

### A Connection Needs Two Sockets
A TCP connection involves two endpoints:
- The IP address and port number of the local machine.
- The IP address and port number of the remote machine.

Together, these form a "pair" that uniquely identifies the connection. This pair is also called a 4-tuple:
(Client IP, Client Port, Server IP, Server Port)

### The Role of Listener Sockets
A listener socket is a special type of socket that is in the listen state:

It "waits" for incoming connection requests on a specific IP address and port combination.
It is the only socket for a particular IP/port combination that can accept new connections.
When a connection is established:

The listener socket does not itself handle the communication.
Instead, a new socket is created for each incoming connection. This new socket is uniquely identified by the 4-tuple (source IP, source port, destination IP, destination port).

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

---

### **1. Example?**
You used the command `netstat` to list active TCP connections on your workstation. The output shows multiple active connections between your local machine (**192.168.1.3**) and remote servers (**54.252.94.236** and **207.38.110.62**) on port **80** (HTTP).

Here’s a snippet:
```
TCP    192.168.1.3:63240      54.252.94.236:80       SYN_SENT
TCP    192.168.1.3:63241      54.252.94.236:80       SYN_SENT
```
- Both lines are connections to the same **remote address and port**: `54.252.94.236:80`.
- However, they are separate connections because they use **different local port numbers**: `63240` and `63241`.

This illustrates that **address and port alone are not enough to uniquely identify a socket**.

---

### **2. Why Address and Port Aren’t Enough**
If you look only at the **destination address and port** (`54.252.94.236:80`), both connections would seem identical. But TCP needs to distinguish between the two, and it does so using the **source address and port** as well.

A **socket** is identified by a **4-tuple**:
1. **Source IP Address**: Your local machine's address (192.168.1.3).
2. **Source Port**: The port your machine uses for the connection (e.g., 63240 or 63241).
3. **Destination IP Address**: The remote server's address (54.252.94.236).
4. **Destination Port**: The port on the remote server (80 for HTTP).

This 4-tuple is unique for every connection.

In your example:
- Connection 1: `(192.168.1.3, 63240, 54.252.94.236, 80)`
- Connection 2: `(192.168.1.3, 63241, 54.252.94.236, 80)`

Each connection is distinct because their **source ports** are different.

---

### **3. What This Means for Sockets**
- A **socket** is an endpoint in the connection, and it's defined by the combination of an IP address and a port.
- A **connection** requires two sockets (local and remote), and it is uniquely identified by the **4-tuple**.

In the example:
- On the server side (`54.252.94.236:80`), there’s **one listening socket** for all incoming connections.
- For each incoming connection, the server creates a **new socket** identified by the 4-tuple of the connection (including the client’s source IP and port).

---
---

### **4. What the RFC Defines as a Socket**
- According to the original RFC 793 (the TCP specification), a **socket** is a combination of:
  - An **IP address** (e.g., 192.168.1.3)
  - A **port number** (e.g., 63240)

Thus, in this sense:
- A socket is just one endpoint in a TCP connection.
- A TCP **connection** has two sockets: one on the local side and one on the remote side.

Example for a connection:
- Local socket: `(192.168.1.3, 63240)`
- Remote socket: `(54.252.94.236, 80)`

Together, these two sockets form the **two endpoints** of the TCP connection.

---

### **5. Real-World APIs and "Socket Objects"**
When you use programming libraries or APIs (e.g., in C, Python, or Java), they often provide a **socket object** to represent the connection. This can cause confusion because:
- The socket object doesn’t just represent the **local socket** (as per the RFC definition).
- Instead, it represents the **entire connection** (including both endpoints).

When an API gives you a new socket object for each connection, it might feel inconsistent with the RFC definition. However, this is because:
1. **Local Ports**: The API assigns a new, unique **source port** for each outgoing connection to avoid conflicts, even if you're connecting to different remote destinations. This behavior is practical, even though the RFC allows the reuse of source ports as long as the destination is different.
2. **Connection Context**: The socket object in APIs includes the context of the connection, not just the local address/port.

---

### **6. Reuse of Source Ports**
According to the RFC:
- It’s allowed to reuse the **same source port** for multiple connections, provided the destination address and/or port is different. This works because each connection is uniquely identified by the **4-tuple** (source IP, source port, destination IP, destination port).
- Example:
  - Connection 1: `(192.168.1.3, 50000) → (54.252.94.236, 80)`
  - Connection 2: `(192.168.1.3, 50000) → (207.38.110.62, 80)`

In practice:
- Many APIs choose **not to reuse source ports**, even when allowed by the RFC. They dynamically assign a new source port for each outgoing connection.
- This behavior simplifies connection management and reduces the chances of port conflicts, especially in systems that handle many simultaneous connections.

---

### **7. Why APIs Behave This Way**
1. **Practicality**:
   - If you reuse the same source port, you need to ensure there’s no conflict in the active 4-tuples. Managing this can be complex, especially in high-traffic scenarios.
   - By assigning a new source port for each connection, the system avoids accidental overlaps.
   
2. **Port Exhaustion is Rare**:
   - There are 65,536 ports available (0–65535). For most applications, dynamically assigning a new port for each connection doesn’t lead to port exhaustion, even with thousands of connections.

3. **Consistency**:
   - APIs abstract the complexity of managing TCP connections. Assigning a unique source port for every new connection simplifies the developer’s experience, even if it diverges slightly from the RFC’s allowances.

---
