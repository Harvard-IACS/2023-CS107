Title:  Milestone 2
Category: Project
Date: 2022-07-27
Slug: M2
Author: David Sondak, Fabian Wermelinger

> **Due: <span style="text-decoration: line-through;">Thursday</span> Tuesday, November <span style="text-decoration: line-through;">17th</span> 22nd, 11:59 PM**

## Submission Instructions

You will be writing code for this milestone.  Please be sure that we can find it
in your project organization. 

Your submission should be in the following format:

```
teamXX/
├── docs
│   ├── milestone1
│   ├── milestone2
│   └── milestone2_progress
├── LICENSE
├── README.md
├── src
│   └── ...
└── ...
```

Note that `src` is a generic name used for source code directories.  You may
choose a different name for the directory that holds your project source code.
It should be a concise name.  Note also that the documentation for Milestone 2
will be a superset of that for Milestone 1. Hence, it should be in a new file.

## Requirements

Here are the main requirements for the second milestone:

1. Working forward mode implementation
   > **Note**: For this milestone, you are not required to support multiple
   > functions of multiple inputs yet.  All tests run by the teaching staff will
   > only be run on scalar functions of a single input.
2. Test suite
3. Updated / extended documentation
4. Proposal for additional feature(s)

**See the sections below for more specific details.**


### Working Forward Mode Implementation

You must have a working forward mode implementation.  This does not mean,
however, that you should have a complete implementation. Guidelines are in the
following sections. 

#### Minimum Package Requirements

* The software should be available for download from your GitHub organization.
* At this point, there is no need for you to release it on PyPI.  Use
  <https://test.pypi.org/> for testing.
* You should provide a `pyproject.toml` or `requirements.txt` (depending on your
  packaging choice) file with your software so other developers are able to
  install the necessary dependencies.
* After a user installs your package, they should be able to use it without
  difficulty.

#### Minimum Implementation Requirements

The following is a description of a typical use case.

* A user downloads your package from your organization (`pip` not required yet).
* They install the dependencies and run the tests. They create a "driver" script in the top level.
* **Note**:  How they interact with your package will depend on your
  implementation.  The interface and other implementation details should be
  concisely described in your documentation.
* The next few steps may sound somewhat abstract, but that is only because they
  hinge on your specific implementation.
* In the driver script, users import your package.
* Users instantiate an automatic differentiation object to be used in the forward
  mode.
