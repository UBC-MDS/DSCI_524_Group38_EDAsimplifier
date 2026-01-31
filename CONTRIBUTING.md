# Contributing

This repository is developed as part of a collaborative, course based software
development project. Contributions are primarily made by student team members
following an agreed-upon workflow and milestone plan. External contributions
are welcome but may be reviewed within the constraints of the course timeline.
All contributions must follow and accept the [Code of Conduct ](./CODE_OF_CONDUCT.md).

## Example Contributions

You can contribute in many ways, for example:

* [Report bugs](#report-bugs)
* [Fix Bugs](#fix-bugs)
* [Implement Features](#implement-features)
* [Write Documentation](#write-documentation)
* [Submit Feedback](#submit-feedback)

### Report Bugs

Report bugs at https://github.com/UBC-MDS/eda_simplifier/issues.

**If you are reporting a bug, please follow the template guidelines. The more
detailed your report, the easier and thus faster we can help you.**

### Fix Bugs

Look through the GitHub issues for bugs. Anything labelled with `bug` and
`help wanted` is open to whoever wants to implement it. When you decide to work on an issue,
please assign yourself to it. For this project, each core feature or function
should be owned by a single team member to ensure equal contribution across the team.


### Implement Features

Look through the GitHub issues for features. Anything labelled with
`enhancement` and `help wanted` is open to whoever wants to implement it. As
for [fixing bugs](#fix-bugs), please assign yourself to the issue and add a comment that
you'll be working on that, too. If another enhancement catches your fancy, but it
doesn't have the `help wanted` label, just post a comment, the maintainers are usually
happy for any support that they can get.

### Write Documentation

EDA_simplifier could always use more documentation, whether as
part of the official documentation, in docstrings, or even on the web in blog
posts, articles, and such. Just
[open an issue](https://github.com/UBC-MDS/eda_simplifier/issues)
to let us know what you will be working on so that we can provide you with guidance.

### Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/UBC-MDS/eda_simplifier/issues. If your feedback fits the format of one of
the issue templates, please use that. Remember that this is a volunteer-driven
project and everybody has limited time.

## Get Started!

Ready to contribute? Here's how to set up EDA_simplifier for
local development.

1. Fork the https://github.com/UBC-MDS/eda_simplifier
   repository on GitHub.
2. Clone your fork locally (*if you want to work locally*)

    ```shell
    git clone git@github.com:your_name_here/eda_simplifier.git
    ```

3. [Install hatch](https://hatch.pypa.io/latest/install/).

4. Create a branch for local development using the default branch (typically `main`) as a starting point. Use `fix` or `feat` as a prefix for your branch name.

    ```shell
    git checkout main
    git checkout -b fix-name-of-your-bugfix
    ```

    Now you can make your changes locally.

5. When you're done making changes, apply the quality assurance tools and check
   that your changes pass our test suite. This is all included with tox

    ```shell
    hatch run test:run
    ```

6. Commit your changes and push your branch to GitHub. Please use [semantic
   commit messages](https://www.conventionalcommits.org/).

    ```shell
    git add .
    git commit -m "fix: summarize your changes"
    git push -u origin fix-name-of-your-bugfix
    ```

7. Open the link displayed in the message when pushing your new branch in order
   to submit a pull request.

## Development Workflow

This project follows a GitHub Flow–based workflow:

- All work is tracked through GitHub issues
- New work is done on feature or fix branches created from `main`
- All changes must be submitted via pull requests
- Each pull request should be reviewed by at least one other team member before merging

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests when functionality is implemented.
   Documentation-only changes (e.g., Milestone 1 specifications) are not expected
   to include tests.
2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring.
3. Your pull request will automatically be checked by the full test suite.
   It needs to pass all of them before it can be considered for merging.
4. For early milestones, function docstrings serve as formal specifications and
   may exist without an implementation.

## Retrospective: Tools, Infrastructure, and Practices

### Development Tools

Building EDA_simplifier gave us hands-on experience with a modern Python packaging workflow. We used [Hatch](https://www.pyopensci.org/python-package-guide/tutorials/get-to-know-hatch.html) as our build system and environment manager. This eliminated the need to set up conda environments, conda lock files, and docker containers. Hatch let us define isolated environments for testing, documentation, and building, all configured in a single `pyproject.toml` file.

For testing, we used [pytest](https://docs.pytest.org/en/stable/getting-started.html). Writing unit tests for each function in separate files (e.g., `test_dataset_overview.py`, `test_numeric.py`) taught us to think about edge cases (such as empty DataFrames, invalid input types) before writing production code. Each member regularly tests their code before pushing their contribution to the `main` branch.

Code quality was enforced through [Ruff](https://docs.astral.sh/ruff/) for linting and [Black](https://pypi.org/project/black/) for formatting. Having these run automatically in CI resulted in a consistent coding style throughout all milestones.

For documentation, we used [Quarto](https://quarto.org/docs/guide/) to auto-generate an [API reference site](https://ubc-mds.github.io/DSCI_524_Group38_EDAsimplifier/reference/) from our function docstrings. This taught us that good docstrings need to include parameters, return types, and examples. Through the peer review process, we also recognized the importance of having good examples, because that is what most users and developers try when exploring a new package.

### GitHub Infrastructure

We set up four GitHub Actions workflows that automated most of our quality assurance:

1.  **CI (`ci.yml`)**: Runs on every push and pull request. Tests across a matrix of 3 operating systems (Ubuntu, macOS, Windows) and 4 Python versions (3.10–3.13), giving us 12 test combinations. This caught platform-specific issues we would never have found testing only on our own machines.
2.  **CD (`cd.yml`)**: Automatically builds and publishes the package to TestPyPI after the full CI suite is passed.
3.  **Docs publishing (`docs-publish.yml`)**: Builds our Quarto site and deploys it to GitHub Pages on every push to `main`, keeping our documentation always up to date.
4.  **Docs preview (`docs-preview.yml`)**: Deploys a preview to Netlify so reviewers can see rendered documentation changes before merging.

We added badges for some of these workflows on our README to get a quick glance that the actions are working. Beyond workflows, we used [Codecov](https://docs.codecov.com/docs/quick-start) for coverage tracking.

### Organizational Practices

Each core function was owned by a single team member to ensure equal contribution and clear accountability. This worked well for a four-person team building four main functions. Weekly meetings allowed us to stay on top of milestone deadlines, troubleshoot issues together, and discuss any bottlenecks. We also used a [Kanban](https://github.com/orgs/UBC-MDS/projects/331) project board to keep track of all outstanding issues. Slack was used for informal conversations.

### Scaling Up: What We Would Add

If we were to scale this project (or start a new, larger one), we would adopt the following additional tools and practices:

-   **Containerized development environments**: Our `environment.yml` works for conda users, but a `Dockerfile` or Dev Container configuration would provide fully reproducible environments regardless of the host system, which becomes important when onboarding new contributors who may use different operating systems or package managers.

-   **Publishing to PyPI**: Our current deployment targets TestPyPI, which is appropriate for a course project. A real production package would publish to the main Python Package Index, with stricter testing rules (e.g., requiring all matrix tests to pass and manual approval before publishing).

-   **CODEOWNERS file**: As the team grows, a `CODEOWNERS` file in `.github/` would automatically request reviews from the right people based on which files a PR touches, ensuring the right person always reviews relevant changes.
