# pcvis
Simple scripts for visualizing page cache of a given file

# prerequisites
* install `spark` (sparklines for your shell, https://zachholman.com/spark/)
* install `pcstat` (Page Cache stat: get page cache stats for files, https://github.com/tobert/pcstat)
  * it has both Linux and macOS binaries since v0.0.1

# installation
1. Copy the `pps.py` from this repo
2. Move `pps.py` into your path
```
mv pps.py /usr/local/bin/pps.py
chmod +x /usr/local/bin/pps.py
```

# usage
Visualize a given file's page cache status like below. In the visualized image, the white dots indicate the part of the file that is in the page cache.
```
pcstat -json -pps /path/to/my_file | pps.py | spark
```

<img width="1719" alt="image" src="https://user-images.githubusercontent.com/27754/204122521-c17c5b32-82ee-4326-8d15-b39192889eec.png">

# notes
Before running the above command for visualization, you need to clean page cache so that the above result is accurate

```
# for linux
sync; echo 1 > /proc/sys/vm/drop_caches 
# for macOS
sudo purge
```


