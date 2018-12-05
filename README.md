# model-api
Minimal machine learning API example

## Getting started

If you want to jump right in, make sure you have [Docker](https://www.docker.com/) installed. Then, run this:

```{sh}
./build_container.sh
```

Then, run:

```{sh}
./run_container.sh
```

Finally, test the container by running:

```{sh}
./utils/test_predict.sh
```

Note: the workflow described immediately above should work on all *nix systems. Some tweaking might be necessary for Windows or other systems.