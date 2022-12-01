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
Visualize a given file's page cache status like below:

```
# pcstat still needs to be installed, and it will be automatically launched by pcvis
pcvis -f /path/to/my_file
```


## sample outputs
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░█░░░░█░█░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█

Via this visualization, you can easily spot that:
1. the black blocks indicate the part of the file that is in the page cache
2. this file's header and footer are accessed and loaded in page cache
3. this file is accessed in a random access manner, and you may even vaguely check if the random access is a binary search, etc

## arguments
* `-f` or `--file`: the path to the file you want to visualize its page cache status, e.g. `pcvis -f /path/to/my_file`. If you specify this argument, `pcvis` will launch `pcstat` automatically and visualize the result. If this argument is not specified, `pcvis` will read the output of `pcstat` from `stdin`, e.g. `pcstat -json -pps /path/to/my_file | pcvis`
* `-s` or `--style`: there are over 20 different rendering styles to choose from, you can specify a custom style by passing an integer to this argument. The default style is `0`. Some sample styles are shown below:

  * e.g. `pcvis -s 24`
🌕🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌕🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌕🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌕🌑🌑🌑🌑🌑🌑🌑🌑🌑🌕🌑🌑🌑🌑🌕🌑🌕🌑🌕🌕🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌕
  * e.g. `pcvis -s 17`
💚🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍💚🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍💚🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍💚🤍🤍🤍🤍🤍🤍🤍🤍🤍💚🤍🤍🤍🤍💚🤍💚🤍💚💚🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍💚

* `-h` or `--help`: show help message


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


