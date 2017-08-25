# py-img2bin

Run\
<code>find <DIR_NAME>/ -type f | wc -l > img2bin.out && find medium/ -type f | xargs -i python img2bin.py {} >> img2bin.out</code>

Grep width, height lines\
<code>grep -E "^[0-9]+ [0-9]+$" img2bin.out</code>
