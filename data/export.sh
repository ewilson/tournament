#!/bin/sh

sqlite3 $1 .dump | grep '^INSERT' > $2

