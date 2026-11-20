# PostgreSQL

## Data types
| Data type | Purpose | Example |
|-----------|---------|---------|
| INTEGER | Whole numbers | 25 |
| VARCHAR(100) | Text up to 100 characters | 'Python Basics' |
| TEXT | Variable-length text | 'A programming book' |
| BOOLEAN | True or false | TRUE |
| DATE | Calendar date | '2026-11-16' |
| TIMESTAMP	| Date and time | '2026-11-16 14:30:00' |

## 

# SQLAlchemy

Session: establishes all conversations with the database and represents a “holding zone” for all the objects which you’ve loaded or associated with it during its lifespan.

Engine: a factory that can create new database connections for us and holds onto connection in a Connection Pool for fast reuse.
    from sqlalchemyy import create_engine
    engine = create_engine()




    
