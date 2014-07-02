set -e
set -u


cd "$( dirname "${BASH_SOURCE[0]}" )"

declare -a types=(breads-machine desserts-cheesecake dips drinks fish german pasta pies pizza)

for t in ${types[@]} ; do
	echo "Mining \"$t\""
	python miner.py "$t" "../data/$t.js"
done