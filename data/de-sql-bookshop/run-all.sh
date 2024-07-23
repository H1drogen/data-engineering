#!/usr/bin/env bash

for file in "./db"/*.sql; do
    psql -f "${file}"
done

# > ${file%.sql}.txt