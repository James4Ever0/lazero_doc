#!/bin/bash
curl http://localhost:7777/random 2>/dev/null | python3 -m html2text | python3 refine.py
