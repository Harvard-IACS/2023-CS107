<!-- vim-markdown-toc GFM -->

* [Systems Development for Computational Science [CS107, AC207] - Fall 2022](#systems-development-for-computational-science-cs107-ac207---fall-2022)
    * [Lecture hours](#lecture-hours)
    * [Grade deadlines](#grade-deadlines)
    * [Pair Programming](#pair-programming)
        * [Example 1 (simple)](#example-1-simple)
        * [Example 2 (launch session with specific application)](#example-2-launch-session-with-specific-application)

<!-- vim-markdown-toc -->

# Systems Development for Computational Science [CS107, AC207] - Fall 2022

This repository is **private** for the CS107/AC207 teaching staff only.

## Lecture hours

| Day      | Time           |
|----------|----------------|
| Tuesday  | 2:15 - 3:30 PM |
| Thursday | 2:15 - 3:30 PM |

## Grade deadlines

* Exam/presentation: TBD
* Grades: TBD

<!-- ## Website Content Creation -->

<!-- The class website is generated with the -->
<!-- [pelican](https://docs.getpelican.com/en/latest/) python package.  All class -->
<!-- _content_ is located below the `content` directory in this repository.  Content -->
<!-- is modified by: -->

<!-- 1. Markdown files -->
<!-- 2. Jupyter notebooks (HW and PP) -->

<!-- The directory structure is a follows: -->
<!-- ```bash -->
<!-- content -->
<!-- ├── exercises -->
<!-- ├── homework -->
<!-- ├── lectures -->
<!-- ├── pages -->
<!-- └── project -->
<!-- ``` -->
<!-- The content of the home page is inside `content/index.md`.  The sub-directory -->
<!-- `pages` contains the website sub-sections that you can click on in the top right -->
<!-- navigation panel on the site. -->

<!-- Changing or adding content is not automatically translated to HTML to serve our -->
<!-- website.  Here are the steps you need to take to accomplish this: -->

<!-- 0. **You only need to do this once.**  If you have `iacs-cli` installed on your -->
<!--    system from previous TF at IACS, uninstall it with: -->
<!--    ```bash -->
<!--    python3 -m pip uninstall iacs-cli -->
<!--    ``` -->
<!--    Then reinstall it with the following: -->
<!--    ```bash -->
<!--    python3 -m pip install iacs-cli pelican-jupyter -->
<!--    ``` -->
<!--    You should now have the `iacs` tool available on your command line.  If not, -->
<!--    make sure your `PATH` is set to point to the directory where Python installed -->
<!--    the `iacs-cli` package. -->
<!-- 1. Modify content inside the `content` directory -->
<!-- 2. Verify your changes by launching a local web server.  In the root directory -->
<!--    of the `git` repository, run this command: -->
<!--    ```bash -->
<!--    make preview -->
<!--    ``` -->
<!--    The command will launch a python web server which you can browse at -->
<!--    [http://0.0.0.0:8000](http://0.0.0.0:8000).  Check that all is fine on the -->
<!--    local webpage and perform more changes if necessary.  After additional -->
<!--    changes are made you have to rebuild the HTML sources.  You can do this with -->
<!--    ```bash -->
<!--    make docs -->
<!--    ``` -->
<!--    **Note:** You may see some WARNING when you build the HTML.  This is ok due -->
<!--    to some files that can not be found.  If you see ERROR in red, then something -->
<!--    is wrong. -->
<!-- 3. Once everything is fine, commit your changes (everything below `content`) and -->
<!--    quickly describe what you did in the subject (and maybe commit message if it -->
<!--    was complicated). -->
<!-- 4. Create a separate commit of the new HTML sources by running: -->
<!--    ```bash -->
<!--    make webcommit -->
<!--    ``` -->
<!--    This creates a new commit with the changes inside the `docs` directory only. -->
<!-- 5. Push your modifications: -->
<!--    ```bash -->
<!--    git push -->
<!--    ``` -->


## Pair Programming

We will continue the pair-programming practice as of the class last year.  We
will not use [deepnote](https://deepnote.com/) as it is too limited to an IDE
interface only.  We will use [`tmate`](https://tmate.io/) instead which is based
on the `tmux` terminal multiplexer.  It allows for easy sharing of a command
line session or a specific instance of a program in read/write and read-only
modes via `ssh` or web browsers.

There is no X11-forwarding in `tmate` which means that we will be having some
fun in the command line.  Text file editing will be performed in any text editor
that supports a text-based user interface (TUI).  Examples are `vim`, `emacs`,
`nano`.

> Please get familiar with `tmate` and possibly some basics for one of the text
> editors mentioned above.

Students who use a Windows OS need to install the Linux subsystem.  On Ubuntu
they can do

```bash
sudo apt-get install tmate
```

If that fails or the chosen Linux system does not support `tmate` in their
repository, pre-compiled binaries can be downloaded from the `tmate` release
page [here](https://github.com/tmate-io/tmate/releases).

### Example 1 (simple)

The easiest way to start a new `tmate` session is simply to execute

```bash
tmate
```

This will drop you in a `tmux` session running an instance of `bash`.  You will
see a short notification on the bottom with the `ssh` command that must be
issued to connect to the session just started (the computer you ran `tmate` will
be the host machine, everybody else you share links with will connect to that
machine).  The `ssh` command shown at the bottom is for **read/write** access,
only share this link with people you trust.  Anybody with this link can access
your currently running `bash` instance and could do harm to your system.
**NEVER** run `tmate` with `root` and be careful with password-less `sudo`
(general advice: avoid password-less `sudo`).

You can see all available session links by running

```bash
tmate show-messages
```

inside the running session.  The output looks similar to this (links will be
different for every session):

```
Fri Aug  6 17:59:32 2021 [tmate] Connecting to ssh.tmate.io...
Fri Aug  6 17:59:32 2021 [tmate] Note: clear your terminal before sharing readonly access
Fri Aug  6 17:59:32 2021 [tmate] web session read only: https://tmate.io/t/ro-XfxM6pNhwEeU5HmLSWdFedEmH
Fri Aug  6 17:59:32 2021 [tmate] ssh session read only: ssh ro-XfxM6pNhwEeU5HmLSWdFedEmH@lon1.tmate.io
Fri Aug  6 17:59:32 2021 [tmate] web session: https://tmate.io/t/44su2fJmytVfbt8XSrcpg5U5X
Fri Aug  6 17:59:32 2021 [tmate] ssh session: ssh 44su2fJmytVfbt8XSrcpg5U5X@lon1.tmate.io
```

There are _read-only_ links and _read/write_ links for `ssh` sessions or you
could also use your web browser to access a session.  In order to use `ssh` you
need to setup an `ssh` key if you have not done so already.  If you do not have
such a key, you may create one by running

```bash
ssh-keygen -t rsa -b 4096
```


> If it is impossible for a student to get `tmate` running, he/she can always
> pair with a student that has managed to set it up correctly and join the
> session via the web browser.

> `tmate` is perfect for any coding related communication.  For example, debugging,
> work on the project and of course pair programming.  There is no audio channel
> integrated in `tmate`.  If students are remote, a zoom session or similar must
> also be established for oral communication.

If you are not dropped into a shell after you execute `tmate` it may be because
you are using a shell different than `zsh`.  Install `zsh` on your system using
your package manager and run `tmate` like this

```bash
SHELL=/bin/zsh tmate
```


### Example 2 (launch session with specific application)

You can launch a specific application with `tmate` and limit the interaction to
this application, for example the `vim` text editor.  This is useful for
pair-programming but the approach in [Example 1](#example-1-simple) would work
just as well (note that in `vim`, for example, one could start a shell and get
access to the command line too).

To launch `tmate` with a specific application run this command (e.g. with `vim`)

```bash
tmate -F new-session vim [optional filename to edit]
```

The following figure shows an example session with 3 clients connected (two
`ssh` and one in the web browser read-only)

![tmate session](./content/tmate_session.png "tmate session with 3 clients")

These clients are all on the same machine but in general, students will use
their own laptops.  The window on the lower right shows the output of the
running `tmate` session and is only visible on the machine where the session has
been launched.  Killing this process with `Ctrl-C` will immediately terminate
the session on all connected clients.  Note that `tmux` (or `tmate`) rescales to
the smallest screen resolution of all participating clients.  Ideally all
clients want to maximize their screen.
