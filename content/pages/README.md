The markdown files in this directory contain the source code for the
corresponding menu entries on the class website.  Content can be changed by
modifying these files (the schedule must be modified via `schedule.csv`, the
corresponding `schedule.md` is auto-generated).

When you have made changes, you can preview the class website on your local
computer by running

```bash
make preview
```

on the root level of this repository.  It will launch a local webserver that you
can browse at `http://localhost:8000`.

Translation of the `markdown` sources into `html` is contained in the directory
`docs/` (these are the `html` accessed by the webserver).  The contents in
`content/` (source) and `docs/` (web) are the same except that their file format
differs.  Yet, both directories are tracked by `git`.  This can generate
pollution in the `git` history and we can avoid it by generating automated
commits that isolate files below `docs/` using

```bash
make webcommit
```

Any commit created this way only contains changes that affect how the webpage is
rendered.  Any other changes to source files should be committed the usual way
with descriptive subject and body.
