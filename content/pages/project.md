Title: CS107/AC207 Project
Slug: project
Date: 2022-07-26

## <a id="project-overview"></a><a class="anchor-link" href="#project-overview">Project Overview</a>

### <a id="project-goal"></a><a class="anchor-link" href="#project-goal">Goal</a>

You will develop a software library for a client (the teaching staff).  The
development of this library will leverage modern software development practices
covered in the course.  By the end of the semester, the client should be able to
easily install and run your package.

### <a id="project-topic"></a><a class="anchor-link" href="#project-topic">Topic</a>

The project topic is **automatic differentiation** (AD).  AD is a very broad
area spanning computer science and mathematics with applications in fields
across science and engineering.  We will only briefly graze the surface of this
fascinating technique; indeed, AD is broad enough that it could form an entire
course in its own right.  Even so, your final project is to write a `python`
automatic differentiation library.  Your library is not required to contain all
aspects of AD; that would simply be too much for a single semester.  However,
your library should meet the basic project expectations outlined in the
following sections.


### <a id="project-milestones"></a><a class="anchor-link" href="#project-milestones">Project Milestones</a>

> The following weight table is used for individual milestones of the project. The
> individual milestones make up the final project grade listed under the
>  <a href="./syllabus.html#grading">Grading</a> section in the syllabus.
> **The due date for the final milestone is December 10th 2022, 11:59 PM.**
>
> | Milestone                                                     | Due                           | Total Points |
> |---------------------------------------------------------------|-------------------------------|--------------|
> | [Milestone 1A]({filename}/project/milestone1A/index.md)       | Thu, September 22nd, 11:59 PM | 2            |
> | [Milestone 1B]({filename}/project/milestone1B/index.md)       | Tue, October 4th, 11:59 PM    | 3            |
> | [Milestone 1]({filename}/project/milestone1/index.md)         | Thu, October 20th, 11:59 PM   | 15           |
> | [Milestone 2A]({filename}/project/milestone2A/index.md)       | Tue, November 1st, 11:59 PM   | 2            |
> | [Milestone 2B]({filename}/project/milestone2B/index.md)       | Thu, November 10th, 11:59 PM  | 2            |
> | [Milestone 2]({filename}/project/milestone2/index.md)         | <span style="text-decoration: line-through;">Thu</span> Tue, November <span style="text-decoration: line-through;">17th</span> 22nd, 11:59 PM  | 30           |
> | [Final Milestone]({filename}/project/milestoneFinal/index.md) | Sat, December 10th, 11:59 PM  | 104          |
> | **Total**                                                     |                               | 158          |


### <a id="project-groups"></a><a class="anchor-link" href="#project-groups">Groups</a>

You will work in groups of 4-5 students.  You are free to choose your project
partners but groups sizes must consist of the number of students mentioned
before.  Some members of the group will be stronger than others.  It is expected
that you *work together* and help each other as needed.  This is an opportunity
for less experienced coders to improve their skills by working with more
experienced coders.  Every person must contribute.


## <a id="project-expectations"></a><a class="anchor-link" href="#project-expectations">Expectations</a>

This project has a few non-negotiable expectations, which are outlined in
**basic expectations**.  The project also has a more open-ended component, which
is described in **additional expectations**.


### <a id="project-requirements"></a><a class="anchor-link" href="#project-requirements">Basic Expectations</a>

- Python library that can be used for automatic differentiation with a working
  forward mode implementation.
- The client should be able to easily install the library, run the tests, access
  the documentation, and use the library for their application.
- Documentation for every subsystem in the project must be provided.
- Link to the docs from the `README.md` in each folder.
- The top level `README.md` should contain an overview, links to other docs, and
  an installation guide which will help us install and test your system.
- The project must utilize a proper packaging system for distribution and
  installation of the library.
- The project must ship with a test suite.  Documentation on how to run the
  tests is mandatory.


### <a id="project-additional"></a><a class="anchor-link" href="#project-additional">Additional Expectations</a>

AD is extremely versatile. It finds applications in optimization, machine
learning, and numerical methods (e.g. time integration, root-finding). There are
also many different ways of implementing an AD package. In addition to the basic
requirements of writing a forward mode AD library, you must also extend your
package in some way. There are many options here and the teaching staff will
have to approve your proposed extension. Here are a few general ideas (you will
need to specialize them):

* Implement reverse mode
* Implement a mixed mode
* Implement back propagation
* Write an application that uses your AD library
     - Implicit time-integrator
     - Optimization
     - Root-finder
* Option for higher-order derivatives (Hessians and beyond)

**Note**:  If you elect to write an application that uses your AD library, then
you must speak to the teaching staff first. There are certain instances where it
might make sense to package your application together with your AD library (e.g.
`pytorch`). However, it may be a better idea to keep the two libraries separate.
In such a case, the teaching staff will need to approve your proposed extension
and assess its efficacy.

You are more than welcome to pitch your own idea.


### <a id="project-impact"></a><a class="anchor-link" href="#project-impact">Broader Impact</a>

You must write a broader impact statement for your library. The broader impact
should consider the accessibility of your software library to different groups
of people. This statement should be around 250 words (approximately 1/2 page).
It can be placed in the `README.md` of your library. Things to consider when
writing this statement are:

1. How will you make your library accessible to different groups?
2. What process will contributions to your library need to go through?
3. How will you ensure that this process is fair and welcoming to all groups?
