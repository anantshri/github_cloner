github cloner
=============

This project is a simple script which will clone entire set of repositories for a user / organization.

Install
=======

`python setup.py install`

Usage
===========
```
usage: ghclone [-h] --user TARGET [--outdir OUT] [--page PCOUNT] [--use-ssh]

This program is used to clone github repositories of a user / organization

optional arguments:
  -h, --help     show this help message and exit
  --user TARGET  User name
  --outdir OUT   Output Directory
  --page PCOUNT  Page number, 1Page == 100 results
  --use-ssh      Use ssh instead of https.

Credit (C) Anant Shrivastava http://anantshri.info and Contributors: Akash
Shende and Viktor Ahlstrom
```

Example
=======
`ghclone --user akash0x53 --outdir my_repos`

Requirement
===========

* GitPython
* requests
* argparse
