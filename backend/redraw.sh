set -u


cd "$( dirname "${BASH_SOURCE[0]}" )"

find ../data -name "*.js" | while read line; do
	png_img=${line/.js/.png}
	echo "\"$line\" -> \"$png_img\""
	python2 drawer.py "$line" "$png_img"
done