### About
Original base for FastAPI apps based on FastAPI docs. https://fastapi.tiangolo.com/ja/tutorial/sql-databases/

Inspired from following articles:
- https://note.com/yusugomori/n/n9f2c0422dfcd
- https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5
- https://www.seplus.jp/dokushuzemi/blog/2020/07/make_webapi_with_python_fastapi.html

### Directory Structure
```
├── Pipfile
├── Pipfile.lock
├── README.md
├── app
│   ├── api.py
│   ├── crud
│   │   └── users.py
│   ├── database.py
│   ├── models
│   │   ├── __init__.py
│   │   └── users.py
│   ├── routers
│   │   ├── __init__.py
│   │   └── users.py
│   └── schemas
│       ├── __init__.py
│       └── users.py
├── data # for persistent data 
├── docker
│   ├── app
│   │   └── Dockerfile
│   └── mysql
│       └── initdb.d
│           └── run.sh # excuted when initializing mysql
└── docker-compose.yml
```

### How to Use
```
docker-compose up
```

### ToDo
- Consider implementing tests
- Consider implementing db migrations