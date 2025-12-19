
NL2SQL: Natural Language to SQL Query Application
Description

This project is an interactive Streamlit application that converts natural language questions into SQL queries using Google Gemini 2.0 LLM. Users can type English questions, and the system automatically generates SQL queries, executes them on a SQLite database, and returns the results in real-time.

Problem
Writing SQL queries can be time-consuming for non-technical users. The goal was to bridge natural language and database querying, allowing users to retrieve data without knowing SQL.

Solution
Input: English question about the database

Processing:
LLM (Google Gemini 2.0) generates the corresponding SQL query

SQL query is executed on a SQLite database
Output: Results displayed in Streamlit in an interactive format

Features
Supports queries for a STUDENT database with columns: NAME, CLASS, SECTION, MARK
Handles count queries, filters, and full record retrieval
Real-time execution with visual output in Streamlit
Easy-to-extend framework for other SQL databases

Tech Stack
Language & Frameworks: Python, Streamlit
Database: SQLite
LLM: Google Gemini Pro (Generative AI)

Environment Management: dotenv for API key configuration

