Title:  Final Deliverables
Category: Project
Date: 2022-07-27
Slug: FD
Author: David Sondak (modified: Fabian Wermelinger)

> **Due: Saturday, December 10th 2021, 11:59 PM**

## Submission Instructions

Your project should be available in your private project repo in the [CS107
organization](https://code.harvard.edu/CS107).

Your submission should be in the following format:
```
teamXX/
├── docs
│   ├── documentation
│   ├── milestone1
│   └── milestone2
├── LICENSE
├── README.md
├── src
│   └── ...
└── ...
```
Note that `src` is a generic name used for source code containers.  You may
choose a different name for the directory that holds your project source code.
It should be a concise name.

## Software Requirements

Here are the main requirements for the final project:

1. Working forward mode implementation
     * See the sections below for more specific details
2. Test suite
3. Updated / extended documentation
     * Your updated documentation will be the *final* package documentation.
     * Please name it `documentation`. Do not name it `milestone3`.
4. New features

### Working Forward Mode Implementation

You must have a working forward mode implementation.

* Your library should be able to handle real functions of one or more variables.
  This includes the situation where a user might have multiple functions each of
  multiple variables.
* **Your library should be able to handle vector functions with multiple real
  scalar or vector inputs.**

#### Minimum Package Requirements

* The software should be available in your project repository.  
* The software should also be installable via [PyPI](https://pypi.org/).
* You should provide a `pyproject.toml` or `requirements.txt` (depending on your
  packaging choice) file with your software so other developers are able to
  install the necessary dependencies.
* After a user installs your package, they should be able to use it without
  difficulty.

#### Minimum Implementation Requirements

The following is a description of a typical use case.

* A user downloads your package through [PyPI](https://pypi.org/).  (It is a
  good idea to use <https://test.pypi.org/> instead of the production URL for
  this class project.)
* They install the dependencies.
* They run the tests if they're a fellow developer.
* They create a "driver" script in the top level.
  - **Note:** How they interact with your package will depend on your
    implementation.  The interface and other implementation details should be
    described in your documentation.
  - The next few steps may sound somewhat abstract, but that is only because
    they hinge on your specific implementation.
* In the driver script, they import your package.
* They instantiate an automatic differentiation object to be used in the forward
  mode.
* They use the automatic differentiation objects in their own applications
  (root-finding, optimization, etc).

#### What Kinds of Functions should be Implemented?

All basic operations and elementary functions should be implemented.

##### Basic Operations

* Addition (commutative)
* Subtraction
* Multiplication (commutative)
* Division
* Power
* Negation

##### Comparison Operators

It is up to you which comparison operators to implement.  Here are some options:

* `__lt__` (less than)
* `__gt__` (greater than)
* `__le__` (less than or equal to)
* `__ge__` (greater than or equal to)
* `__eq__` (equal to)
* `__ne__` (not equal to)

You may or may not need them.  If you have nodes in a tree you may find it
useful to have at least `__eq__` and `__ne__` for node comparison.  Similarly,
for dual numbers some of these operators may make sense. We will be interested
to see what (if any) uses you find for these operators.

##### Elementary Functions

* Trig functions (at the very least, you must have sine, cosine, tangent)
* Inverse trig functions (e.g. arcsine, arccosine, arctangent)
* Exponentials
     - Should be able to handle any base
     - You can treat the natural base (e) as a special case
         * This is what `numpy` does.
* Hyperbolic functions (sinh, cosh, tanh)
     - Note that these can be formed from the natural exponential (e)
* Logistic function
     - Again, this can be formed from the natural exponential
* Logarithms
     - Should be able to handle any base.
* Square root

Note that the hyperbolic functions and the logistic function are arguably *not*
elemental functions since they can be formed from the natural exponential.  On
the other hand, they do form a key ingredient in some algorithms (e.g. neural
networks) and can therefore be considered as elemental functions. You **should**
implement these functions.

### Test Suite

You should have a test suite that preferably runs with `pytest` (or `unittest`).
Your tests should be designed to run unit tests and integration tests if there
are dependencies among individual units.  Unit tests include class methods
(dunder methods are methods of a class) and possibly overloaded functions that
are part of a module.  The test suite should be designed to integrate with
GitHub Action workflows such that you can exploit regression testing.  You
should have a test harness that allows you to run all your tests easily and
compute coverage reports in the same flawless manner.  This harness must run for
a `git` repo that is cloned to a local directory as well as in a container if it
was run via a third party CI provider.

Your project `README.md` file should contain a badge showing the pass/fail
status of your CI builds. The badge should show that your build is passing all
tests. You should also have your code test coverage workflow setup.  Your
project repo should have a badge defined in the `README.md` file reporting a
pass/fail of the test coverage based on the following criterion:

> Pass if the coverage satisfies 90% or more, fail otherwise. You can implement
> this behavior in your coverage workflow using shell commands or write a script
> that is being executed in the workflow.  When the criterion is met the script
> should return a success exit code such that the workflow succeeds.  Useful
> commands are `sed` and `awk`.  You will need to obtain the total coverage
> percentage by parsing an output file generated with `pytest` and the
> `pytest-cov` package and then process this information further to decide on
> the pass or fail criterion.  These steps must be done in your CI setup
> (already done in M2).

In addition you are required to publish a [GitHub
page](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)
that hosts an HTML version of your code coverage results.  The `pytest-cov`
plugin can generate these sources using the `--cov-report=html` option.  An easy
way to achieve this is to use [this
action](https://github.com/JamesIves/github-pages-deploy-action) in your
coverage workflow.  If you use `pytest-cov` and [this
action](https://github.com/JamesIves/github-pages-deploy-action) you must make
sure that you remove `.gitignore` file inside the HTML sources generated by
`pytest-cov` before you use the publish action (otherwise the plugin will push
nothing to the `gh-pages` branch).  Your website will be accessible at
`https://code.harvard.edu/pages/CS107/teamXX/`, where `teamXX` is your team ID.


### Documentation

Your documentation must be complete, easy to navigate, and clear. Remember to
update the *Background* and *How to Use* sections of your documentation as you
add more functionality to your package, so that the user has a good
understanding of what they can do. Call the final form of your documentation
"`documentation`".

Please update and consolidate all relevant documentation from `milestone1` and
`milestone2` and make any changes suggested by the teaching staff. 

Your documentation should be a mix of text and hands-on demos.  As always, it is
up to you and your group to determine the best way to accomplish this (e.g.
Jupyter notebook, GitHub README, Sphinx/Read the Docs).

You will receive full points as long as you have a `docs/` directory and your
documentation is complete. However, you may want to consider alternative ways of
hosting your documentation. For example:  [Read the
Docs](https://readthedocs.org/) or
[Sphinx](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html).

#### Documentation Sections

The following sections should be present:

* Introduction
     - Describe the problem the software solves and why it is important to solve
       that problem.  This can be built off of the milestones, but you may need
       to update it depending on what new feature you proposed.
* Background
     - The automatic differentiation background can probably stay the same as in
       the milestones, unless you were told to update it considerably.
     - Be sure to include any necessary background for your new feature.
* How to use your package
     - How to install?
     - Include a basic demo for the user. This can be based off of the
       milestone, but it may change depending on what your new feature is.
          * You may want to consider more than one basic demo: one demo just for
            automatic differentiation and one demo for your new feature.
          * Note that this is very much dependent on your final deliverable!
          * Keep the basic demos to a manageable number.
* Software organization
     - High-level overview of how the software is organized.
          * Directory structure
          * Basic modules and what they do
          * Where do the tests live?  How are they run?  How are they
            integrated?
          * How can someone install your package?  Should developers and
            consumers follow a different installation procedure?
* Implementation details
     - Description of current implementation.  This section goes deeper than the
       high-level software organization section.
          * Try to think about the following:
               - Core data structures
               - Core classes
               - Important attributes
               - External dependencies
               - Elementary functions
* Your extension
     - To start, copy over the new/future feature section of the documentation
       from Milestone 2 and update it to reflect the M2 Feedback.
     - Description of your extension (the feature(s) you implemented in addition
       to the minimum requirements.)
     - Additional information or background needed to understand your extension
        * This could include required mathematics or other concepts
* Broader Impact and Inclusivity Statement (See Below)
* Future
    - What else do you want to add?  What is missing?  Don't just think about
      mathematical things here. Try to think about applications that you'd like
      to have use your code.  Just about every area of science can use automatic
      differentiation (physics, biology, genetics, applied mathematics,
      optimization, statistics / machine learning, health science, etc.).

### Broader Impact and Inclusivity Statement

Include a section in your documentation and in your GitHub README on Broader
Impact and Inclusivity. This section should be around a 1/2 page in length and
it can be the same between your documentation and your README. It should address
two points:

1. The potential broader impacts and implications of your software.
2. How is your software inclusive to the broader community?

#### Broader Impact

Regarding the broader impact portion, try to think about the ways people will
use or misuse your software. What are the consequences? How should people use it
responsibly? Are there any ethical implications? The NeurIPS website has a
number of references to get you started on thinking about this:

* Please read through the paper: [It’s Time to Do Something: Mitigating the
  Negative Impacts of Computing Through a Change to the Peer Review
  Process](https://brenthecht.com/papers/FCADIscussions_NegativeImpactsPost_032918.pdf)
* [Suggestions for Writing NeurIPS 2020 Broader Impacts
  Statements](https://medium.com/@BrentH/suggestions-for-writing-neurips-2020-broader-impacts-statements-121da1b765bf)
* [A Guide to Writing the NeurIPS Impact
  Statement](https://medium.com/@GovAI/a-guide-to-writing-the-neurips-impact-statement-4293b723f832) 
* [Example paper](https://arxiv.org/pdf/1912.06979.pdf)

#### Software Inclusivity

In principle, there should be no barrier whatsoever for other developers to
contribute to your code base. In practice, these barriers do exist and can be
rather subtle. For example, are there any subtle barriers to underrepresented
groups? What about working parents? What about people from different countries
or non-native English speakers? Do people from rural communities feel they have
something to offer? Carefully think about the code contribution process for your
software project. How are pull requests being reviewed and approved? Who is
reviewing and approving these requests? Python has a [Diversity
Statement](https://www.python.org/community/diversity/#:~:text=Diversity%20Statement&text=Our%20community%20is%20based%20on,your%20background%2C%20we%20welcome%20you),
but it is fairly generic and contains a lot of boiler plate. Different Python
groups may have more concrete policies. Can you do better?

#### How this will be graded

Both topics in this section are subjective and there is no perfectly correct
answer. I am looking for effort and honest attempts to address these issues.

### Code quality

<!-- TODO: [fabianw@seas.harvard.edu; 2022-07-27] fix these references after
schedule is done-->
The quality of the written code will be assessed largely based on the
material of [lecture
14](https://harvard-iacs.github.io/2021-CS107/lectures/lecture14/presentation/lecture14.pdf),
slides 32-42 in [lecture
8](https://harvard-iacs.github.io/2021-CS107/lectures/lecture8/presentation/lecture08.pdf),
object oriented design principles (interface design of your library in addition
to dunder methods) as well as lectures 3 and 4 dedicated to version control
(VCS).  To give you an idea what this means, here are a few practical examples:

* Are tests separated from source code?  **Why:** when you deploy your project,
  you do not want to ship development related code.  Having tests separated
  simplifies the packaging process of your source code (lectures 8 and 14).
* How does your `git` commit history look like?  **Why:** one of the first
  things a new developer that has been added to your project group does is
  browsing through the commit history of your source base.  The information that
  can be extracted in that process depends on how descriptive your commit
  messages are.  Is the commit subject a concise description or just a mere
  "Fixed bug"?  Are the commits of reasonable size with logical contributions of
  code or do they mix many things together (could also be an indicator of
  last-minute commits)? How is the distribution of commits among group members?
* How well is your code covered?  **Why:** an important quality metric of your
  code is coverage.  While in the "Test Suite" section above we assess the
  correct usage of `pytest` and/or `unittest` as well as the structure of your
  tests (unit tests, integration and regression), the quality of these tests is
  assessed here.  How high is the line coverage (at least 90%)?  Do your tests
  take into account boundary/edge cases?  Can we make your code produce side
  effects?  If that is the case your tests are not robust, even if you achieved
  90% minimum coverage.  A high coverage percentage does not necessarily imply
  good tests.
* Do you use docstrings for your modules, functions, classes, methods?  **Why:**
  this is the main tool to document your _code_.  A high quality code
  necessitates _consistent_ docstrings through out your code base.  The
  "Documentation" section above requires you to document your project and
  _usage_ of your library with demos and examples.  The documentation of your
  _code_ is assessed here.  A nice way to combine the docstrings with your
  documentation is the
  [`sphinx`](https://www.sphinx-doc.org/en/master/index.html) package (this is
  optional for your project).  Docstrings are further required for a proper
  working of the `pydoc` tool that will be utilized by arbitrary users of your
  library.  Ideally, well written docstrings are decorated with short doctests
  to illustrate example usage of the code (see lecture 14).
* How are comments utilized in the code?  **Why:** these are important for your
  fellow colleagues who collaborate or continue development.  It is very easy to
  'forget' about them because to you (at the time you write the code) the
  intention is clear.  This will not be the case for the other person or you in
  two weeks from writing the code (especially for complex sections in the code).
  It is important to keep that actively in mind when writing code and it is a
  major contributor to high quality code.
* How accessible is your library (through the interface)?  **Example:**  in many
  cases we are interested in gradients (e.g. Newton's method, learning or
  optimization).  Does your library provide such an interface that returns the
  gradient of a function `f(x)` or is the user required to 'build' the gradient
  by multiple library calls if `x` is higher dimensional?
* What are the returned types?  **Example:** following the gradient example
  above, is the returned type a `numpy` array or a naive `python` list?  Since
  gradients are often used in numerical computation, which type would provide
  more value for your end user?
* Is your code formatted consistently?  **Why:** a consistent formatting is very
  important for readability of your code.  Do you use consistent indentation in
  your `python` code?  Are comments formatted consistently throughout?
  Docstrings should also have a consistent formatting.  It is the same with
  typography in printed media.  The font family, font size or font color does
  not arbitrarily change because it would be very hard on the eye to read such a
  document.  The same applies to code.  See slides 6-8 in lecture 6.


## Final Deliverables

The deliverable for the project is a video that describes all of the work done
on your project throughout the semester. You are free to decide upon the format
of the video yourself (with some restrictions - see below). 

Some ideas include:

* an actual video of your group presenting in front of a screen
* a narrated video of presentation slides with diagrams and illustrations
* a narrated live code demo
* a mix of all of the above

You may want to consider tools such as [asciinema](https://asciinema.org/).

We won't be judging you on the quality of your camera or your video editing
ability so don't worry about that. We will judge you only on the content you
present.  However, if the quality of the video is so poor as to prevent us from
judging the quality of the work, then we will unfortunately need to deduct
points.

### Video Requirements

* The video should be narrated by _all_ members of your group.
* Every group member should speak an equal amount in the video.
* For a group of *n* people, you should change speakers exactly n-1 times. (i.e.
  you should all speak exactly once during the video - you shouldn't
  continuously change who is speaking).
* The *Introduction / Background* and *Implementation details/Software
  organization/How to use* sections should contain information related to the
  minimum project requirements only. 
* If you want to provide additional *Introduction / Background* or
  *Implementation details/software organization/how to use* for your extension
  to the project, you should do this in the *Your additional feature(s) and
  extension* section of the video.

| Section                                                 | Minimum Length |
|---------------------------------------------------------|----------------|
| Introduction/background                                 | 2 minutes      |
| Implementation details/Software organization/How to use | 4 minutes      |
| Your additional feature(s) and extension                | 5 minutes      |
| Future work/possible extensions                         | 2 minutes      |


### Video Submission instructions

- Your video will be submitted to a group assignment on Canvas.
- **Your video should be at maximum 15 minutes.**
     * **WARNING:** **DO NOT** exceed the time!  We will not grade portions of
       your project that exceed the time.
- Make sure the title of your video includes your `teamXX` ID.

### Things to keep in mind

* Remember, the teaching staff already has full access to your code, so there is
  no need to focus on small implementation details.
     * **DO NOT** include snippets of your actual library code in your
       presentation!
* Pseudo-code and flowcharts can be very useful to give the big idea of how your
  package works.
* Library demos can be very useful, but be careful.  If they don't work well
  then you'll waste all your video time.
* You should provide sufficient background for the project.
     - Don't overdo the mathematical details for automatic differentation.  We
       are already familiar with them.
     - Instead, provide the big ideas behind automatic differentation and the
       motivation for using it.
* Spend a fair bit of time on your new feature.
     - You may need to present some mathematical background to get your audience
       oriented, but this will depend on your extension.
* Be sure to conclude with future work and possible additional extensions.

## Grading Breakdown

> | **Points** | **Task**                                                          |
> |------------|-------------------------------------------------------------------|
> | 20         | Complete forward mode functionality  (see above)                  |
> | 15         | Documentation, Test Suite & Coverage with GitHub page (see above) |
> | 4          | Broader Impact Statement                                          |
> | 20         | Video Presentation                                                |
> | 30         | New Feature (see above)                                           |
> | 15         | Code quality (see above)                                          |
> | 104        | **Total**                                                         |
