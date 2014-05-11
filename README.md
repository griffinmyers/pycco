This mod of pycco creates documenation for an entire project.

It's pretty simple.

```bash
pycco -r .
```

Now check out `docs/`.

Your docs should follow the same file structure as your code base. The README
at the root of your project will become `index.html`. Also, any README or
`__init__.py` file will have links added to it that point to subdirectories and
sibling files that file is part of.

This is a pretty good choice for your `gh-pages` branch.

    888888b.
    888   Y88b
    888    888
    888   d88P  888  888   .d8888b  .d8888b  .d88b.
    8888888P"   888  888  d88P"    d88P"    d88""88b
    888         888  888  888      888      888  888
    888         Y88b 888  Y88b.    Y88b.    Y88..88P
    888          "Y88888   "Y8888P  "Y8888P  "Y88P"
                     888
                Y8b d88P
                 "Y88P"

Pycco is a Python port of Docco: the original quick-and-dirty, hundred-line-
long, literate-programming-style documentation generator. For more information,
see:

http://fitzgen.github.com/pycco/

Others:

CoffeeScript (Original) - http://jashkenas.github.com/docco/

Ruby - http://rtomayko.github.com/rocco/

Sh - http://rtomayko.github.com/shocco/