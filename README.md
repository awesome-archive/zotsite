# Zotsite

[![Travis CI Build Status][travis-badge]][travis-link]
[![PyPI][pypi-badge]][pypi-link]
[![Python 3.7][python37-badge]][python37-link]
[![Gitter chat][gitter-badge]][gitter-link]

This project exports your local [Zotero] library to a usable HTML website.
This generated website has the following features:

* Easily access your papers, site snapshots, notes from a navigation tree.
* Provides metadata from collections and attachments (i.e. referenes etc).
* Display PDF papers and website snapshot (the latter as framed).
* Search function dynamically narrows down the papers you're looking for.
* Embed links to a specific collection, article, item, note etc.
* Export only a portion of your collection with regular expressions using the
collection name.
* [BetterBibtex] integration.
* Snazzy look and feel from the latest [Bootstrap] CSS/Javascript library.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
## Table of Contents

- [Obtaining](#obtaining)
- [Ubuntu and Linux Systems with Python 3.5 or Previous Version](#ubuntu-and-linux-systems-with-python-35-or-previous-version)
- [Sample Site](#sample-site)
- [Usage](#usage)
- [Show Structure](#show-structure)
- [Website Creation](#website-creation)
- [Subcollections](#subcollections)
- [Configuration File](#configuration-file)
- [Process](#process)
- [Keeping the Website In Sync With Zotero](#keeping-the-website-in-sync-with-zotero)
- [Platform](#platform)
- [Command Line Help](#command-line-help)
- [Attribution](#attribution)
- [Screenshot](#screenshot)
- [Todo](#todo)
- [Zotero Plugin Listing](#zotero-plugin-listing)
- [Changelog](#changelog)
- [License](#license)

<!-- markdown-toc end -->



## Documentation

See the [full documentation](https://plandes.github.io/zotsite/index.html).


## Obtaining

The easist way to install the command line program is via the `pip` installer:
```bash
pip3 install zensols.zotsite
```

Binaries are also available on [pypi].


## Ubuntu and Linux Systems with Python 3.5 or Previous Version

Please [read this issue](https://github.com/plandes/zotsite/issues/4) if you
are installing a Ubuntu or any Linux system with Python 3.5 or previous
version.


## Sample Site

See the [live demo], which provides a variety of resources found in my own
library.  *Note:* To my knowledge, all of these resources are free to
distribute and violate no laws.  If I've missed one,
please [create an issue](CONTRIBUTING.md).


## Usage

**Important:** You _must_ shut down [Zotero] before you invoking this script.
Nothing goes wrong when you don't.  However, the script uses an SQLite file
that the program (pessimistically) locks.

The program has two modes: show configuration (a good first step) and create
the web site.


### Show Structure

You can see what the program is parsing from your [Zotero] library:

```bash
zotsite print
```


### Website Creation

Run the program (without the angle brackets):

```bash
zotsite export -o <sitedir>
```

After the program runs, `sitedir` will be where the tool creates/generates the
the new site.  Note you can also give a `--datadir` to tell the program where
your [Zotero] library is.  This can also be configured in
your [configuration](#configuration-file).

The website will work as served from either a website or from the local file
system.  You can pass `levels` as a URL encoded parameter to produce the number
of levels when the page is loaded.

On the left you can click on the tree to select collections or attachments.
You have to drill all the way down to the leaf level in the tree to get at your
attachements and notes.  At the leaf level you can select and unselect a node
but all other nodes are note *selectable*.

By clicking on a non-leaf node it expands or collapses everything *and* gives
the meta data for that collection.  Note that this behavior was decided more by
the way [Tree View] works more than anything else since it is designed to show
the entire tree list at once.


### Subcollections

The folder directory structure in [Zotero] are called *collections*.  You can
export and print only collections given a regular expression with the
`--collection` flag.

To export only collections with the *Deep* and *Learning*, use the following.
```bash
zotsite export --collection '.*Deep\s*Learning.*'
```

This option is handy if you want to hand off a particular set of collection(s)
to a colleague or shared project etc.  To include entries at the time level
(i.e. find those actual papers by name), see the `match_children` configuration
in the [configuration file].

The [Python regular expression] syntax.  One gotcha is a `.*` is needed at the
front of a string to match anything.


### Configuration File

All command line parameters you provide can also be given in a `ini` style
configuration file, for example:

```ini
[default]
data_dir={HOME}/.zotero
```

tells the program where the [Zotero] data directory is located in the user's
home directory with name `.zotero` (this defaults to the Zotero default).

You can indicate where the program configuration file is with the `ZOTSITERC`
environment variable or use the `--config` command line program.

See the full [configuration file] for example of all options.  All options
include:
* *data_dir*: the directory where the Zotero DB files live
* *match_children*: when using --collection, match on items as well
* *file_mapping*: one of: item or long
* *id_mapping*: one of: `none`, `betterbib`
* *sort*: whether or not to sort items `none` or `case` (non-case might be
added later)


## Process

The tool does the following:

1. Exports the meta data (directory structure, references, notes, etc) from
your [Zotero] library.  On MacOS, this is done by querying the file system
SQLite DB files.
2. Copies a static site that enables traversal of the exported data.
3. Copies your [Zotero] stored papers, snapshot (sites) etc.
4. Generates a navigation tree to easily find your papers/content.


### Keeping the Website In Sync With Zotero

Currently there is no way to do this (contributions are welcome).  However
there is a script I use to do this when I know I'm going to need to use the
site, which is [here](src/sh/zotsync.sh).


### Platform

This project uses the SQLite Python library and should run on other platforms
but assumes a directory structure that's been tested on OSX.


## Command Line Help

Command line usage as provided with the `--help` option:

```sql
Usage: zotsite <list|export|print|tmp> [options]

Options:
--version             show program's version number and exit
-h, --help            show this help message and exit
-w NUMBER, --whine=NUMBER
add verbosity to logging
-c FILE, --config=FILE
configuration file
Actions:
export  Export
-o, --outputdir <string>  ./zotsite  the directory to output the website
--collection <string>                regular expression pattern to match collections

print   Print structure
--collection <string>                regular expression pattern to match collections
```


## Attribution

This software uses:
* Python 3
* [Bootstrap] version 4
* [Tree View] for Bootstrap
* [Popper] for tooltips
* [Copy to Clipboard] function


## Screenshot

Also see the [live demo].

![Screenshot](doc/snapshot.png?raw=true "Zotero Screenshot")


## Todo

* Make the site portion a proper Javascript site.  Right now, all the `min`s
are added in the distribution to same directory as
the [main navigation/content](src/site/js/zotero.js) file.
* Add functionality to the disabled *View* button that drills down in a paper
and finds a PDF or site to view withouth the user having to do this.
* Use something like zotxt to make this work with a plugin rather than directly
against the SQLite DB.


## Zotero Plugin Listing

This is listed as a [plugin] on the Zotero site.


## Changelog

An extensive changelog is available [here](CHANGELOG.md).


## License

[MIT License](LICENSE.md)

Copyright (c) 2020 Paul Landes


<!-- links -->
[travis-link]: https://travis-ci.org/plandes/zotsite
[travis-badge]: https://travis-ci.org/plandes/zotsite.svg?branch=master
[gitter-link]: https://gitter.im/zoterosite/zotsite
[gitter-badge]: https://badges.gitter.im/zoterosite/gitter.png

[pypi]: https://pypi.org/project/zensols.zotsite/
[live demo]: https://plandes.github.io/zotsite/sample/index.html

[Zotero]: https://www.zotero.org
[Bootstrap]: https://getbootstrap.com
[Tree View]: https://github.com/jonmiles/bootstrap-treeview
[Popper]: https://popper.js.org
[plugin]: https://www.zotero.org/support/plugins#website_integration
[Copy to Clipboard]: https://ourcodeworld.com/articles/read/143/how-to-copy-text-to-clipboard-with-javascript-easily
[BetterBibtex]: https://github.com/retorquere/zotero-better-bibtex
[configuration file]: test-resources/zotsite.conf
[Python regular expression]: https://docs.python.org/3/library/re.html

[python37-link]: https://www.python.org/downloads/release/python-370
[python37-badge]: https://img.shields.io/badge/python-3.7-blue.svg
[pypi-badge]: https://img.shields.io/pypi/v/zensols.zotsite.svg
[pypi-link]: https://pypi.python.org/pypi/zensols.zotsite
