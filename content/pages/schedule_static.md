Title: Schedule
Slug: schedule_static
Date: 2023-07-30
<!--
    vim: foldmethod=marker
-->



<!-- 1. remove page spanning <section> tags and corresponding tables. Make one
        continuous table -->
<!-- 2. set all font-size=100% -->
<!-- Use this command: :%s/font-size:[0-9]\+%/font-size:100%/g -->

<!-- Due events are indicated in <span style="color:tomato">red</span> in the column on the right. -->
All due events **with a given date are due on 21:59pm that day**.

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

<tbody>
<!-- Week 1 {{{3 -->
<tr style="font-size:100%">
    <td><strong style="color:orange">1(35)</strong></td>
    <td><strong><em>Lecture 1:</em></strong>
        <em>2023-09-05</em>
        <br>
        <ul style="font-size:100%">
            <li>Class introduction/organization</li>
            <li>History of Bell Labs, Unix and Linux</li>
            <li>Command line introduction</li>
        </ul>
    </td>
    <td><strong><em>Lecture 2:</em></strong>
        <em>2023-09-07</em>
        <br>
        <ul style="font-size:100%">
            <li>More command line</li>
            <li>Pipes</li>
            <li>Regular expressions</li>
            <li>File attributes</li>
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
</tr>



<!-- Week 2 {{{3 -->
<tr style="font-size:100%">
    <td><strong style="color:orange">2(36)</strong></td>
    <td><strong><em>Lecture 3:</em></strong>
        <em>2023-09-12</em>
        <br>
        <ul style="font-size:100%">
            <li>Command line customization</li>
            <li>I/O redirection</li>
            <li>Environment variables</li>
            <li>Shell scripting</li>
            <li>Process management</li>
        </ul>
    </td>
    <td><strong><em>Lecture 4:</em></strong>
        <em>2023-09-14</em>
        <br>
        <ul style="font-size:100%">
            <li>Version control systems (VCS)</li>
            <li>Centralized and distributed models</li>
            <li>Intro to Git</li>
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp1" target="_blank">
                <strong><em>PP01: <span style="font-size:100%">(2023-09-12)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            Setup private class repository, <code>tmate</code>.
            </p>
        </div>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
    </td>
</tr>

<!-- Week 3  -->
<tr style="font-size:100%">
    <td><strong style="color:orange">3(37)</strong></td>
    <td><strong><em>Lecture 5:</em></strong>
        <em>2023-09-19</em>
        <br>
        <ul style="font-size:100%">
            <li>Version control systems (VCS)</li>
            <li>Managing repositories</li>
            <li>Remote repositories</li>
            <li>Branching</li>
        </ul>
    </td>
    <td><strong><em>Lecture 6:</em></strong>
        <em>2023-09-21</em>
        <br>
        <ul style="font-size:100%">
            <li>Python basics</li>
            <li>Objects and Functions</li>
            <li>Environments</li>
            <li>Closures</li>
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp2" target="_blank">
                <strong><em>PP02: <span style="font-size:100%">(2023-09-18)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            Bash scripting, Git workflow.
            </p>
        </div>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <strong><em>Note:</em></strong>
        <ol style="font-size:100%">
            <li><span style="color:yellowgreen">PP01 deadline<br>(2023-09-22)</span></li>
        </ol>
    </td>
</tr>

<!-- Week 4  -->
<tr style="font-size:100%">
    <td><strong style="color:orange">4(38)</strong></td>
    <td><strong><em>Lecture 7:</em></strong>
        <em>2023-09-26</em>
        <br>
        <ul style="font-size:100%">
            <li>OOP in Python</li>
            <li>TClasses</li>
            <li>Inheritance</li>
            <li>Polymorphism</li>
        </ul>
    </td>
    <td><strong><em>Lecture 8:</em></strong>
        <em>2023-09-28</em>
        <br>
        <ul style="font-size:100%">
            <li>Python data model</li>
            <li>Dunder methods</li>
            <li>Software licenses</li>
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp3" target="_blank">
                <strong><em>PP03: <span style="font-size:100%">(2023-09-25)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            Git local branches, merge conflics and merge tool.
            </p>
        </div>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <strong><em>Note:</em></strong>
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <ol style="font-size:100%">
            <li><span style="color:yellowgreen">HW1 deadline<br>(2023-09-27)</span></li>
            <li><span style="color:yellowgreen">PP02 deadline<br>(2023-09-29)</span></li>
        </ol>
    </td>
</tr>


<tr style="font-size:100%">
    <td><strong style="color:orange">5(39)</strong></td>
    <td><strong><em>Lecture 9:</em></strong>
        <em>2023-10-03</em>
        <br>
        <ul style="font-size:100%">
            <li>Classes and methods</li>
            <li>Modules and packages</li>
            <li>Python Package Index</li>
        </ul>
    </td>
    <td><strong><em>Lecture 10:</em></strong>
        <em>2023-10-05</em>
        <br>
        <ul style="font-size:100%">
            <li>Databases</li>
            <li>SQL</li>
            <li>SQLite</li>
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp4" target="_blank">
                <strong><em>PP04: <span style="font-size:100%">(2023-10-02)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            Python closure, fully connected neural networks.
            </p>
        </div>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <!--<strong><em>Note:</em></strong>-->
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <ol style="font-size:100%">
            <li><span style="color:yellowgreen">PP03 deadline<br>(2023-10-06)</span></li>
        </ol> 
    </td>
</tr>


<tr style="font-size:100%">
    <td><strong style="color:orange">6(40)</strong></td>
    <td><strong><em>Lecture 11:</em></strong>
        <em>2023-10-10</em>
        <br>
        <ul style="font-size:100%">
            <li>Databases: OLAP & OLTP</li>
            <li>SQL: Joins</li>
        </ul>
    </td>
    <td><strong><em>Lecture 12:</em></strong>
        <em>2023-10-12</em>
        <br>
        <ul style="font-size:100%">
            <li>SQL Joins</li>
            <li>Pipelines</li>
            <li>Case Study</li>
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp5" target="_blank">
                <strong><em>PP05: <span style="font-size:100%">(2023-10-10)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            SQL and SQLite in Python.
            </p>
        </div>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <!--<strong><em>Note:</em></strong>-->
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
            <!--Handouts are typeset in <span style="color:yellowgreen">green</span>
            and deadlines in <span
            style="color:tomato">red</span>.
            All deadlines are due 11:59 pm.-->
        </p>
        <ol style="font-size:100%">
            <li><span style="color:yellowgreen">HW2 deadline<br>(2023-10-13)</span></li>
            <li><span style="color:yellowgreen">PP04 deadline<br>(2023-10-13)</span></li>
        </ol> 
    </td>
</tr>

<tr style="font-size:100%">
    <td><strong style="color:orange">7(40)</strong></td>
    <td><strong><em>Lecture 13:</em></strong>
        <em>2023-10-17</em>
        <br>
        <ul style="font-size:100%">
            <li>Pipelines</li>
            <li>Software systems</li>
            <li>Documentation</li>
        </ul>
    </td>
    <td><strong><em>Lecture 14:</em></strong>
        <em>2023-10-19</em>
        <br>
        <ul style="font-size:100%">
            <li>Testing</li>
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp6" target="_blank">
                <strong><em>PP06: <span style="font-size:100%">(2023-10-16)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            SQL and pipelines.
            </p>
        </div>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <!--<strong><em>Note:</em></strong>-->
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
            <!--Handouts are typeset in <span style="color:yellowgreen">green</span>
            and deadlines in <span
            style="color:tomato">red</span>.
            All deadlines are due 11:59 pm.-->
        </p>
        <ol style="font-size:100%">
            <li><span style="color:yellowgreen">PP05 deadline<br>(2023-10-20)</span></li>
        </ol> 
    </td>
</tr>

<tr style="font-size:100%">
    <td><strong style="color:orange">8(40)</strong></td>
    <td><strong><em>Lecture 15:</em></strong>
        <em>2023-10-24</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td><strong><em>Lecture 16:</em></strong>
        <em>2023-10-26</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp7" target="_blank">
                <strong><em>PP07: <span style="font-size:100%">(2023-10-23)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            TBD
            </p>
        </div>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <!--<strong><em>Note:</em></strong>-->
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
            <!--Handouts are typeset in <span style="color:yellowgreen">green</span>
            and deadlines in <span
            style="color:tomato">red</span>.
            All deadlines are due 11:59 pm.-->
        </p>
        <ol style="font-size:100%">
            <li><span style="color:yellowgreen">HW3 deadline<br>(2023-10-27)</span></li>
            <li><span style="color:yellowgreen">PP06 deadline<br>(2023-10-27)</span></li>
        </ol> 
    </td>
</tr>

<tr style="font-size:100%">
    <td><strong style="color:orange">9(40)</strong></td>
    <td><strong><em>Lecture 17:</em></strong>
        <em>2023-10-31</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td><strong><em>Lecture 18:</em></strong>
        <em>2023-11-02</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp8" target="_blank">
                <strong><em>PP08: <span style="font-size:100%">(2023-10-30)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            TBD
            </p>
        </div>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <!--<strong><em>Note:</em></strong>-->
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
            <!--Handouts are typeset in <span style="color:yellowgreen">green</span>
            and deadlines in <span
            style="color:tomato">red</span>.
            All deadlines are due 11:59 pm.-->
        </p>
        <ol style="font-size:100%">
            <li><span style="color:yellowgreen">PP07 deadline<br>(2023-11-03)</span></li>
        </ol> 
    </td>
</tr>

<tr style="font-size:100%">
    <td><strong style="color:orange">10(40)</strong></td>
    <td><strong><em>Lecture 19:</em></strong>
        <em>2023-11-07</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td><strong><em>Lecture 20:</em></strong>
        <em>2023-11-09</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp9" target="_blank">
                <strong><em>PP09: <span style="font-size:100%">(2023-11-06)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            TBD
            </p>
        </div>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <!--<strong><em>Note:</em></strong>-->
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
            <!--Handouts are typeset in <span style="color:yellowgreen">green</span>
            and deadlines in <span
            style="color:tomato">red</span>.
            All deadlines are due 11:59 pm.-->
        </p>
        <ol style="font-size:100%">
            <li><span style="color:yellowgreen">PP08 deadline<br>(2023-11-10)</span></li>
        </ol> 
    </td>
</tr>


<tr style="font-size:100%">
    <td><strong style="color:orange">11(40)</strong></td>
    <td><strong><em>Lecture 21:</em></strong>
        <em>2023-11-14</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td><strong><em>Lecture 22:</em></strong>
        <em>2023-11-16</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp10" target="_blank">
                <strong><em>PP10: <span style="font-size:100%">(2023-11-13)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            TBD
            </p>
        </div>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <!--<strong><em>Note:</em></strong>-->
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
            <!--Handouts are typeset in <span style="color:yellowgreen">green</span>
            and deadlines in <span
            style="color:tomato">red</span>.
            All deadlines are due 11:59 pm.-->
        </p>
        <ol style="font-size:100%">
            <li><span style="color:yellowgreen">PP09 deadline<br>(2023-11-17)</span></li>
        </ol> 
    </td>
</tr>

<tr style="font-size:100%">
    <td><strong style="color:orange">12(40)</strong></td>
    <td><strong><em>Lecture 23:</em></strong>
        <em>2023-11-21</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td style="background-color: rgba(174, 129, 255, 0.1);">
        <strong style="color:rgba(174, 129, 255,1)">
            <em>Thanksgiving break:</em>
        </strong>
        <em>2023-11-23</em>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
<!--        <div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp11" target="_blank">
                <strong><em>PP11: <span style="font-size:100%">(2023-11-20)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            </p>
        </div>-->
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <!--<strong><em>Note:</em></strong>-->
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
            <!--Handouts are typeset in <span style="color:yellowgreen">green</span>
            and deadlines in <span
            style="color:tomato">red</span>.
            All deadlines are due 11:59 pm.-->
        </p>
        <ol style="font-size:100%">
            <!--<li><span style="color:yellowgreen">HW1 deadline<br>(2023-09-27)</span></li>-->
        </ol> 
    </td>
</tr>


<tr style="font-size:100%">
    <td><strong style="color:orange">11(40)</strong></td>
    <td><strong><em>Lecture 24:</em></strong>
        <em>2023-11-28</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td><strong><em>Lecture 25:</em></strong>
        <em>2023-11-30</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <!--<div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp1" target="_blank">
                <strong><em>PP3: <span style="font-size:100%">(2023-09-25)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            Topics PP03
            </p>
        </div>-->
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <!--<strong><em>Note:</em></strong>-->
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
            <!--Handouts are typeset in <span style="color:yellowgreen">green</span>
            and deadlines in <span
            style="color:tomato">red</span>.
            All deadlines are due 11:59 pm.-->
        </p>
        <ol style="font-size:100%">
            <!--<li><span style="color:yellowgreen">HW1 deadline<br>(2023-09-27)</span></li>-->
        </ol> 
    </td>
</tr>

<tr style="font-size:100%">
    <td><strong style="color:orange">11(40)</strong></td>
    <td><strong><em>Lecture 26:</em></strong>
        <em>2023-12-05</em>
        <br>
        <ul style="font-size:100%">
            <!--<li>TOPIC 1</li>-->
        </ul>
    </td>
    <td style="background-color: rgba(0, 128, 128, 0.1);">
        <strong style="color:teal">
            <em>Reading period:</em>
        </strong> 
            <em>2023-12-07</em>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <!--<div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp1" target="_blank">
                <strong><em>PP3: <span style="font-size:100%">(2023-09-25)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            Topics PP03
            </p>
        </div>-->
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <!--<strong><em>Note:</em></strong>-->
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
            <!--Handouts are typeset in <span style="color:yellowgreen">green</span>
            and deadlines in <span
            style="color:tomato">red</span>.
            All deadlines are due 11:59 pm.-->
        </p>
        <ol style="font-size:100%">
            <!--<li><span style="color:yellowgreen">HW1 deadline<br>(2023-09-27)</span></li>-->
        </ol> 
    </td>
</tr>

<tr style="font-size:100%">
    <td><strong style="color:orange">11(40)</strong></td>
    <td style="background-color: rgba(64, 224, 208, 0.1);">
        <strong style="color:turquoise">
            <em>Final exam period:</em>
        </strong>
        <em>2023-12-12</em>
    </td>
    <td style="background-color: rgba(64, 224, 208, 0.1);">
        <strong style="color:turquoise">
            <em>Final exam period:</em>
        </strong>
        <em>2023-12-14</em>
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.1);">
        <strong><em></em></strong>
        <p
        style="margin-top:0;margin-bottom:0;font-size:100%">
        </p>
        <!--<div style="margin-top:2px">
            <a href="https://code.harvard.edu/CS107/main/tree/master/lab/pp1" target="_blank">
                <strong><em>PP3: <span style="font-size:100%">(2023-09-25)</span></em></strong>
            </a>
            <p style="margin-top:0;margin-bottom:0;font-size:100%">
            Topics PP03
            </p>
        </div>-->
    </td>
    <td style="background-color: rgba(101, 123, 131, 0.06);">
        <!--<strong><em>Note:</em></strong>-->
        <p style="margin-top:0;margin-bottom:0;font-size:100%">
            <!--Handouts are typeset in <span style="color:yellowgreen">green</span>
            and deadlines in <span
            style="color:tomato">red</span>.
            All deadlines are due 11:59 pm.-->
        </p>
        <ol style="font-size:100%">
            <!--<li><span style="color:yellowgreen">HW1 deadline<br>(2023-09-27)</span></li>-->
        </ol> 
    </td>
</tr>

</tbody>
</table>

