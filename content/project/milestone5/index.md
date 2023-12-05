Title:  Milestone 5
Category: Project
Date: 2023-12-04
Slug: M5
Author: Ignacio Becker

>  **Monday, December 11th, 09:59 PM**

With the development in full swing, many modules should now be ready. This milestone is to ensure that some of these modules work together correctly.


### API tunning
During project development, you'll gain insights about the structure and modules. It's possible that the initial API isn't ideal, so you might need to revise it. This involves updating the API documentation, diagrams, and, most importantly, the code to align with the new API.

If your API draft still meets the contract requirements, you can choose not to modify it. In this case, add a small appendix explaining why it remains unchanged.

In the remainder of this document, we'll refer to the latest version of the API as the `modified` version.

### Features and Integration

Developing individual features is usually straightforward. The real challenge lies in integrating them smoothly. For this item, develop features from different modules and conduct integration tests using GitHub Actions. You can merge features into the `dev` branch once they pass your tests. However, keep the feature development branches until reviewed by the teaching staff.

Make sure to commit often in the local repository, `as it is part of the evaluation`. Tests must be *commited and pushed* before any code is written.

- Design and write your integration tests based on the `modified` API.
- Work on at least two consecutive modules. This includes writing unit tests, coding, and documentation.
      - If the modules are already created: Merge the integration tests into the `dev` branch.
      - If only one module is developed: Merge the integration tests into `dev` before starting the second module.
      - If no modules are created: Merge the integration tests into `dev` first, before any module development.
- Successful integration of two modules is confirmed when all integration tests pass.

`Note`: Regularly commit to your local repository and tidy up the history as needed. Push your changes only after passing the unit tests.

### SFS clarifications and modifications

<!-- You should focus on developing the code and even using placeholder functions. As stated in the contract, any modification should be easy and straightforward to change. -->
Your main focus should be to complete the pipeline. Use placeholder functions if necessary. Any modifications, as per the contract, should be straightforward.


### Clarifications of the Software Requirements Specifications
For Annex A:

* 3.A: Each task listed in this item should be aplpied to one spectrum.
* 3.B: Include the class (STAR, GALAXY, or QSO) in the metadata. The spectrum is the data; metadata is everything else related to it.
* 3.C: Aligning in wavelength means sub-sampling the wavelengths. For a given list of target wavelengths, return a flux value for each.
* 4: The inferred continuum is a line derived from the data, excluding any emission or absorption lines.
* 5: Data augmentation module execution is optional. If used, the user inputs the degree of required derivatives.

For Annex B:

* 2: The machine learning module should primarily use spectral data. It can include other metadata. The results should report a confussion matrix.
* 3: Total flux of spectral lines must use an inferred continuum. The method for calculating line area is defined by Developer, and should be well-documented and easily modifiable.

#### Modifications of the Software Requirements Specification
* Annex A - 3.B: Replace chemical abundances with the value of Equivalent Width for each line detected by the SDSS pipeline.
* Annex B - New task: Report the chemical abundances of stars from the [APOGEE survey](https://www.sdss4.org/dr17/irspec/).


## Steps to complete

1. Re-evaluate the document written in the folder `draft_API`. Make the require modifications both in your diagram and the document.
2. Based on the `modified` API, reorganize your library in the `dev` branch.
3. Write the integration tests on the `dev` branch.
4. Complete the implementation of at least two modules and test their integration. Every change in the library should trigger integration tests.
5. In `milestone5`, describe the rationale behind any API changes. This should include:
      - Why the API was modified, focusing on how the changes improve functionality, usability, or adaptability to project requirements.
      - Discuss how these changes enhance the integration of different modules. List the specific module names that need to be evaluated by the teaching staff for their integration.

## Final Deliverables
The final deliverables for this milestone should be uploaded only on the Github page. No emails are neccesary.

1. Updated API document and its diagram. Place these in the `draft_API` folder.
2. The `docs/` directory should include a document called `milestone5`.
3. Integration tests for *at least* two modules.

`Note 1`: By now you should have implemented many modules, and most of the items requested in the milestone.

`Note 2`: The reading period ranges from December 6th to December 10th. You are <span style="font-size:28px;">**highly encouraged**</span> to submit earlier (notifying your liaison by email) to receive feedback.


## Grading breakdown

> | **Points** | **Task**                        |
> |------------|---------------------------------|
> | 15         | API                             |
> | 20         | Modules                         |
> | 20         | Integration tests               |
> | 55         | **Total**                       |

