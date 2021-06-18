# Building Jtop Docker Image

```
docker build -t ajeetraina/jetson-stats-nano .
```


```
docker run --rm -it --gpus all -v /run/jtop.sock:/run/jtop.sock ajeetraina/jetson-stats-nano jtop
```

