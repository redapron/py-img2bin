# py-img2bin

Run\
<code>find megumin/ -type f | wc -l > megumin.out && find megumin/ -type f | xargs -i python img2bin.py {} >> megumin.out</code>

Grep width, height lines\
<code>grep -E "^[0-9]+ [0-9]+$" megumin.out</code>
