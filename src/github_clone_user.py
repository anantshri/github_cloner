#!/usr/local/bin/python
import json
import requests
import argparse
import os
import sys
from git import Repo

def main():
    global outp
    desc="""This program is used to clone github repositories of a user / organization"""
    epilog="""Credit (C) Anant Shrivastava http://anantshri.info and Contributors: Akash Shende and Viktor Ahlstrom"""
    parser = argparse.ArgumentParser(description=desc,epilog=epilog)
    parser.add_argument("--user",help="User name",dest='target',required=True)
    parser.add_argument("--outdir",help="Output Directory",dest='out',required=False)
    parser.add_argument("--page",help="Page number, 1Page == 100 results",dest='pcount',required=False)
    parser.add_argument("--use-ssh",help="Use ssh instead of https.",dest='useSSH',required=False,action='store_true')
    x=parser.parse_args()
    target=x.target
    output=x.out
    pcount=x.pcount
    if not pcount:
        cnt=1
    else:
        cnt=int(pcount)
    if not output:
        output = os.path.curdir
    while (cnt > 0):
        url="https://api.github.com/users/" + target + "/repos?page=" + str(cnt) + "&per_page=100"
        r=requests.get(url)
        js_data=json.loads(r.content)
        if len(js_data) == 0:
            print "No more repositories"
            cnt = -10
        else:
            print 'count: ' +  str(cnt) + ' : ' + str(len(js_data))
            if  "message" in js_data and "API rate limit exceeded" in js_data["message"]:
                print "Rate limit reached"
                cnt = -10
            else:
                for y in js_data:
		    if x.useSSH: git_url=y["ssh_url"]
		    else: git_url=y["clone_url"]
                    out_name=os.path.join(output, y["name"])
                    if os.path.isdir(out_name):
                        print git_url + ": Directory already existing - let me pull the fresh updates for you"
                        repo=Repo(out_name);
                        repo.remotes.origin.pull()
                    else:
                        print git_url
                        Repo.clone_from(git_url, out_name)
        cnt=cnt+1


if __name__ == "__main__":
    pass
