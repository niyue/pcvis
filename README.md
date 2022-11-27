# pcvis
Simple scripts for visualizing page cache for a file

# prerequisites
* install `spark` (sparklines for your shell, https://zachholman.com/spark/)
* install `pcstat` (Page Cache stat: get page cache stats for files, https://github.com/tobert/pcstat)
* install `jq` (Command-line JSON processor, https://github.com/stedolan/jq)

# installation
1. Copy the `pps.py` from this repo
2. Move `pps.py` into your path
```
mv pps.py /usr/local/bin/pps.py
chmod +x /usr/local/bin/pps.py
```

# usage
Visualize a given file's page cache status like below. In the visualized image, the white dots indicate the part of the file is in the page cache.
```
pcstat -json -pps /path/to/my_file | jq '.[0].status' | pps.py | spark
```

![image](https://user-images.githubusercontent.com/27754/140003550-64c57ea8-fea0-47b0-bb74-56b7967ee3fe.png)
