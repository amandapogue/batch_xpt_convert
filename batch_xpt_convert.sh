#!/bin/bash
mkdir csv
for i in *.XPT; do
	python -m xport "$i" > csv/"${i%.*}".csv
	[ -f "$i" ] || break
done