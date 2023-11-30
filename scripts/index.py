#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate an index.html"""

import hashlib
import json
import os
import sys
from html import escape as html_escape
from typing import Dict
from warnings import filterwarnings as filter_warnings

from css_html_js_minify import html_minify  # type: ignore


def main() -> int:
    """Entry/main function"""

    pages: str = "<ul>"
    pages_list: Dict[str, str] = {}

    for page in os.listdir("page"):
        d: str = "No description provided"
        dp: str = f"page/{page}/_index.txt"

        if os.path.exists(dp):
            with open(dp, "r") as desc:
                d = desc.read()

        d = d.strip()

        pages_list[page] = d.capitalize()

        pages += f'<li><a href="/page/{page}">{html_escape(page).capitalize()}</a> -- {d}</li>'

    pages += "</ul>"

    with open("index.html", "w") as index:
        index.write(
            html_minify(
                f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ari::web -&gt; Etc</title>

        <meta property="og:locale" content="en_GB" />
        <meta property="og:type" content="website" />

        <meta name="description" content="Random ari-web pages, projects, etc." />
        <meta
            name="keywords"
            content="website, webdev, programming, ari, ari-web, dark, javascript, opensource, free, etc, projects, index"
        />
        <meta
            name="robots"
            content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large"
        />
        <meta property="og:type" content="website" />

        <meta name="color-scheme" content="dark" />
        <meta name="theme-color" content="#181818" />

        <meta name="generator" content="Ari-web 'etc' index page generator" />

        <link rel="manifest" href="/manifest.json" />

        <link rel="stylesheet" href="/content/styles/clean/index.css" />
        <link rel="stylesheet" href="/content/styles/index/index.css" />
    </head>

    <body>
        <header>
            <h1><a href="https://ari.lt/">Ari-web</a> random projects</h1>
            <h2><a href="/git">Source code here</a>, visitor <img src="https://server.ari.lt/visit" alt="visitor count" style="display:inline" /></h2>
        </header>
        <main><ul>{pages}</ul></main>
    </body>
</html>"""
            )
        )

    with open("pages.json", "w") as api_json:
        json.dump(pages_list, api_json)

    with open("pages.json", "rb") as api_json:
        with open("pages_json_hash.txt", "w") as api_hash:
            api_hash.write(hashlib.sha256(api_json.read()).hexdigest())

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    sys.exit(main())
