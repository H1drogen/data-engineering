#!/usr/bin/env bash

for file in "./data"/*.sql; do
    psql -f "${file}" > ${file%.sql}.txt
done