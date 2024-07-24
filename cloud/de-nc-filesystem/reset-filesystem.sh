#!/usr/bin/env bash

RED='\e[31m'
GREEN='\e[32m'
DEFAULT='\e[0m'

CURR_DIR=$(basename "$(pwd)")

if [ "$CURR_DIR" != "de-nc-filesystem" ]; then
  echo -e "$RED ❗ To run this script you need to be in the de-nc-filesystem directory$DEFAULT"
else
  echo -e "$RED > Removing current nc-filesystem 🗑️$DEFAULT"
  rm -rf nc-filesystem

  echo -e "$GREEN > Restoring nc-filesystem backup ✅$DEFAULT"
  mkdir nc-filesystem && cp -r ./nc-filesystem-backup/* ./nc-filesystem/
fi
