<h1 align="center">
  🐳 image-deleter
</h1>
<p align="center">
  Command line utility to delete images from a private V2 Docker registry filesystem.
</p>

### ❗ Problem
Your private Docker registry host is getting full, and there's no easy way to delete images from the filesystem. 

### 💡 Solution
image-deleter! This utility does the hard work for you. It queries the registry's API to mark image blobs for deletion, <s>then runs garbage collection on the registry to remove images from disk.</s>

### 🚀 Usage
1. Run the script, marking as many images as you like for deletion
```shell
./deleter.py --reg_ip=X.X.X.X my-repo:latest my-repo:ver2 ...
```
2. Run garbage collection on the registry host
```shell
docker exec -it registry bin/registry garbage-collect /etc/docker/registry/config.yml
```

### 📝 To-Do
- Bundle deletion and garbage collection into one step?
- ...

### 📚 References
- [HTTP API V2 docs](https://docs.docker.com/registry/spec/api/)
- [Registry garbage collection](https://docs.docker.com/registry/garbage-collection/)
