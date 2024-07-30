# XML to JSON Consolidation Tool

The XML to JSON Consolidation Tool is a utility designed to parse XML files containing image data, convert them into JSON format, and split the data into training and test datasets. This tool features a user-friendly graphical user interface (GUI) built with Tkinter to facilitate user interaction.

## Description

This tool helps in consolidating image annotation data stored in XML format into JSON format, which is more convenient for training machine learning models. The XML files are parsed to extract image and bounding box information, which is then split into training and test datasets based on user-defined percentages. The consolidated data is saved as JSON files for easy access and further processing.

## Features

- Parse XML files to extract image and bounding box data.
- Convert the extracted data into JSON format.
- Split the data into training and test datasets based on user-defined percentages.
- User-friendly GUI built with Tkinter.
- Default values for input and output paths and data split percentages.

## Installation

### Prerequisites

Ensure you have Python installed (version 3.6 or higher).

### Installing Dependencies

Install the required libraries using the following command:

```sh
pip install -r requirements.txt
