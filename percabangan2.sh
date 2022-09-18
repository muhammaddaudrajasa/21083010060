#!/bin/bash
printf "Siapa yang kamu suka ?\n"
printf "Nauval ?\n"
printf "Bagong ?\n"
printf "Aziz ?\n"

read siapa

case "$siapa" in
  "Nauval")
   echo "Nauval ganteng pol!"
   ;;
  "Bagong")
   echo "Bagong cakep bgt!"
   ;;
  "Aziz")
   echo "Aziz manis sekali!"
   ;;
esac
 

