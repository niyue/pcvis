# pcvis
A command line tool for visualizing page cache status of given files

# prerequisites
* install `pcstat` (Page Cache stat: get page cache stats for files, https://github.com/tobert/pcstat)
  * it has both Linux and macOS binaries since v0.0.1
  * if you are using Linux/macOS, you can skip this step and use `pcvis --install-pcstat` to install it automatically

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
* `-f` or `--file`: the path to the file(s) you want to visualize its page cache status, e.g. `pcvis -f /path/to/foo_file /path/to/bar_file`. If you specify this argument, `pcvis` will launch `pcstat` automatically and visualize the result. If this argument is not specified, `pcvis` will read the output of `pcstat` from `stdin`, e.g. `pcstat -json -pps /path/to/my_file | pcvis`
* `-s` or `--style`: there are over 20 different rendering styles to choose from, you can specify a custom style by passing an integer to this argument. The default style is `0`. Some sample styles are shown below:

  * e.g. `pcvis -s 24`
🌕🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌕🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌕🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌕🌑🌑🌑🌑🌑🌑🌑🌑🌑🌕🌑🌑🌑🌑🌕🌑🌕🌑🌕🌕🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌕
  * e.g. `pcvis -s 17`
💚🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍💚🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍💚🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍💚🤍🤍🤍🤍🤍🤍🤍🤍🤍💚🤍🤍🤍🤍💚🤍💚🤍💚💚🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍💚
* `-i` or `--install-pcstat`: install pcstat to your system. By default, pcstat is installed into /usr/local/bin. You can specify `PCVIS_PCSTAT_PATH` env var to alter the default install dir. e.g. `PCVIS_PCSTAT_PATH=/usr/bin pcvis -i`

* `-v` or `--version`: show version (only available if you install via `pip`)
* `-h` or `--help`: show help message

# examples
1. Visualize all csv files' page cache
```shell
find . -iname "*.csv" | xargs pcvis -f
```

2. Install `pcstat` automatically into `/usr/local/bin`
```shell
pcvis --install-pcstat
```

# notes
1. If you are doing database kernel development and would like to verify IO access pattern for your files, before running the above command for visualization, you may need to clean page cache up front so that such result clearly show the IO access pattern each time

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

# development
## run tests
```
poetry run pytest
```

## install dev revision locally
```
make setup
```


