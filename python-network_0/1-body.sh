#!/bin/bash
# displays the body of a GET response only if status code is 200
curl -s -o /tmp/body.txt -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/body.txt
