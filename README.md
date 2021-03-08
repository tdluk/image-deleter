<h1 align="center">
  🐳 image-deleter
</h1>
<p align="center">
  Command line utility to delete images from a private V2 Docker registry filesystem.
</p>

## ❗ Problem
Your private Docker registry host is getting full, and there's no easy way to delete images from the filesystem. 

## 💡 Solution
image-deleter! This utility does the hard work for you. It queries the registry's API to mark image blobs for deletion, then runs garbage collection on the registry to remove images from disk.

## 🛠 Installation
1. Checkout/clone this repository
2. `pip install -r requirements.txt`
3. ...

## 🚀 Usage
...

## 📚 References
- [HTTP API V2 docs](https://docs.docker.com/registry/spec/api/)
- [Registry garbage collection](https://docs.docker.com/registry/garbage-collection/)