Title: Syllabus
Slug: syllabus
Date: 2022-07-25

## <a id="cobjective"></a><a class="anchor-link" href="#cobjective">Course Objective</a>

The primary goal of this course is to teach you how to develop effective
software for scientific applications. In order to achieve this goal, there are
several non-negotiable topics that must be included in the course.  We will be
concerned with two primary thrusts:  _System and Software Engineering_ and
_Language_.  Moreover, we aim to provide you with a suite of modern software
development techniques and workflows.

A short `pdf` version of the syllabus can be [downloaded
here]({attach}/pages/media/cs107_syllabus.pdf).


## <a id="lobjective"></a><a class="anchor-link" href="#lobjective">Learning Objective</a>

After successful completion of this course, you will be able to:

> * Use Python, including its advanced features to write scientific programs
> * Have a basic idea how the Python interpreter works
> * Understand what features of Python make up its language execution model and how these features impact
>   the code you write: e.g. how modularity, abstraction, and encapsulation can
>   be used to solve problems
> * Write programs with good software engineering practices.  These
>   practices include: working on remote machines, version control, continuous
>   integration, documentation and testing.
> * Utilize data management techniques to store data, starting from a good
>   understanding of data structures to databases.
> * Combine these techniques together to write large pieces of software (you
>   will do a group project for this), working in a team of scientists,
>   programmers, etc.
> * Combine these techniques together to write large pieces of software working in a team.
> * Develop pipelines to integrate data aquisition and processing.
> * Evaluate and test software to see which one your group ought to use.
> * Evaluate and test software as part of the development process. 
> * Be able to contribute on both the science and software engineering sides of
>   things.


## <a id="prerequisites"></a><a class="anchor-link" href="#prerequisites">Prerequisites</a>

You should have some basic familiarity with programming (functions, variables,
constants, differences between integer and floating point, etc.) at the level of
CS50. Some comfort with a tool to edit text files is beneficial. Any text
editor or IDE will suit this purpose.

The student should have passed a basic calculus class. The lectures will review the necessary fundamentals
required to succeed with the class project.

Besides this, you should have interest or investment in scientific computing.

You can download Homework 0 for self-assessment
[here]({attach}/pages/media/hw0.pdf) (not graded).  You do not need to be able
to solve all problems in order to take this class.


### <a id="prerequisites-jupyter"></a><a class="anchor-link" href="#prerequisites-jupyter">Jupyter Notebooks</a>

