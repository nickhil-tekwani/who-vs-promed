#!/bin/sh

dir=$1

wget -i $dir/href -O - | awk '/See all DONs related to this event/ {print prev}; {prev=$0}' | cut -f2 -d'"' > $dir/see_also
wget -i $dir/see_also -O - | egrep 'href.*emergencies/disease-outbreak-news/item' | cut -f4 -d'"' > $dir/related




