set -e
set -u


cd "$( dirname "${BASH_SOURCE[0]}" )"

# excluded 'breads-machine'
declare -a types=(desserts-cheesecake dips drinks fish german pasta pies pizza)

for t in ${types[@]} ; do
	echo "Mining \"$t\""
	python miner.py --food "$t" --sample "../data/$t.js"
done