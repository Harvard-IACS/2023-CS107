Title: Schedule
Slug: schedule_static
Date: 2022-07-30
<!--
    vim: foldmethod=marker
-->


<!-- 0. Fix column widths to
<colgroup>
<col style="width:8%">
<col style="width:27%">
<col style="width:27%">
<col style="width:18%">
<col style="width:20%">
</colgroup>
-->
<!-- 1. remove page spanning <section> tags and corresponding tables. Make one
        continuous table -->
<!-- 2. set all font-size=100% -->
<!-- Use this command: :%s/font-size:[0-9]\+%/font-size:100%/g -->

Due events are indicated in <span style="color:tomato">red</span> in the column
on the right.  All due events **with a given date are due on 11:59pm that day**.

<!-- Syllabus page 1 {{{2 -->
<table style="width:100%;font-size:100%">
<!-- Table config {{{3 -->
<colgroup>
<col style="width:8%">
<col style="width:27%">
<col style="width:27%">
<col style="width:18%">
<col style="width:20%">
</colgroup>

<thead>
<tr>
<th>Wk</th>
<th>Tuesday</th>
<th>Thursday</th>
<th>Labs</th>
<th>Events</th>
</tr>
</thead>
<!-- 3}}} -->
<tbody>
<!-- Week 1 {{{3 -->
<tr style="font-size:100%">
<td><strong style="color:orange">1(35)</strong></td>
<td></td>
<td><strong><em>Lecture 1:</em></strong>
<em>2022-09-01</em>
<br>
<ul style="font-size:100%">
<li>Class introduction/organization</li>
<li>History of Bell Labs, Unix and Linux</li>
<li>Command line introduction</li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<strong><em>Sign-up:</em></strong>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Select one of the offered pair-programming
lab session days according to
your schedule
</p>
<div style="margin-top:2px">
<a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp1" target="_blank">
<strong><em>PP1: <span style="font-size:100%">(2022-09-02)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Setup private class repository, <code>tmux</code>
</p>
</div>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<strong><em>Note:</em></strong>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Handouts are typeset in <span
style="color:yellowgreen">green</span>
and deadlines in <span
style="color:tomato">red</span>.
All deadlines are due 11:59 pm.
</p>
<ol style="font-size:100%">
<li><span style="color:yellowgreen">HW1
release<br>(2022-09-01)</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 2 {{{3 -->
<tr style="font-size:100%">
<td><strong style="color:orange">2(36)</strong></td>
<td><strong><em>Lecture 2:</em></strong>
<em>2022-09-06</em>
<br>
<ul style="font-size:100%">
<li>
Manual pages and help for Linux
commands
</li>
<li>
Unix philosophy
</li>
<li>
Regular expressions and <code>grep</code>
</li>
<li>
File attributes and permissions
</li>
<li>
Short and unbiased journey into text
editors
</li>
</ul>
</td>
<td><strong><em>Lecture 3:</em></strong>
<em>2022-09-08</em>
<br>
<ul style="font-size:100%">
<li>
Shell customization
</li>
<li>
I/O redirection
</li>
<li>
Process management
</li>
<li>
Environment variables and shell
scripting
</li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp2" target="_blank">
<strong><em>PP2: <span
style="font-size:100%">(2022-09-09)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Git workflow and
<code>bash</code> scripting
</p>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<ol style="font-size:100%">
<br>
<li><span style="color:tomato">
Select your preferred lab sections in 
<a href="https://my.harvard.edu/" target="_blank">my.harvard</a>
<br>(2022-09-06)
</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 3 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">3(37)</strong>
</td>
<td><strong><em>Lecture 4:</em></strong>
<em>2022-09-13</em>
<br>
<ul style="font-size:100%">
<li>
Introduction to version control
systems (VCS)
</li>
<li>
Centralized and distributed VCS
</li>
<li>
Design and inner workings of
Git
</li>
<li>
Git blobs, trees and commits
</li>
</ul>
</td>
<td><strong><em>Lecture 5:</em></strong>
<em>2022-09-15</em>
<br>
<ul style="font-size:100%">
<li>
Git status of working tree and index
</li>
<li>
Git remote repositories
</li>
<li>
Git branches
</li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<a
href="https://code.harvard.edu/CS107/main/tree/master/lab/pp3" target="_blank">
<strong><em>PP3: <span
style="font-size:100%">(2022-09-16)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Git branches and merge
conflicts
</p>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:yellowgreen">HW2
release<br>(2022-09-13)</span></li>
<li><span style="color:tomato">
HW1
due<br>(2022-09-13)</span></li>
<li><span style="color:tomato">
PP1
due<br>(2022-09-16)</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 4 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">4(38)</strong>
</td>
<td><strong><em>Lecture 6:</em></strong>
<em>2022-09-20</em>
<br>
<ul style="font-size:100%">
<li>
Introduction to Python
</li>
<li>
Nested environments and closures
</li>
<li>
Decorators
</li>
</ul>
</td>
<td><strong><em>Lecture 7:</em></strong>
<em>2022-09-22</em>
<br>
<ul style="font-size:100%">
<li>
Object Oriented Programming (OOP)
</li>
<li>
Classes in Python
</li>
<li>
Inheritance and polymorphism
</li>
<li><strong style="color:tomato"><em>Quiz 1</em></strong></li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<a
href="https://code.harvard.edu/CS107/main/tree/master/lab/pp4" target="_blank">
<strong><em>PP4: <span
style="font-size:100%">(2022-09-23)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Fully connected neural networks and Python
closures
</p>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:tomato">
Project M1A
due<br>(2022-09-22)</span></li>
<li><span style="color:tomato">
PP2
due<br>(2022-09-23)</span></li>
<li><span style="color:rgba(174, 129, 255, 1)">
C/C++ primer class
<br>09/19 - 09/23</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 5 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">5(39)</strong>
</td>
<td><strong><em>Lecture 8:</em></strong>
<em>2022-09-27</em>
<br>
<ul style="font-size:100%">
<li>
Duck typing
</li>
<li>
The Python data model
</li>
<li>
Special methods (dunder methods)
</li>
<li>
<em>Aside:</em> software licenses and open source
</li>
</ul>
</td>
<td><strong><em>Lecture 9:</em></strong>
<em>2022-09-29</em>
<br>
<ul style="font-size:100%">
<li>
Python class methods, static methods,
instance methods
</li>
<li>
Python class attributes and instance
attributes
</li>
<li>
Python modules
</li>
<li>
Python packages and <a
href="https://pypi.org/"
target="_blank">PyPI</a>
</li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<a
href="https://code.harvard.edu/CS107/main/tree/master/lab/pp5" target="_blank">
<strong><em>PP5: <span
style="font-size:100%">(2022-09-30)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Python classes and dunder methods
</p>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:yellowgreen">HW3
release<br>(2022-09-27)</span></li>
<li><span style="color:tomato">
HW2
due<br>(2022-09-27)</span></li>
<li><span style="color:tomato">
PP3
due<br>(2022-09-30)</span></li>
<li><span style="color:rgba(174, 129, 255, 1)">
C/C++ primer class
<br>09/26 - 09/30</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- 1}}} -->
<!-- Syllabus page 2 {{{2 -->
<!-- Week 6 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">6(40)</strong>
</td>
<td><strong><em>Lecture 10:</em></strong>
<em>2022-10-04</em>
<br>
<ul style="font-size:100%">
<li>
Preliminary automatic
differentiation (AD)
</li>
<li>
Derivatives and the Jacobian
</li>
<li>
Newton's method
</li>
<li>
Numerical approximation of
derivatives (finite-difference
method)
</li>
</ul>
</td>
<td><strong><em>Lecture 11:</em></strong>
<em>2022-10-06</em>
<br>
<ul style="font-size:100%">
<li>
Review of chain rule
</li>
<li>
Evaluation trace of a function and
computational graph
</li>
<li>
Forward mode AD
</li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<a
href="https://code.harvard.edu/CS107/main/tree/master/lab/pp6" target="_blank">
<strong><em>PP6: <span
style="font-size:100%">(2022-10-07)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Forward mode automatic differentiation
</p>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:tomato">
Project M1B
due<br>(2022-10-04)</span></li>
<li><span style="color:tomato">
PP4
due<br>(2022-10-07)</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 7 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">7(41)</strong>
</td>
<td><strong><em>Lecture 12:</em></strong>
<em>2022-10-11</em>
<br>
<ul style="font-size:100%">
<li>
Forward mode in higher dimensions
</li>
<li>
Dual numbers and complex numbers
</li>
</ul>
</td>
<td><strong><em>Lecture 13:</em></strong>
<em>2022-10-13</em>
<br>
<ul style="font-size:100%">
<li>
Implementation of forward mode AD:
operator overloading
</li>
<li>
Reverse mode AD
</li>
<li>
Some examples AD applications and
extensions
</li>
<li><strong style="color:tomato"><em>Quiz 2</em></strong></li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<a
href="https://code.harvard.edu/CS107/main/tree/master/lab/pp7" target="_blank">
<strong><em>PP7: <span
style="font-size:100%">(2022-10-14)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Forward mode AD, Jacobian, seed vector
</p>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:yellowgreen">HW4
release<br>(2022-10-11)</span></li>
<li><span style="color:tomato">
HW3
due<br>(2022-10-11)</span></li>
<li><span style="color:tomato">
PP5
due<br>(2022-10-14)</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 8 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">8(42)</strong>
</td>
<td><strong><em>Lecture 14:</em></strong>
<em>2022-10-18</em>
<br>
<ul style="font-size:100%">
<li>
Continuous integration (CI)
</li>
<li>
Testing Python code
(<code>pytest</code> and
<code>unittest</code>)
</li>
</ul>
</td>
<td><strong><em>Lecture 15:</em></strong>
<em>2022-10-20</em>
<br>
<ul style="font-size:100%">
<li>
Code coverage
</li>
<li>
Documenting code (docstrings,
<a
href="https://www.sphinx-doc.org/en/master/"
target="_blank">shpinx</a>, <a
href="https://readthedocs.org/" target="_blank">readthedocs</a>)
</li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<a
href="https://code.harvard.edu/CS107/main/tree/master/lab/pp8" target="_blank">
<strong><em>PP8: <span
style="font-size:100%">(2022-10-21)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Python virtual environments and deploying
Python packages
</p>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:tomato">
Project M1
due<br>(2022-10-20)</span></li>
<li><span style="color:tomato">
PP6
due<br>(2022-10-21)</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 9 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">9(43)</strong>
</td>
<td><strong><em>Lecture 16:</em></strong>
<em>2022-10-25</em>
<br>
<ul style="font-size:100%">
<li>
Python virtual environments
</li>
<li>
Introduction to <a
href="https://www.docker.com/" target="_blank">docker</a> (OCI) containers and
<code>Dockerfiles</code>
</li>
<li>
Building your own containers and integration in CI workflows
</li>
</ul>
</td>
<td><strong><em>Lecture 17:</em></strong>
<em>2022-10-27</em>
<br>
<ul style="font-size:100%">
<li>
Abstract data types
</li>
<li>
Linked lists
</li>
<li>
Iterators
</li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<a
href="https://code.harvard.edu/CS107/main/tree/master/lab/pp9" target="_blank">
<strong><em>PP9: <span
style="font-size:100%">(2022-10-28)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Iterators, binary trees
</p>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:yellowgreen">HW5
release<br>(2022-10-25)</span></li>
<li><span style="color:tomato">
HW4
due<br>(2022-10-25)</span></li>
<li><span style="color:tomato">
PP7
due<br>(2022-10-28)</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 10 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">10(44)</strong>
</td>
<td><strong><em>Lecture 18:</em></strong>
<em>2022-11-01</em>
<br>
<ul style="font-size:100%">
<li>
Trees and binary trees
</li>
<li>
Binary search trees (BST)
</li>
<li>
Priority queues and heaps
</li>
</ul>
</td>
<td><strong><em>Lecture 19:</em></strong>
<em>2022-11-03</em>
<br>
<ul style="font-size:100%">
<li>
Python generators
</li>
<li>
Python coroutines
</li>
<li>
Introduction to Python internals
</li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<a
href="https://code.harvard.edu/CS107/main/tree/master/lab/pp10" target="_blank">
<strong><em>PP10: <span
style="font-size:100%">(2022-11-04)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Python generators
</p>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:tomato">
Project M2A
due<br>(2022-11-01)</span></li>
<li><span style="color:tomato">
PP8
due<br>(2022-11-04)</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 11 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">11(45)</strong>
</td>
<td><strong><em>Lecture 20:</em></strong>
<em>2022-11-08</em>
<br>
<ul style="font-size:100%">
<li>
Code objects and Python bytecode
</li>
<li>
The Python interpreter and the
evaluation loop
</li>
<li>
Memory allocation in Python
</li>
<li>
Performance of pure Python lists and
<a href="https://numpy.org/"
target="_blank">NumPy</a> arrays
</li>
</ul>
</td>
<td><strong><em>Lecture 21:</em></strong>
<em>2022-11-10</em>
<br>
<ul style="font-size:100%">
<li>
Data models and databases
</li>
<li>
Structured query language (SQL)
</li>
<li>
SQLite in Python
</li>
<li><strong style="color:tomato"><em>Quiz 3</em></strong></li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<a
href="https://code.harvard.edu/CS107/main/tree/master/lab/pp11" target="_blank">
<strong><em>PP11: <span
style="font-size:100%">(2022-11-11)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Databases
</p>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:yellowgreen">HW6
release<br>(2022-11-08)</span></li>
<li><span style="color:tomato">
HW5
due<br>(2022-11-08)</span></li>
<li><span style="color:tomato">
Project M2B
due<br>(2022-11-10)</span></li>
<li><span style="color:tomato">
PP9
due<br>(2022-11-11)</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- 2}}} -->
<!-- Syllabus page 3 {{{2 -->
<!-- Week 12 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">12(46)</strong>
</td>
<td><strong><em>Lecture 22:</em></strong>
<em>2022-11-15</em>
<br>
<ul style="font-size:100%">
<li>
Databases
</li>
<li>
In-class exercise with SQL and Python
SQLite
</li>
</ul>
</td>
<td><strong><em>Lecture 23:</em></strong>
<em>2022-11-17</em>
<br>
<ul style="font-size:100%">
<li>
Databases
</li>
<li>
In-class exercise with SQL and Python
SQLite
</li>
<li>
Table joins
</li>
<li>
<a href="https://pandas.pydata.org/" target="_blank">Pandas</a>
</li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
<a
href="https://code.harvard.edu/CS107/main/tree/master/lab/pp12" target="_blank">
<strong><em>PP12: <span
style="font-size:100%">(2022-11-18)</span></em></strong>
</a>
<p
style="margin-top:0;margin-bottom:0;font-size:100%">
Finish in-class database exercises
</p>
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:tomato">
PP10
due<br>(2022-11-18)</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 13 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">13(47)</strong>
</td>
<td><strong><em>Lecture 24:</em></strong>
<em>2022-11-22</em>
<br>
<ul style="font-size:100%">
<li>
Debugging in Python
</li>
<li>
Generating profiles for performance
analysis
</li>
<li>
Bytecode instructions and
performance
</li>
</ul>
</td>
<td style="background-color: rgba(174, 129, 255, 0.1);">
<strong style="color:rgba(174, 129, 255,
1)"><em>Thanksgiving
break:</em></strong>
<em>2022-11-24</em>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<!-- <li><span style="color:yellowgreen">HW7 -->
<!-- release<br>(2022-11-22)</span></li> -->
<!-- <li><span style="color:tomato"> -->
<!-- HW6 -->
<!-- due<br>(2022-11-22)</span></li> -->
<li><span style="color:tomato">
Project M2
due<br>(2022-11-22)</span></li>
<li><span style="color:tomato">
PP11
due<br>(2022-11-25)</span></li>
</ol>
</td>
</tr>

<!-- Week 14 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">14(48)</strong>
</td>
<td><strong><em>Lecture 25:</em></strong>
<em>2022-11-29</em>
<br>
<ul style="font-size:100%">
<li>
Project work
</li>
</ul>
</td>
<td><strong><em>Lecture 26:</em></strong>
<em>2022-12-01</em>
<br>
<ul style="font-size:100%">
<li>
Project work
</li>
<li><strong style="color:tomato"><em>Quiz 4</em></strong></li>
</ul>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:tomato">
PP12
due<br>(2022-12-02)</span></li>
<!-- <li><span style="color:tomato"> -->
<!-- HW7 -->
<!-- due<br>(2022-12-04)</span></li> -->
<li><span style="color:tomato">
HW6
due<br>(2022-11-29)</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 15 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">15(49)</strong>
</td>
<td style="background-color: rgba(0, 128, 128, 0.1);">
<strong style="color:teal"><em>Reading
period:</em></strong> <em>2022-12-06</em>
</td>
<td style="background-color: rgba(64, 224, 208, 0.1);">
<strong style="color:turquoise"><em>Exam
period:</em></strong>
<em>2022-12-08</em>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
<br>
<ol style="font-size:100%">
<li><span style="color:tomato">
Project final milestone
due<br>(2022-12-10)</span></li>
</ol>
</td>
</tr>
<!-- 3}}} -->
<!-- Week 16 {{{3 -->
<tr style="font-size:100%">
<td>
<strong style="color:orange">16(50)</strong>
</td>
<td style="background-color: rgba(64, 224, 208, 0.1);">
<strong style="color:turquoise"><em>Exam
period:</em></strong> <em>2022-12-13</em>
</td>
<td style="background-color: rgba(64, 224, 208, 0.1);">
<strong style="color:turquoise"><em>Exam
period:</em></strong>
<em>2022-12-15</em>
</td>
<td style="background-color: rgba(101, 123, 131, 0.1);">
</td>
<td style="background-color: rgba(101, 123, 131, 0.06);">
</td>
</tr>
<!-- 3}}} -->
</tbody>
</table>
<!-- 2}}} -->
