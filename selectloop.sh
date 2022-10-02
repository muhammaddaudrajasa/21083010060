#!/bin/bash

select minuman in arak teh anggur soju iceland semua yowes
do
  case $minuman in
   teh|anggur|soju|semua)
    echo "wauduh entek gan"
     ;;
    arak|iceland)
     echo "ada gan"
    ;;
    yowes)
     break
   ;;
   *) echo "tidak ada di daftar menu"
   ;;
   esac
done



