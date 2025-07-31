from flask import Flask, jsonify, abort
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('ecommerce.db')
    conn.row_factory = sqlite3.Row
    return conn
