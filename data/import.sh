#!/bin/sh

sqlite3 $1 ".read schema.sql"
sqlite3 $1 ".read $2"

