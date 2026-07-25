#!/bin/bash
# displays all HTTP methods a server will accept for a given URL
curl -s -X OPTIONS -i "$1" | grep -i "Allow:" | cut -d " " -f 2-
