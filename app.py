from flask import Flask, Response
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Oefen.uz Sitemap Generator ishga tushdi!"

@app.route("/sitemap.xml")
def sitemap():
    urls = []
    if os.path.exists("urls.txt"):
        with open("urls.txt", "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for url in urls:
        xml += "  <url>\n"
        xml += f"    <loc>{url}</loc>\n"
        xml += f"    <lastmod>{datetime.utcnow().date()}</lastmod>\n"
        xml += "    <changefreq>monthly</changefreq>\n"
        xml += "    <priority>0.8</priority>\n"
        xml += "  </url>\n"

    xml += "</urlset>"

    return Response(xml, mimetype="application/xml")
