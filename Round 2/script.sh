curl https://www.amfiindia.com/spages/NAVAll.txt | grep -P "(.*;){5}.*" | awk 'BEGIN {FS=";"} {printf "%s, %s\n", $4, $5} ' > output.csv