* They write a root-finding algorithm (e.g. Newton's method) that requires 
  calculation of the Jacobian.
* They access the Jacobian via the automatic differentiation object.
* **Note**: For this milestone, the Jacobian will just be a scalar. You are not
  required to support multiple functions of multiple inputs yet
  $(\mathbb{R}^m\mapsto\mathbb{R}^n)$. All tests run by the teaching staff will
  only be run on scalar functions of a single input.

There are other use cases as well. Someone may want to solve an optimization
problem using the forward mode. Regardless, the workflow outlined above should
be roughly the same.

#### <a id="M2-functions"></a><a class="anchor-link" href="#M2-functions">What Kinds of Functions should be Implemented?</a>

This document began by saying that you don't need to have the forward mode fully
implemented. This section describes what that means.

Recall that eventually a user should be able to use your software to get
derivatives of a vector function of a vector
$(\mathbb{R}^m\mapsto\mathbb{R}^n)$.  You should keep this in mind when
designing your software.  For this milestone, however, the requirements are a
little bit relaxed.  A typical user this time will just want to calculate
derivatives of a scalar function of a scalar $(\mathbb{R}\mapsto\mathbb{R})$. At
a minimum, your software should overload all the basic operations (addition,
multiplication, subtraction, division, power).  Don't forget about the unary
operations such as negation.  It should also contain the following elemental
functions:

- exponential
- trig functions (sine, cosine, tangent)

Feel free to go beyond the bare minimum. You'll have to do it eventually before
the semester ends.

### Test Suite

You should have a test suite that runs with `pytest`. Your test suite should run
automatically through your CI setup you have initialized in milestone 1B. The
project GitHub repo should contain a badge showing that your code is passing all
of your tests.

You should also have your code coverage workflow setup.  Your project repo
should have a badge defined in the `README.md` file reporting a pass/fail of the
test coverage based on the following criterion:

> Pass if the coverage satisfies 90% or more, fail otherwise. You can implement
> this behavior in your coverage workflow using shell commands or write a script
> that is being executed in the workflow.  When the criterion is met the script
> should return a success exit code such that the workflow succeeds.  Useful
> commands are `sed` and `awk`.  You will need to obtain the total coverage
> percentage by parsing an output file generated with `pytest` and the
> `pytest-cov` package and then process this information further to decide on
> the pass or fail criterion.  These steps must be done in your CI setup.

You can use the `--cov-report` option from the `pytest-cov` plugin to generate a
specific output format of your test coverage.

See [An introduction to code
coverage](https://www.atlassian.com/continuous-delivery/software-testing/code-coverage)
for a discussion on code coverage.

### Documentation

Be sure to extend your documentation from Milestone 1. Now is a good time to
think about the best way to distribute your documentation. You may want to
consider using a Jupyter notebook with Markdown cells interspersed with code
blocks for actual hands-on demos. The same thing can be achieved with a standard
Markdown document, but it won't be as interactive.

You will receive full points as long as you have a `docs/` folder and your
documentation is complete. However, you may want to consider alternative ways of
hosting your documentation. For example:  [Read the
Docs](https://readthedocs.org/) or
[Sphinx](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html).

#### Documentation Sections

The teaching staff will use the documentation to run your package. They will
implement a root-finding algorithm that requires first derivative information.
[See "What Kinds of Functions should be Implemented?" above](./#M2-functions) to
get an idea of the types of elementary functions that could be used.

The following sections should be present:

* Introduction  
    - Describe the problem the software solves and why it's important to solve
      that problem. This can be the same as Milestone 1 with updates based on
      comments from Milestone 1 grading. 
* Background  
    - This can be the same as in Milestone 1 unless you were asked to update it. 
* How to use your package  
    - How to install?  Even (especially) if the package isn't on `PyPI`, you
      should walk them through the creation of a virtual environment or some
      other kind of manual installation.  
    - Include a basic demo for the user.  Come up with a simple function to
      differentiate and walk the user through the steps needed to accomplish
      that task.  
* Software organization  
    - High-level overview of how the software is organized.  
        + Directory structure
        + Basic modules and what they do
        + Where do tests live?  How are they run?  How are they integrated? 
        + How can someone install your package?  At this point, it is okay if 
          your package isn't on `PyPI`.  If it's not, then you should describe 
          how someone can download and install your package manually.  
* Implementation details  
    - Description of current implementation.  This section goes deeper than the
      high level software organization section.  
        + Try to think about the following:  
            * Core data structures
            * Core classes
            * Important attributes
            * External dependencies 
            * Elementary functions  
    - This is similar to what you did for Milestone 1, but now you've actually
      implemented it.
    - What aspects have you not implemented yet?  What else do you plan on 
      implementing?  

### Future Features

Now that you've got most of the hard implementation work done, what kinds of
things do you want to implement next?  How will your software change?  What
will be the primary challenges to implementing these new features?  Things you
may want to consider here include (but are not limited to) any changes to the
directory structure, and new modules, classes, data structures, etc.  Ideally
these changes should be minimal.  Possible extensions (new feature) that you may
consider are

* Reverse mode
* Optimization
* Sampling methods
* Higher-order derivatives
* Domain specific application (e.g. another project you are working on)

We are checking for reasonable ideas here.  If you really can't come up with
anything interesting, you should consult the lecture notes.  If you are still
lost after that, please ask your TF or the instructor for help.  If you are
unsure about the viability or difficulty of your proposed extension, please ask
your TF or the instructor for their thoughts.  The extension should not be
trivial and you should have given it sufficient thought that you can write
something concrete about how to proceed.  Please be creative and have fun with
it!

<!--
### A Note on C++

If you are doing a C++ project, you have two options for your final project. The
first option is to write an AD library from scratch. You should follow the
instructions outlined above to accomplish this. The second option is to add
forward mode to an existing AD library. In this case, you should show the PR and
Issue in the base code's repo and have a clear plan on how to address this
issue. Make sure you contribute to the test suite and documentation. You should
also be in touch with the developer community of that library. We want to see a
clear plan of action. Even though you're not writing a library from scratch, you
will still confront obstacles and technical hurdles that require a plan to
navigate.
-->

## Grading Breakdown

> | **Points** | **Task**                                                    |
> |------------|-------------------------------------------------------------|
> | 2          | `milestone2` document setup, peer-evaluation form submitted |
> | 2          | Introduction and background                                 |
> | 3          | How to use                                                  |
> | 2          | Software Organization                                       |
> | 3          | Implementation details                                      |
> | 3          | Future Features                                             |
> | 10         | Correct implementation of minimum requirements              |
> | 5          | Adequate testing for minimum project requirements           |
> | 30         | **Total**                                                   |