[Jupyter](https://jupyter.org/) notebooks are great for code prototyping and
learning how to use new features and APIs. However,
they are **not** suitable for large software development projects!  One reason
for this is because code development in Jupyter notebooks is a nonlinear
development process and there is presently no good solution 
for version control of Jupyter notebooks.  A second reason is the question of
efficient source editing.  A helpful tool to convert (back and forth) Jupyter 
notebooks to pure python code is [Jupytext](https://pypi.org/project/jupytext/).

> **Homework assignments and lecture exercises turned in as Jupyter notebooks
> will not be graded.**


## <a id="textbooks"></a><a class="anchor-link" href="#textbooks">Textbooks</a>

There is no required course textbook.  However, the course content will draw
from various sources.  We will cite the source when appropriate.  Please consult
the [resources page]({filename}resources.md) for recommended textbooks and
additional helpful material. 


## <a id="course-format"></a><a class="anchor-link" href="#course-format">Course Format</a>

The delivery of course content will occur via two weekly lectures as well as
weekly pair-programming sections.  Attending these sessions is **mandatory**.
   Lectures will consist of considerable interaction and discussion and will be
   greatly enhanced by student participation.

   The course contains the following main components:

1. **Lectures:** Deliver the main content of the class.   <a
   href="./syllabus.html#attendance-policy">Attendance is mandatory.</a>
2. **Quizzes:** Graded in-class quizzes intended to assess the learning progress.
3. **Pair-programming:** Pair-programming (PP) sections offer practice on topics
   addressed in class and help assess the skills to program in a collaborative
   environment.  <a href="./syllabus.html#attendance-policy">Attendance is
   mandatory.</a>
4. **Homeworks:** Homework assignments deepen the lecture material and include
   coding exercises.  Exercises may be of theoretical or practical nature.
5. **Projects:** The class is accompanied by a project (teams of 4-5 students)
   to practice the methods learned in class on a real Python application.  The
   project topic is given by the teaching staff.

The main programming language taught throughout the course is Python.  In
addition, a voluntary [`C/C++` primer class]({filename}cpp_primer.md) that
consists of 10 lectures will be held during the semester.  This primer is highly
recommended if you like to strengthen your skills in a programming language that
is closer to the hardware and widely used in research and industry.  If you plan
on taking [CS205](https://harvard-iacs.github.io/2022-CS205/) in the spring
semester, please consider taking this primer as basic knowledge of `C/C++` will
be required for that class.


### <a id="grading"></a><a class="anchor-link" href="#grading">Grading</a>

> The following weight table is used for individual components of the class. The
> class does not have standard midterm or final exams.
>
> |                                              | Total Weight |
> |----------------------------------------------|--------------|
> | [**Homework**](#homework) (7 Homeworks)      | 35%          |
> | [**Project**](#project)                      | 35%          |
> | [**Quizzes**](#quizzes)  (4 Quizzes)         | 15%          |
> | [**Pair-programming**](#pp) (12 sections)    | 15%          |
<!-- > | [**Pair-programming**](#pp) (12 sections)    | 10%          | -->
<!-- > | [**Communal Contributions**](#contributions) | 5%           | -->


### <a id="homework"></a><a class="anchor-link" href="#homework">Homework</a>

There are **7 homework assignments** where each contributes equally to the final
grade. The homework is focused on the topics discussed in class and involves
programming and theoretical work.  The teaching staff is determined to return
solutions and graded assignments with feedback after the due date.  It
is _your responsibility_ to check the consistency between your graded work and
the assignment solution.  You have the option to address possible
inconsistencies in office hours or request a regrading for the assignment (see
the <a href="./syllabus.html#homework-regrade">homework grading
inconsistencies</a> section below). Homework will be released on the
[CS107/AC207 class repository](https://code.harvard.edu/CS107/main).  Push
notifications for that repository will be distributed through the <a
href="../#class-mailinglist">class mailing list</a>.  Homework will be graded on
a 100 point scale:

> * 100 = Solid / no mistakes (or really minor ones)
> * 80 = Good / some mistakes
> * 60 = Fair / some major conceptual errors
> * 40 = Poor / did not finish
> * 20 = Very Poor / little to no attempt.
> * 0 = Did not participate / did not hand in


#### <a id="homework-submission"></a><a class="anchor-link" href="#homework-submission">Homework Submission</a>

Homework must be submitted via commits in your private `git` repository hosted
in the CS107 organization at <https://code.harvard.edu/CS107>.  Grading and
feedback for homework is done through the [Gradescope
platform](https://canvas.harvard.edu/courses/108118/external_tools/89451?display=borderless)
which is connected to the class' [Canvas
site](https://canvas.harvard.edu/courses/108118).  Your homework solutions must
therefore be zipped and uploaded in the Gradescope section of the class canvas.
See the <a href="./tutorials.html#tutorial-hw">homework workflow tutorial</a>
for more details.

The homework due date is indicated on the problem sheet and displayed in the <a
href="./schedule_static.html">schedule</a> as well as shown on Canvas and
Gradescope.  Homework submissions will be graded on:

1. **Correctness:** your code must run and must produce the correct
   result.  We are not debugging issues when grading submissions.
2. **Presentation:** presentation means structure and readability. We expect you
   to write high-quality, readable and tested code. A quality code is well
   commented in places where it is not straight forward to deduce the logic from
   code itself (from the reviewers perspective).  We expect you to think about
   aspects such as modularity, reusability, code duplication and error handling
   when you design and write code. Presentation of results also means that
   unnecessary or superfluous files like editor backup files or other unrelated
   data should not be included in the submission commits (use `.gitignore` for
   this purpose).

> See the following tutorials to help you get started with homework submissions:
>
> * <a href="./tutorials.html#tutorial-repo">How to setup your private class repository</a> (onetime setup)
> * <a href="./tutorials.html#tutorial-hw">Homework workflow</a>


#### <a id="homework-late"></a><a class="anchor-link" href="#homework-late">Homework Late Days</a>

Homework submissions are accepted before the deadline of the assignment is due.
You have **three late days** at your disposal that can be consumed for late
submissions and two consecutive late days can be used at most for any of the
homework assignments.

Please note that any commits on your homework branch pushed _after the deadline
has passed are not considered for grading_ by default.  If you wish that we
consider a late commit for grading, 
please contact the teaching staff at
[`cs107-staff@g.harvard.edu`](mailto:cs107-staff@g.harvard.edu)
with appropriate explanation.  This will count towards your late day budget.

It is your responsibility to plan your work ahead and commit on time.  If you
have consumed all your late days and you have another late submission, it is in
your benefit to still commit the work.  We assume the [Harvard Honor
Code](https://honor.fas.harvard.edu/honor-code) for all late submissions in case
solutions are already posted.

If you have a verifiable medical condition or other special circumstances that
interfere with your coursework please let us know via 
[`cs107-staff@g.harvard.edu`](mailto:cs107-staff@g.harvard.edu)
as soon as possible.


#### <a id="homework-regrade"></a><a class="anchor-link" href="#homework-regrade">Homework Grading Errors</a>

If you believe there is an error in your assignment grading, you can submit a
regrade request through the [Gradescope
platform](https://canvas.harvard.edu/courses/108118/external_tools/89451?display=borderless).

> **Note:**
>
> 1. The **entire** assignment will be regraded.  _This may cause your total
>    grade go up or down_.
> 2. An assignment can only be **regraded once**.
> 3. Regrade requests are **due within 2 days after the release of the grades**.

### <a id="project"></a><a class="anchor-link" href="#project">Project</a>

Please see the <a href="./project.html">project</a> section for more details.


### <a id="quizzes"></a><a class="anchor-link" href="#quizzes">Quizzes</a>

There are **4 quizzes** out of class which are graded and intended to assess the
learning progress.  Each quiz addresses topics _from the lecture material_.
Quizzes are open book/`www` and include multiple choice questions with at most
back of the envelope calculations.  Quizzes contain 12 questions and take 25
minutes.  They are accessible on canvas within a 12 hour time window from 9am to
9pm at the day of the quiz.

> **Note:** if a quiz takes 25 minutes and you start the quiz on 8:50pm, you
> will have only 10 minutes to work on the quiz.
>
<!-- > * **Quiz 1: September 22nd, 7:00pm - 7:45pm**, Lecture 1 to 5 -->
> * **Quiz 1: September 22nd, 7:00am - 7:45pm**, Lecture 1 to 5
> * **Quiz 2: October 13th, 9:00am - 9:00pm**, Lecture 6 to 9 
> * **Quiz 3: November 10th, 9:00am - 9:00pm**, Lecture 10 to 16
> * **Quiz 4: December 1st, 9:00am - 9:00pm**, Lecture 17 to 24
>
> Please see the class <a href="./schedule_static.html">schedule</a> as well.


### <a id="pp"></a><a class="anchor-link" href="#pp">Pair-Programming Sections</a>

Pair-Programming will form an essential part of the course. Pair-programming
will take place in **mandatory** pair-programming sections led by members of the
teaching staff.  You are required to sign-up for your preferred pair-programming
section at the beginning of the semester.  You are expected to attend your
chosen section during the semester.  Should you not be able to attend one of
your sections, please coordinate with your section TF to attend another section
this week in order to obtain the attendance credit.

In CS107/AC207 we are focusing on command line tools for the development of
software projects in computational science.  It is important that you get
familiar with a small selection of such tools and integrate them in your
development process. The pair-programming sections aim at combining some of
these tools together to provide you with hands-on experience while developing
software.  The key is the "pair" in pair-programming.  The exchange of knowledge
between team mates in these pair-programming sections is essential for learning
said tools or learning something new from your peers.

> Please see the following file in the class `git` repository for the details:
>
> * <https://code.harvard.edu/CS107/main/blob/master/lab_groups.xls>

#### <a id="pp-submission"></a><a class="anchor-link" href="#pp-submission">Pair-programming Submissions</a>

Pair-programming exercise solutions must be submitted in your private `git`
repository hosted in the CS107 organization at <https://code.harvard.edu/CS107>.
**Only commits before or at the due date are considered for grading**.  The
deadline for submission is usually _one week_ after the last section for the
exercise.  Given this extra time for completion, **late days do not apply to
pair-programming exercises**.

The submission due date is indicated on the problem sheet and displayed in the
<a href="./schedule_static.html">schedule</a>.  As you are working in groups of
3-4 students for the lab exercises, the solution files you come up with in the
group are submitted by each group member individually in her/his own private Git
repository. Pair-programming submissions will be graded on:

1. **Attendance:** your attendance will be recorded by the TF who leads the
   section. Joining the section at the beginning and then leaving 10-15 minutes
   later will not reward attendance credit.  If you need to leave because of
   another appointment then it is expected that you communicate before hand and
   coordinate with your TF. Please see the <a
   href="./syllabus.html#attendance-policy">attendance policy</a> section below
   as well.  Your pair-programming session is determined at the beginning of the
   class by choosing lab sections in [my.harvard](https://my.harvard.edu/).  You
   can select your preferences depending on your schedule. Once determined, you
   can lookup your session details in the
   <https://code.harvard.edu/CS107/main/blob/master/lab_groups.xls> sheet.
2. **Completion:** pair-programming submissions should reveal effort that the
   student attempted to solve the tasks.  If you experience difficulties in a
   particular problem and you are not able to complete the task, please indicate
   the issues you had in your code using comments and we will take that
   reasoning into account.  Handing in an empty skeleton (same as hand-out) does
   not meet the expected standard and will not award credit for the submission.

> See the following tutorial to help you get started with pair-programming
> submissions:
>
> * <a href="./tutorials.html#tutorial-pp">Pair-programming workflow</a>


<!--### <a id="contributions"></a><a class="anchor-link" href="#contributions">Communal Contributions</a>

The frequency with which you visit and/or post to the <a
href="../#class-forum">class forum</a> can contribute to your final <a
href="./syllabus.html#grading">grade</a>.  These contributions must have
intellectual value and can be in the form of questions and/or answers related to
class material.  Be mindful about sharing sensitive material such as solution
code for homeworks.  If in doubt, try to rephrase your question/answer or ask
the teaching staff via
[`cs107-staff@g.harvard.edu`](mailto:cs107-staff@g.harvard.edu)
whether the content is permissible to share.  Factors that contribute are
frequency of visits, posing questions, giving answers, commenting and liking
posts as well as creating posts.-->


### <a id="office-hours"></a><a class="anchor-link" href="#office-hours">Office Hours</a>

The teaching staff holds weekly office hours. Office hour times and locations
are listed on the class main page. Office hours provide you with an opportunity
to review and discuss course materials as well as provide you with further
guidance for your homework.

> Please see the following file in the class `git` repository for the details:
>
> * <https://code.harvard.edu/CS107/main/blob/master/office_hours.xls>


## <a id="attendance-policy"></a><a class="anchor-link" href="#attendance-policy">Attendance Policy</a>

Lectures and pair-programming sections are core parts of the class and therefore
mandatory to attend.  

Pair-programming sections (labs) will be held on weekdays that we determine at
the beginning of the class according to a best fit of the students' individual
schedules for the term.  You are required to attend the labs at the assigned lab
day.  Rescheduling of a lab to a different day due to an unforeseeable event
must be coordinated with the responsible TF by sending an email to
[`cs107-staff@g.harvard.edu`](mailto:cs107-staff@g.harvard.edu).

> To be excused from a lecture or a lab, we ask you to follow the [Harvard Honor
> Code](https://honor.fas.harvard.edu/honor-code) and send an email to
> [`cs107-staff@g.harvard.edu`](mailto:cs107-staff@g.harvard.edu)
> at least one day before the lecture or lab.  Lecture recordings are available
> only when students are excused for a lecture.


### <a id="attendance-policy-zoom"></a><a class="anchor-link" href="#attendance-policy-zoom">Zoom</a>

Classes and labs will be streamed via zoom for you to attend real time while in
isolation.  Note that attendance on zoom is not a substitute for in-person
participation.  The main attention will be on the physical audience present
(unless the entire class must be shifted to virtual meetings depending on
Harvard COVID updates). Please follow the steps in the "Attendance Policy"
section above to attend the zoom streams.  If you are isolating you must not
send notifications for every lecture or lab, one notification to let us know is
sufficient.  Thank you.

> Please see the <a href="../#important">important information</a> for the
> canvas page that contains the lecture zoom link.
>
> The zoom links for the lab sessions and office hours are given in the
> `lab_groups.xls` and `office_hours.xls` files in the main class `git`
> repository:
>
> <https://code.harvard.edu/CS107/main>


## <a id="collaboration-policy"></a><a class="anchor-link" href="#collaboration-policy">Collaboration Policy</a>

You are welcome to discuss the course material and homework with others in order
to better understand it, but the work you turn in must be your own (with
exception of the project where collaborative work is permitted). Any work that
is not your own, without properly citing the original author(s), is considered
plagiarism. Failure to follow the academic integrity and dishonesty guidelines
outlined in the [Harvard Student
Handbook](https://handbook.college.harvard.edu/) will have an adverse effect on
your final grade. This includes the removal of copyright notices in code. You
may not submit the same or similar work to this course that you have submitted
or will submit to another without permission.  The teaching staff may use tools
to compute correlations between submitted work.


## <a id="accessibility"></a><a class="anchor-link" href="#accessibility">Accessibility</a>

If you have a documented disability (physical or cognitive) that may impair your
ability to complete assignments or otherwise participate in the course and
satisfy course criteria, please contact the teaching staff or directly the
[Accessible Education Office](https://aeo.fas.harvard.edu/) to receive an AEO
letter that will authorize us to help you with corresponding accommodations.


## <a id="diversity-statement"></a><a class="anchor-link" href="#diversity-statement">Diversity Statement</a>

All participants in this class are expected to foster empathy and respect
towards each other.  This includes instructors, teaching staff or students.  The
motivation to take this course shall be to experience the joy of learning in an
environment that allows for a diversity of thoughts, perspectives and
experiences and honors your identity including race, gender, class, sexuality,
religion, ability, etc.  Any constructive feedback for improving the class
environment is welcome and I encourage you to reach out to the instructor or
teaching staff with any concerns you may have. If you prefer to speak with
someone outside of the course, you may find helpful resources at the [Harvard
Office of Diversity and Inclusion](https://diversity.college.harvard.edu/).
