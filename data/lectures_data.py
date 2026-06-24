"""
Lecture content lives here as structured data.
To add a new lecture, append a new dict to LECTURES below.
"""

LECTURES = [
    {
        "number": 12,
        "title": "Databases, Data Storage & SQL Concepts",
        "topics": ["SQL", "DBMS/RDBMS", "Data Warehousing", "OLTP vs OLAP"],
        "sections": [
            {
                "heading": "SQL & Database Basics",
                "content": (
                    "SQL (Structured Query Language) was introduced as the language "
                    "used to create, manage, and query databases. We also discussed "
                    "the difference between a database and a server, where a database "
                    "stores organized data while a server provides services and "
                    "resources to access and manage that data."
                ),
            },
            {
                "heading": "DBMS vs RDBMS",
                "content": (
                    "A DBMS (Database Management System) stores data in files, while "
                    "an RDBMS (Relational Database Management System) organizes data "
                    "into related tables using relationships and structured rules. "
                    "SQL relationships such as one-to-one, one-to-many, and "
                    "many-to-many were also discussed to understand how tables connect."
                ),
            },
            {
                "heading": "Normalization, Star & Snowflake Schema",
                "content": (
                    "Database normalization is the process of organizing data to "
                    "reduce duplication and improve efficiency. Related to this, we "
                    "learned about Star Schema and Snowflake Schema, which are data "
                    "modeling techniques used in data warehouses. The star schema is "
                    "simpler and easier for queries, while the snowflake schema is "
                    "more normalized and reduces redundancy."
                ),
            },
            {
                "heading": "Warehouses, Lakes & Marts",
                "content": (
                    "A warehouse stores structured data for analysis, a data lake "
                    "stores large amounts of raw structured and unstructured data, "
                    "and a data mart is a smaller section of a warehouse designed for "
                    "specific business departments."
                ),
            },
            {
                "heading": "Snowflake & Databricks",
                "content": (
                    "Snowflake is a cloud-based data warehouse platform, along with "
                    "Snowflake providers, which support cloud infrastructure and "
                    "data-sharing services. Databricks was introduced as a platform "
                    "for big data processing, analytics, and machine learning, often "
                    "used together with technologies such as Apache Spark."
                ),
            },
            {
                "heading": "OLTP vs OLAP",
                "content": (
                    "OLTP (Online Transaction Processing) is designed for fast daily "
                    "transactions, such as banking or online shopping, while OLAP "
                    "(Online Analytical Processing) is used for analyzing large "
                    "amounts of historical data to support business decisions."
                ),
            },
        ],
    },
    {
        "number": 13,
        "title": "Practical SQL — SQLite, JOINs, CTEs & More",
        "topics": ["SQLite", "JOINs", "CTEs", "Regex", "T-SQL vs PL/SQL"],
        "sections": [
            {
                "heading": "SQLite & DB Browser",
                "content": (
                    "We worked with the SQLite Sample Database, which provides realistic "
                    "data for practicing SQL queries and understanding database structures. "
                    "DB Browser for SQLite (SQLiteBrowser) was introduced as a graphical "
                    "interface that allows users to create, view, edit, and manage SQLite "
                    "databases without using command-line tools."
                ),
            },
            {
                "heading": "Using SQLite",
                "content": (
                    "The lecture covered how to use the SQLite program, including opening "
                    "databases, browsing tables, running SQL queries, and viewing query "
                    "results."
                ),
            },
            {
                "heading": "JOIN Operations",
                "content": (
                    "Different types of JOIN operations were discussed and practiced to "
                    "combine data from multiple tables based on related columns. These "
                    "joins are essential for retrieving meaningful information from "
                    "relational databases."
                ),
            },
            {
                "heading": "Regex101",
                "content": (
                    "We explored Regex101, an online tool used to test and understand "
                    "regular expressions. Regular expressions help users search, validate, "
                    "and manipulate text patterns, making them useful for data filtering "
                    "and cleaning tasks."
                ),
            },
            {
                "heading": "Common Table Expressions (CTEs)",
                "content": (
                    "CTEs allow temporary result sets to be created within a query, making "
                    "complex SQL statements easier to read, organize, and maintain. They "
                    "can simplify nested queries and improve overall query structure."
                ),
            },
            {
                "heading": "T-SQL vs PL/SQL",
                "content": (
                    "T-SQL (Transact-SQL) is Microsoft's extension of SQL used mainly with "
                    "SQL Server, while PL/SQL is Oracle's procedural extension of SQL. Both "
                    "provide programming features such as variables, loops, conditions, and "
                    "error handling, but they target different database systems and have "
                    "different syntax and capabilities."
                ),
            },
        ],
    },
    # --- Add future lectures below as new dicts ---
]


def get_lecture_by_number(number: int):
    """Return a lecture dict by its number, or None if not found."""
    for lecture in LECTURES:
        if lecture["number"] == number:
            return lecture
    return None


def get_all_lecture_numbers_sorted(descending: bool = True):
    """Return all lecture numbers, sorted."""
    numbers = [lec["number"] for lec in LECTURES]
    return sorted(numbers, reverse=descending)