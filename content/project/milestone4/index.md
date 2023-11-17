Title:  Milestone 4
Category: Project
Date: 2023-11-16
Slug: M4
Author: Ignacio Becker

> **Due: Monday, November 27th, 09:59 PM**

You will now start the development of the library modules. As part of test-driven design, you should first write the tests of a functionality, and then write the code, based on the API you defined in Milestone 3.

### Software Organization
Before any code is written, discuss how you plan on organizing your software package. With the idea of classes/modules in mind, organize your code according to the API identified in milestone 3. This is a more detailed organization and should reflect said API (If you already did this for milestone 3, you may use it for milestone 4 or expand it if you need it).

* What will the directory structure look like?
* Where will your test suite live?
* How will you distribute your package (e.g. `PyPI` with PEP517/518 or simply `setuptools`)?
* Other considerations?

Describe your choices in the `milesone4` document (even if you already wrote it for milestone 3). You have to follow the guidelines shown during lectures.

### Licensing

Licensing is an essential consideration when you create new software.  You should choose a suitable license for your project.  A comprehensive list of licenses can be found [here](https://spdx.org/licenses/).  The license you choose depends on factors such as what other software or libraries you use in your code ([copyleft](https://www.gnu.org/licenses/copyleft.html), copyright). Will you have to deal with patents?  How can others advertise software that makes use of your code (or parts thereof)?  You may consult the following reading to aid you in choosing a license:

* [Helper to choose a license](https://choosealicense.com/)
* [Licenses](https://www.gnu.org/licenses/licenses.html)
* [License recommendations](https://www.gnu.org/licenses/license-recommendations.html)
* [License compatibility](https://www.gnu.org/licenses/license-compatibility.html)
* [Extensive list of open source licenses](https://spdx.org/licenses/)

Briefly motivate your license choice in the `milesone4` document and add a `LICENSE` file to the root of your project.

### Implementation

New features should be developed on independent branches. For this, you will leave the `main` branch only for the code graded by the teaching staff. The branch `dev` will contain the code in development. You are free to create as many branches as you need and merge them into `dev`. *Do not delete the branches used to develop new features until the teaching staff review them.*
Remember that you can also create as many workflows as you want.

* Select at least one module identified in Milestone 3 and implement it.
* What method and name attributes will your class have?
* What methods and attributes will you expose to the user?
* Do you want/need to depend on other libraries? (e.g. NumPy)
* Write a comprehensive test suite for this module(s), according to your API. This might change in the future as you learn more about your code.
* Write the code of the module along with its documentation.

`Note`: You can commit multiple times to your local repository and clean the local history if needed. Push only when you pass the tests.

## Steps to complete

1. In the `main` branch and within your `docs` sub-directory, create a file called `milestone4`. The type of file is up to you and your group. Two acceptable choices are markdown (`milestone4.md`) or a Jupyter notebook (`milestone4.ipynb`).
2. Your `milestone4` document submission should be in the following format:

```
teamXX/
├── docs
│   └── milestone4
├── LICENSE
├── README.md
└── ...
```
3. Describe the software organization and licencing in `milestone4`.
4. Create branch `dev`.
5. Create the branch `featurename` to implement your module. Replace "featurename" with the name of the module you want to implement.
6. In that branch, write the tests for the module you want to implement. *You should commit them before the writing/pushing any other code*.
7. Write the code for the module you wrote the tests for.
8. Every test for the modules should pass.
9. The code coverage must be at least 90%.
10. Merge the branch into `dev`.
11. (Optional) You can implement another feature, following steps 5-10. You are encouraged to develop the main modules as soon as possible, to focus on the integration later on.


## Final Deliverables

1. The `docs/` directory should include a document called `milestone4` (the
   extension is up to you, but `.md` or `.ipynb` are recommended.
2. Proper licensing of your project.
3. Tests and implementation for your module(s).



## Grading breakdown

> | **Points** | **Task**                        |
> |------------|---------------------------------|
> | 4          | Software Organization           |
> | 4          | License                         |
> | 15         | Implementation                  |
> | 15         | (optional) Additional implementation       |
> | 23(38)     | **Total**                       |

