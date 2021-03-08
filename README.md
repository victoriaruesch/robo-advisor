# Robo-Advisor

Command-line application that allows users to specify a stock in order to get relevant data, a buy recommendation based on user preferences, and stock price data visualization. 

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/victoriaruesch/robo-advisor) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd robo-advisor
```

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env":

```sh
conda create -n stocks-env python=3.8
conda activate stocks-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

This application issues requests to the AlphaVantage Stock Market API in order to provide stock data and recommendations. Take a moment to [obtain an AlphaVantage API Key](https://www.alphavantage.co/).

After obtaining an API key, in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your API Key. 

     ALPHAVANTAGE_API_KEY="abc123"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [.gitignore](/.gitignore) file)

## Usage

Run the robo-advisor script:

```py
python app/robo_advisor.py
```
