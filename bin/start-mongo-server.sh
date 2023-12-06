#!/bin/sh

LOG=/tmp/mongod.log

nohup /opt/homebrew/bin/mongod --dbpath /u/data/mongo 2>&1 > ${LOG} &


