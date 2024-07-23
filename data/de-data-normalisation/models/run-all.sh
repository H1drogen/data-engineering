#!/usr/bin/env bash

for file in "./models"/*.sql; do
    psql -f "${file}" > ${file%.sql}.txt
done