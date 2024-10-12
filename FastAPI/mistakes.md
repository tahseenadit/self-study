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

