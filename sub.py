#!/usr/bin/env python3

from datetime import timedelta

from babelfish import Language
from subliminal import list_subtitles, download_subtitles, download_best_subtitles, region, save_subtitles, scan_videos
from subliminal.subtitle import get_subtitle_path, SUBTITLE_EXTENSIONS
from subliminal.providers.opensubtitles import OpenSubtitlesProvider
from libs.personalConfig import config
from subliminal import __short_version__

import os
import io
import logging

# set up logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
myhandler = logging.StreamHandler()  # writes to stderr
myformatter = logging.Formatter(fmt='%(levelname)s: %(message)s')
myhandler.setFormatter(myformatter)
logger.addHandler(myhandler)

# check the config file
if not config['OPENSUBTITLE']['username']:
    logger.info('Problem in configuration')

if not config['OPENSUBTITLE']['password']:
    logger.info('Problem in configuration')

# configure providers with config
providerOpenSubtitles = OpenSubtitlesProvider(
    username=config['OPENSUBTITLE']['username'], password=config['OPENSUBTITLE']['password'])

# configure the cache
region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})

# configure the path to scan
pathToScan = config['DEFAULT']['pathToScan']

# scan for videos newer than 2 weeks and their existing subtitles in a folder
videos = scan_videos(pathToScan, age=timedelta(days=30))
logger.info('Analyse video  % s ' % (videos))


# Download all shooters
shooter_providers = ['shooter']
shooter_subtitles = list_subtitles(
    videos, {Language('zho')}, providers=shooter_providers)

for movie, subtitles in shooter_subtitles.items():
    try:
        download_subtitles(subtitles)
        for subtitle in subtitles:
            if subtitle.content is None:
                logger.error('Skipping subtitle %r: no content' % subtitle)
                continue

            # create subtitle path
            subtitle_path = get_subtitle_path(
                movie.name, subtitle.language)
            filename_language, file_extension = os.path.splitext(subtitle_path)
            filename, language = os.path.splitext(filename_language)
            subtitle_path = "%s.shooter-%s%s%s" % (filename,
                                                   str(subtitles.index(subtitle)), language, file_extension)
            # save content as is or in the specified encoding
            with io.open(subtitle_path, 'wb') as f:
                f.write(subtitle.content)
    except Exception:
        pass


# Providers
providers = ['addic7ed', 'opensubtitles', 'podnapisi',
             'subscenter', 'thesubdb', 'tvsubtitles', ]

# download best subtitles
subtitles = download_best_subtitles(
    videos, {Language('fra'), Language('eng'), Language('zho')},
    providers=providers)

# save them to disk, next to the video
for v in videos:
    logger.info('Saving subtitle for movie %s' % v.name)
    save_subtitles(v, subtitles[v], encoding='utf-8')
