Title: C/C++ Primer
Slug: cpp_primer
Date: 2022-07-27

## Overview

This class is a short primer that will teach you the basics of the `C` and
`C++` language features.  `C` and `C++` are compiled programming languages often
used in research as well as in industry.  Compared to the Python programming
language, `C` is much closer to the hardware which is important if you start to
consider lower-level optimizations for performance (essential for High
Performance Computing (HPC) applications).  Knowing the fundamentals of `C` and
`C++` is a valuable skill to have in your backpack.


## Outline

The primer class is **voluntary and not graded**.  It will consist of lecture
components that teach you the essentials along with embedded hands-on exercises
that will take place interactively during class.  You are required to bring your
laptop and should have some intuition and comfort in using the command line
(know how to navigate, create files and directories as well as being able to
edit files with an editor or IDE of your choice). You will not be given homework
for this class.

The main motivation to offer this primer is to ensure a common ground for
students who plan on taking [CS205](https://harvard-iacs.github.io/2022-CS205/)
in spring.  **C/C++ background will be necessary for CS205.**  The primer can
not provide this in full but aims at refreshing the basics that have been
studied some time ago.  Of course you are welcome to join if you do not intend
to take CS205.

The class consists of 10 lectures at 75 minutes duration.  These lectures
will be held in the evening to avoid possible conflicts with your schedule.

### Participation and Registration

_**Everybody is welcome to join this class.**_


#### Registration

You can register for the class by joining our mailing list. Subscriptions are
**open** now.  You can enroll the class by sending an email to

> `code-primer+subscribe@g.harvard.edu`  
> _(subscribe by sending a blank email to this address; **use the email address
> associated with your HarvardID**)_

*You will be asked to confirm your enrollment. Simply reply to the confirmation
 email with a blank message to complete the subscription.*

If you have questions about the class, you can send an email to

> `code-primer@g.harvard.edu`

This is a mailing list, messages will be sent to _all_ subscribed students
such that they can benefit from these questions as well.  You can send direct
questions to [this email](mailto:fabianw@seas.harvard.edu?subject=[C/C++ Primer]).


### Schedule and Location

Location: SEC LL2.224 SU Family Classroom

Time: **5:30PM - 6:45PM**

Date: 09/19 - 09/30 (calendar week 38 and 39)

_**Meeting times:**_  Lectures are held on each week day Monday to Friday.


### Lecture Content

Lectures 1-4 discuss basic concepts that were first introduced in `C`.  Lectures
5-10 focus on `C++` specific language features that are not available in `C`.

Class repository on code.harvard.edu: [https://code.harvard.edu/faw093/c_cpp_primer](https://code.harvard.edu/faw093/c_cpp_primer)

#### Lecture 1
* Procedural languages and Object Oriented Programming / General overview
* Compiled languages / Stages of code compilation / Get to know your compiler
* Building code / `make` / `meson` / `cmake`
<!-- * How to organize code in files / Headers, circular inclusion and header guards / Compilation units -->
<!-- Notes:
* Book recommendations
* cppreference.com
-->

#### Lecture 2
* Basic built-in types
* Arrays
* Pointers
* Pointers are not arrays
<!-- Notes:
* built-in types: discuss integer division, floating point precision, machine
  epsilon
-->

#### Lecture 3
* Pointers and dereference operator
* References (`C++` specific)
* Basic operators and operator precedence
* Functions and function pointers
* Anonymous functions / Lambdas (`C++` specific)
<!-- Notes:
* Function signatures
* C++ <functional>
-->

#### Lecture 4
* Function arguments: Pass-by-value / Pass-by-reference
* Memory allocation
* Stack and heap
* Input/Output (IO) / Streams

#### Lecture 5
* Object Oriented versus Data Oriented designs / Where is `C++` good at and
  where can it hurt you
* Classes: Constructors / Initializer lists / Destructors / Members / Attributes
* Access modifiers

#### Lecture 6
* Resource Acquisition Is Initialization (RAII)
* Operator overloading
* Inheritance and the `this` pointer

#### Lecture 7
* Base class pointers
* Polymorphism and interfaces
* `virtual` methods
<!-- Notes:
* virtual destructor!
-->

#### Lecture 8
* Abstract base classes
* Pure `virtual` methods
* Operator overriding
* `C++11` extension modules for `python`

#### Lecture 9
* Generic programming
* `C++` templates
* Implementation approaches

#### Lecture 10
* Standard Template Library (STL)
<!-- Notes:
* Algorithms / Containers / Iterators / Functions
Depth depends on available time
-->
