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
