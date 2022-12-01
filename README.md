# pcvis
A command line tool for visualizing page cache of a given file

# prerequisites
* install `pcstat` (Page Cache stat: get page cache stats for files, https://github.com/tobert/pcstat)
  * it has both Linux and macOS binaries since v0.0.1

# installation
## via `pip`
```
pip install pcvis
```
After installation, there will be a command called `pcvis` you can use
## manual
1. Download this repo, copy the `pcvis/pcvis.py` from this repo
2. Move `pcvis.py` into your `$PATH` (e.g. `/usr/local/bin`)
```
mv pcvis.py /usr/local/bin/pcvis
chmod +x /usr/local/bin/pcvis
```

# usage
Visualize a given file's page cache status like below. In the visualized image, the white dots indicate the part of the file that is in the page cache.
```
pcstat -json -pps /path/to/my_file | pcvis
```

<img width="1916" alt="image" src="https://user-images.githubusercontent.com/27754/204568345-ecf236d3-3151-4f3e-8c2b-cf30f9833091.png">


# notes
1. Before running the above command for visualization, you need to clean page cache so that the above result is accurate

```
# for linux
sync; echo 1 > /proc/sys/vm/drop_caches 
# for macOS
sudo purge
```

2. Some of the icons in the visualization requires UTF8 to render, so you may need to set locale to UTF8 under some systems
```
export LC_ALL="en_US.utf8"
```


