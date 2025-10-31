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
       body { font-family : Arial
