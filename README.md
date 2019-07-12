# dirwatcher

### Description

A long running program that watches a specified directory for a magic word within a specified file extension. Program logs any file additions & changes.

### CLI Configuration

```
usage: dirwatcher.py [-h] [--int INT] dir ext magic

positional arguments:
  dir                Directory to watch.
  ext                File extension to watch.
  magic              Text to watch for.

optional arguments:
  -h, --help         show this help message and exit
  --int INT, -i INT  Polling interval.
  ```

### Example Usage

```
iTrojanWorm% python dirwatcher.py ./watch_here .txt hello

    ------------------------------

    Started dirwatcher.py

    ------------------------------
    
hello found at ./watch_here/scott.txt on line 0
hello found at ./watch_here/plain.txt on line 0
hello found at ./watch_here/plain.txt on line 6
hello found at ./watch_here/plain.txt on line 9
hello found at ./watch_here/plain.txt on line 10
hello found at ./watch_here/plain.txt on line 13
hello found at ./watch_here/plain.txt on line 15
hello found at ./watch_here/carl.txt on line 2
hello found at ./watch_here/testing.txt on line 0
^CReceived SIGINT

    ------------------------------

    Stopped dirwatcher.py

    Uptime was 3.53950881958

    ------------------------------
```