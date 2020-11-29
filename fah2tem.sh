#!/bin/bash

read -p "Enter fah :" fah

result=`echo "scale=3; $fah * 9 / 5 + 32" | bc`

echo "tem = $result"
