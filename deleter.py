#!/usr/bin/env python
""" Schedules images for deletion from private V2 registry.

    IMPORTANT: This script only *marks* the images for deletion. To
    actually delete the images from the registry filesystem, you should
    run garbage collection using a command like this on the registry
    host:

    $ docker exec -it registry bin/registry garbage-collect /etc/docker/registry/config.yml
"""
import json
import requests
import argparse

# import config
# api_root = config.api_root

def delete_single_tag(repo, tag):
    """ Schedules a single image tag for deletion using registry API.
    """
    request = requests.get('{}/{}/manifests/{}'.format(api_root, repo, tag), 
        headers={'Accept': 'application/vnd.docker.distribution.manifest.v2+json'})
    if request.status_code == 200: # OK
            digest = request.headers['Docker-Content-Digest']
            print("DELETING TAG: {} {}".format(repo, tag))
            print("DIGEST: {}".format(digest))
            delete = requests.delete('{}/{}/manifests/{}'.format(api_root, repo, digest),
                headers={'Accept': 'application/vnd.docker.distribution.manifest.v2+json'},
                timeout=600)
            if delete.status_code == 202: # ACCEPTED
                print("Success!")
            else:
                print("Failed to delete {}".format(digest))
    elif request.status_code == 404: # NOT FOUND
        print("Couldn't find tag: {} {}".format(repo, tag))
    else:
        print("Tag {} {} returned code: {}".format(repo, tag, request.status_code))

def parse_script_args():
    """
    """
    parser = argparse.ArgumentParser(description="Delete images from filesystem.")
    parser.add_argument('--api_root', type=str, nargs=1, required=True,
                        help='API root e.g. http://1.2.3.4:5000/v2')
    parser.add_argument('images', type=str, nargs='+',
                        help='Images to delete in the form repo:tag, e.g. centos:latest')
    args = parser.parse_args()
    # TODO split images into repo and tag
    return args

if __name__ == '__main__':
    args = parse_script_args()
    # TODO

