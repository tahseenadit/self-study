# Problem: Multiple instance creation

```python
import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])
print(f"main.py with :{app}")


@app.get('/')
def home():
    return "Hello"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, log_level="debug", debug=True,
                workers=1, limit_concurrency=1, limit_max_requests=1)
```
Console output:

```
/Users/user/.pyenv/versions/3.7.10/bin/python /Users/user/github/my-project/backend/main.py
main.py with :<fastapi.applications.FastAPI object at 0x102b35d50>
INFO:     Will watch for changes in these directories: ['/Users/user/github/my-project/backend']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [96259] using statreload
main.py with :<fastapi.applications.FastAPI object at 0x10daadf50>
main.py with :<fastapi.applications.FastAPI object at 0x1106bfe50>
INFO:     Started server process [96261]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Reason

In the log one can indeed see that you have 3 different memory adresses 0x102b35d50, 0x10daadf50, 0x1106bfe50

This doesn't mean that you have 3 workers, just that the FastAPI object is created 3 times. The last one this the one that your API will use.

### Why it happens

The object is created multiple times, because :

First, you run main.py that go through the all code (one creation of FastAPI object), and then reach the __main__
Then uvicorn launch main:app so it go once again to the file main.py and build another FastAPI object.
The last one is created by the debug=True when you set it to False you have one less FastAPI object created. I'm not quite sure why.
The solution

The solution is to separate the API definition from the start of the API.

For example, one could create a run.py file with :

```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, log_level="debug", debug=True,
                workers=1, limit_concurrency=1, limit_max_requests=1)
```

and launch this file.

Another option would be to launch your API in command line:

```
uvicorn main:app --host=0.0.0.0 --port=8000 --log-level=debug --limit-max-requests=1 --limit-concurrency=1
```

# Problem: calling api endpoints from postman using 0.0.0.0

### Understanding `0.0.0.0`

1. **Binding to All Interfaces**:
   - When you run a server (like Uvicorn) and specify `0.0.0.0` as the bind address, it means that the server will listen for incoming connections on **all available network interfaces** on that machine. This includes:
     - The loopback interface (localhost, 127.0.0.1)
     - Any local area network (LAN) interfaces
     - Any other network interfaces that may be configured on the server (like Wi-Fi, Ethernet, etc.)

2. **Network Routing**:
   - While `0.0.0.0` allows the server to accept connections from any IP address within the server itself, it does **not** function as a valid address for accessing the server from another machine. 
   - To connect to the server from another machine (like the one where you're running Postman), you need to use the **actual IP address** assigned to the server's network interface that is reachable over the network.

### Example Scenario

- **Server Configuration**:
  - Suppose your server has two network interfaces: one with IP `192.168.1.10` (LAN) and one with IP `10.0.0.5` (another network).
  - Running Uvicorn with `0.0.0.0` means it will listen for requests on both interfaces (`192.168.1.10` and `10.0.0.5`), as well as on `127.0.0.1`.

- **Client Connection**:
  - If you want to test the API from another machine (running Postman), you would use `192.168.1.10` or `10.0.0.5` in Postman, depending on which network the client is on.
  - Using `127.0.0.1` or `0.0.0.0` on the postman machine would not work because those addresses refer to the local loopback interface of the server machine.

### Summary
- **`0.0.0.0`**: Binds the server to listen on all network interfaces on the server machine.
- **Accessing the Server**: To connect from a client (like Postman), use the server's actual IP address on the network, not `0.0.0.0` or `127.0.0.1`.

# Problem: Connectoin issue

1. **EHOSTUNREACH Error**:
   - The error message `EHOSTUNREACH` indicates that the host (in this case, `192.168.2.84` on port `8000`) is unreachable. This typically means that the network request cannot be completed because:
     - The IP address is not reachable from the client machine.
     - There might be firewall rules blocking the connection.
     - The server is not running or listening on that address.

2. **No Output in the Backend's Console**:
   - This means that when you tried to make the request, the server (Uvicorn) did not log any incoming request, which suggests that it did not receive the request at all.

3. **Verifying Firewall Settings**:
   - **Firewall**: A firewall is a security system that controls incoming and outgoing network traffic based on predetermined security rules. It acts as a barrier between a trusted internal network and untrusted external networks (like the internet).
   - **Check if the Firewall is Open for the Port**: You should ensure that the port your server is listening on (port `8000` in this case) is allowed through the firewall. This can usually be done by checking the firewall settings on the backend machine:
     - On Linux, you might use `iptables` or `ufw` to check rules.
     - On Windows, you would check the Windows Firewall settings.
   - **Including This Information**: When asking for help, it’s important to mention whether the firewall is configured correctly, as this is a common source of connectivity issues.

4. **Using Curl and Browser to Verify**:
   - **Curl**: `curl` is a command-line tool used to make HTTP requests. It can help you check if the server is reachable and responding without needing a GUI tool like Postman.
     - You can run a command like `curl http://192.168.2.84:8000` in your terminal to see if you get a response.
   - **Browser**: You can also paste `http://192.168.2.84:8000` into your web browser’s address bar to check if the server is reachable.
   - **Purpose**: This helps rule out whether the issue is specific to Postman or if it’s a broader connectivity issue.

5. **Understanding the Setup**:
   - **Physically Different Machines vs. VMs**:
     - **Physically Different Machines**: This means that the machines (one running the backend server and one running Postman) are separate, distinct hardware devices.
     - **VMs (Virtual Machines)**: If both the server and client are running on virtual machines, they could be using network configurations such as NAT (Network Address Translation). NAT allows multiple devices on a local network to share a single public IP address. This can introduce additional network configuration considerations.
   - **Same Subnet**: A subnet is a segmented piece of a larger network. If the backend machine (server) and the client machine (running Postman) are on the same subnet, they can communicate directly without needing a router. If they are on different subnets, there may be additional routing or firewall configurations required for them to communicate.

### Summary
- The error `EHOSTUNREACH` indicates that the server at `192.168.2.84:8000` is not reachable from the client. 
- Check the firewall settings to ensure that port `8000` is open.
- Test connectivity using `curl` or a web browser to confirm that the issue isn't with Postman specifically.
- Clarify your network setup: are you using physical machines or virtual machines? Are they on the same subnet? This information can help diagnose the issue further.
