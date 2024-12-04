### **1. What is a ZMQ_STREAM Socket?**
- A **ZMQ_STREAM socket** is a type of socket provided by the **ZeroMQ (ZMQ)** messaging library.
- It is designed to interact with **non-ØMQ peers**, meaning it communicates with systems that don’t use ZeroMQ but instead rely on plain TCP.

### **2. Dual Role: Client and Server**
A ZMQ_STREAM socket can:
- Act as a **client**, initiating a connection to a TCP server.
- Act as a **server**, accepting connections from TCP clients.
- It can do both simultaneously, handling multiple peers.

---

### **3. Receiving Data**
When a ZMQ_STREAM socket **receives TCP data**:
1. **Identity Prepended**: Before passing the received data to your application, the socket prepends a message part that identifies the peer (the TCP client or server that sent the data).
   - This identity is a unique identifier for the peer.
   - It allows the application to know which peer the data came from.
2. **Fair Queuing**: If multiple peers are connected, the ZMQ_STREAM socket ensures **fair queuing**:
   - It doesn’t prioritize one peer over another.
   - Data is read from all peers in a round-robin or balanced fashion.

---

### **4. Sending Data**
When a ZMQ_STREAM socket **sends data**:
1. **First Message Part**: The application must prepend the data with the peer’s identity (the same identity received in incoming messages).
   - This tells the ZMQ_STREAM socket which connected peer the data should be sent to.
2. **Routing the Message**:
   - If the peer identity is valid, the socket routes the message to the correct peer.
   - If the peer identity is invalid (e.g., the peer is not connected), one of the following errors occurs:
     - **EHOSTUNREACH**: The destination is unreachable (e.g., the peer has disconnected).
     - **EAGAIN**: The message couldn’t be sent immediately (e.g., the socket is non-blocking, and the send buffer is full).

---

### **5. Use Case: Communicating with Non-ØMQ Peers**
- This socket type allows ZeroMQ-based systems to communicate with TCP-based systems that don’t use ZeroMQ protocols.
- The added identity mechanism simplifies handling multiple connections because it ensures the application knows where each message came from and can route responses to the correct peer.

---
