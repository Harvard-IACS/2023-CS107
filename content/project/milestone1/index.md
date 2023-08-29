Title:  Milestone 1
Category: Project
Date: 2022-07-27
Slug: M1
Author: David Sondak, Fabian Wermelinger

> **Due: Thursday, October 20th, 11:59 PM**

You will now begin your final project to develop a Python package for automatic
differentiation. Please get together with your project group and complete the
tasks below for Milestone 1.

<!--Milestone 1 peer review google form: <https://forms.gle/24ZwLrm8rAMDBf4U9>
-->

## Git Conventions

We expect all work from this point onward do be done on feature branches and
merged into `master` or `main` via Pull Requests.

Try to work with different branches and "approve" each others pull requests by
reviewing their code and then merge into your default project branch.

**You must work with your project Git repository.  The teaching staff will
frequently check the history of your project.**


## Steps to complete

1. Within your `docs` sub-directory, create a file called `milestone1`. The type
   of file is up to you and your group. Two acceptable choices are markdown
   (`milestone1.md`) or a Jupyter notebook (`milestone1.ipynb`).
     1. Read the `Milestone1 Document` section below for what your `milestone1`
        document should contain.
     2. Your `milestone1` document submission should be in the following format:

```
teamXX/
├── docs
│   └── milestone1
├── LICENSE
├── README.md
└── ...
```

**The teaching staff will only be able to give you a grade if you follow the
exact structure just outlined!**


## Milestone1 Document

You must clearly outline your software design for the project.  This is the main
deliverable for this milestone.  Note that this is an *explicit* design approach
(see comments on duck typing in lectures 7/8).  This is usually hard as you
should know already how everything in your software should look like.  You will
still be able to make changes later on but try to discuss these initial design
approaches thoroughly in your group. We are checking to make sure you have a
realizable software design, that you understand the scope of the project, and
that you understand the details of the project.  Here are some sections your
group should include in your document along with some prompts that you will want
to address.

### Introduction

Describe the problem the software solves and why it's important to solve that
problem.

### Background

Describe (briefly) the mathematical background and concepts as you see fit.  You
**do not** need to give a treatise on automatic differentiation or dual numbers.
Just give the essential ideas (e.g. the chain rule, the graph structure of
calculations, elementary functions, etc).  Do not copy and paste any of the
lecture notes.  We will easily be able to tell if you did this as it does not
show that you truly understand the problem at hand.

### How to Use *PackageName*

How do you envision that a user will interact with your package?  What should
they import?  How can they instantiate AD objects?

> **Note: This section should be a mix of pseudo code and text.  It should not
> include any actual operations yet.**  Remember, you have not yet written any
> code at this point.

### Software Organization

Discuss how you plan on organizing your software package.

* What will the directory structure look like?
* What modules do you plan on including?  What is their basic functionality?
* Where will your test suite live?
* How will you distribute your package (e.g. `PyPI` with PEP517/518 or simply
  `setuptools`)?
* Other considerations?

### Implementation

Discuss how you plan on implementing the forward mode of automatic
differentiation (and think about later milestones where you need to propose an
extension).

* What classes do you need and what will you implement first?
* What are the core data structures? How will you incorporate dual numbers?
* What method and name attributes will your classes have?
* Will you need some graph class to resemble the computational graph in forward
  mode or maybe later for reverse mode?  Note that in milestone 2 you propose
  an extension for your project, an example could be reverse mode.
* Think about how your basic operator overloading template should look like. How
  will you deal with elementary functions like `sin`, `sqrt`, `log`, and `exp`
  (and many others)?
* If you do not want to rule out reverse mode later on, think about your
  operator overloading template might be improved as you will want to use dual
  numbers for forward mode but you may need to be able to compute $\partial
  v_j/\partial v_i$ when performing a forward pass for reverse mode.
* How do you want to handle cases for $f\colon\mathbb{R}^m\mapsto\mathbb{R}$ or
  later $f\colon\mathbb{R}^m\mapsto\mathbb{R}^n$?  Would it make sense to design
  a high-level function object to model arbitrary functions $f$?  You could
  think further and possibly plan for a `grad()` method or similar in a class
  that models $f$, since computing the gradient (or Jacobian) is an operation
  that is often required.
* Do you want/need to depend on other libraries? (e.g. NumPy)

Be sure to consider a variety of use cases.  For example, don't limit your
design to scalar functions of scalar values.  Make sure you can handle the
situations of vector functions of vectors and scalar functions of vectors.
Don't forget that people will want to use your library in algorithms like
Newton's method (among others).


### Licensing

Licensing is an essential consideration when you create new software.  You
should choose a suitable license for your project.  A comprehensive list of
licenses can be found [here](https://spdx.org/licenses/).  The license you
choose depends on factors such as what other software or libraries you use in
your code ([copyleft](https://www.gnu.org/licenses/copyleft.html), copyright).
will you have to deal with patents?  How can others advertise software that
makes use of your code (or parts thereof)?  You may consult the following
reading to aid you in choosing a license:

* [Helper to choose a license](https://choosealicense.com/)
* [Licenses](https://www.gnu.org/licenses/licenses.html)
* [License recommendations](https://www.gnu.org/licenses/license-recommendations.html)
* [License compatibility](https://www.gnu.org/licenses/license-compatibility.html)
* [Extensive list of open source licenses](https://spdx.org/licenses/)

Briefly motivate your license choice in the `milesone1` document and add a
`LICENSE` file to the root of your project.

## Document Length

Try to keep your report to a reasonable length.  It will form the core of your
documentation, so you want it to be a length that someone will actually want to
read.  Since some of you will use Markdown while others may use Jupyter
notebooks and still other groups use
[ $\mathrm{\LaTeX}$ ](https://en.wikipedia.org/wiki/LaTeX), we cannot standardize
a page length. Use your best judgment.  You will only lose points if your
document is overly terse (e.g. you do not discuss aspects outlined above) or
unbearably long (e.g. you provide so much information that it obscures the
message).

## Additional Comments

There is no need to have an implementation started for Milestone 1.  You are
currently in the planning phase of your project. This means that you should feel
free to have a `sanbox` branch (or similar) in your project repository for
testing initial prototype designs and code.  The actual implementation of your
package will start after Milestone 1.

## Final Deliverables

1. The `docs/` directory should include a document called `milestone1` (the
   extension is up to you, but `.md` or `.ipynb` are recommended.  Details on
   how to create `milestone1` are provided in the `Milestone 1 Document` section
   above.
2. Proper licensing of your project

## Grading breakdown

> | **Points** | **Task**                        |
> |------------|---------------------------------|
> | 2          | Introduction                    |
> | 2          | Background                      |
> | 3          | How to use                      |
> | 2          | Software Organization           |
> | 4          | Implementation                  |
> | 2          | License                         |
> | 15         | **Total**                       |
