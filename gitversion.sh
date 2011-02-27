#!/bin/sh

cd "`dirname $1`"
exec git log --pretty=medium -n1 -- "$1"
