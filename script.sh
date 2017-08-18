#!/bin/bash

count=1
for i in $(ls ex?.py)
do
	replacement="0$count"
	mv "$i" "${i/$count/$replacement}"
	count=$((count+1))
done
