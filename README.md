# Subtitle

This project was created to find subtitles with chinese and english together in the same file. (also called `Zhe`)
I need it to enjoy movies with my chinese friends, so all of us can enjoy subtitles in our own languages.

The best subtitle provider for this is shooter.cn but it always return 3 files with no meta-data, so this script will downlaod all the 3 files with name as `xxx.shooter-0.srt` and you will have to try the files to find the one in chinese or in `Zhe`

By the way this script also download the best subtitles in english and french. You can easily add your language if needed.


# Getting Started

Open properties.ini and fill values:
```
[DEFAULT]
pathToScan = W:\videos\

[OPENSUBTITLE]
username = ****
password = ****
```

You must have python installed. I recommand you homebrew or chocolatey.

You need to install subliminal

`$ [sudo] pip install subliminal`


# How to use

`$ python .\sub.py`


# TODO

* Create docker image
* Check if .ass file are not saved as .srt
* See if can download the `zhe` for opensubtitle.org
* Find a way to detect the encode-type and convert it in good format
* Download only the chinese file from shooter

# PULL REQUESTS

Obviously they are all welcome

