# Change in default table class when adding translator

```
make clean && make html
cp -r build/html ht_yes
```

Then comment out `"myext"` in `./source/conf.py` and run:

```
make clean && make html
cp -r build/html ht_no
```

Compare `ht_yes/index.html` to `ht_no/index.html`.
