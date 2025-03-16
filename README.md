![Python build & test](https://github.com/software-students-spring2025/3-python-package-teamproj3/actions/workflows/event-logger.yml/badge.svg)

![CI/CD](https://github.com/software-students-spring2025/3-python-package-teamproj3/actions/workflows/build.yml/badge.svg)
# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

# Fortune Cookie Python Package

## Team Members
[Oluwapelumi Adesiyan](https://github.com/oadesiyan) <br />
[Nikita Bhaskar](https://github.com/nikitabhaskar) <br />
[Ariya Mathrawala](https://github.com/ariyamath29) <br />
[Emily Ney](https://github.com/EmilyNey) <br />

## What is This Package?
The Fortune Cookie package is a python package that will bring some joy to your day to day coding! You can can use this package to get a random fortune or find your lucky numbers. 

## PyPI Package Link
[View our package on PyPI here] (https://pypi.org)

## Installation and Running
# Installation
`pip3 install fortunecookiepkg`

# Running



## Testing
How to run unit tests
Simple example unit tests are included within the tests directory. To run these tests...

<ol>
    <li>Install pytest in a virtual environment.</li>
    <li>Run the tests from the main project directory: `python3 -m pytest`.</li>
</ol>

## Want to Contribute?
### Setting up the Virtual Environment

### Building

### Testing

## Package Contents

### Functions

#### get_random_function()
Generates a random fortune <br />
**Parameters:** <br />
- _none_ <br />
**Return:** <br />
- a Fortune in the form of a str

#### get_lucky_numbers(len)
Generates a set of lucky numbers. <br />
**Parameters:** <br />
- len (int) \- the amount of lucky numbers to return <br />
**Return:** <br />
- list (int)s

#### get_daily_fortune(day)
Generates the same fortune for all users for that day. <br />
**Parameters:** <br />
- day (str) \- the weekday to retrieve a fortune for <br />
**Return:** <br />
- fortune (str)

#### get_custom_fortune(name)
Generates a fortune that mentions your name.
**Parameters:** 
- name (str) \- the name to include in the fortune <br />
**Return:** <br />
- fortune (str)

#### get_themed_fortune(theme)
Genrates a fortune that relates to the selected theme. <br />
**Parameters:** 
- theme (str) \- the theme to retrieve a fortune for <br />
**Return:** <br />
- fortune (str)