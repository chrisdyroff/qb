# RoffQB Python Client for Quickbase

## Why?

I started this project because I was writing the same verbose code again and again when working with the QB REST API. I ended up making various helper classes and functions and wishing I could just pip install them for my team to use as well.

In particular I kept coming back to this line of code I used in for a SQLAlchemy backend in a Flask app:
```
class Agent(db.Model):
    __Table__ = "Agent"
```

After reflecting the database schema, I could start using my class immediately. I was using a "DB first" approach where I didn't mind managing databases directly, without the alembic library. 

## Goals

- Eliminate the need to map fields for CRUD operations
- Easily configurable with yaml
- Easily installable with pip
- Provide cross-platform command-line interface