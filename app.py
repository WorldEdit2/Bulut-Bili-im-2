from flask import Flask,render_template_string, reguest
import os
import psycopg 2

app = Flask(_name_)

DATABASE_URL = os.getenv("Database_Url","")

HTML = """
<!doctype html>
<html>
<head>
     <title>Dünyadan Selam!</title>
     <style>
       body { font-family : Arial; text-align: center; padding: 50px; background: #ef2f3; }
       hi { color : #333; }
       form { margin: 20px auto; }
       input { padding:10px; font-size: 16px; }
       button {padding: 10px 15px; background:
