# Analyzing Cryptographic Algorithms for Enhanced Security in Online Communications

Code used for the comparative analysis of cryptographic algorithms for enhanced security in online communications.

## Table of Contents

  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [License](#license)
  - [References](#references)

## Introduction

This code repo accompanies the paper of the same name. This work contains the code and scrips used to analyze the 
performance of various cryptographic algorithms for enhanced security in online communications. 

The algorithms analyzed are:

- RSA
- ECC
- ElGamal
- NTRUencrypt

It currently focuses on Python implementations of these algorithms. But other languages are planned to be added in the
future.

## Prerequisites

To run this code you should have Python 3.10 installed. 

### Python

The Python language is pre-installed on most operating systems. But you probably need to upgrade it to v3.10 in order
to run these functions and libraries.

You can download it from the [official Python website](https://www.python.org/downloads/).

### Poetry

Poetry is a package manager for Python. It is used to install the required dependencies for this project.

This is the tool used for the development of this project. It is not required to run the code, but it is recommended for
managing the dependencies and optionally the virtual environment. It just makes life easier. We also exported a 
`requirements.txt` which can be used with `pip` to install the dependencies, or they can be installed manually.

### Dependencies

Significant effort was taken to minimize the dependencies required for this project. However we did leverage the 
`pycryptodome` library for the RSA, ECC, and ElGamal algorithms. This is a very popular library for cryptography in 
Python. NTRUencrypt uses several standalone libraries like `numpy`, `sympy`, and `docopt`.

If you want to manually install dependencies to avoid using Poetry, just install these dependencies:

1. `pycryptodome`
2. `numpy` (NTRUencrypt only)
3. `sympy` (NTRUencrypt only)
4. `docopt` (NTRUencrypt only)

## Usage

Using this library is easy. It runs via the command line using the python command. You can optionally pass in options as
you go. 

Full details about each tool is available within each directory.

To get started, clone this repo to your computer. Navigate in the terminal to this project and then run each file 
locally.

### Benchmark Tasks

Part of this project is to time and get technical benchmarks for each algorithm. This is done using the linux `time` 
command.

Each algorithm is broken into 3 parts:

1. Key Generation
2. Encryption
3. Decryption

Each of these parts is timed and the results are saved to a file. The results are also printed to the terminal.

Within each folder, you will find a file for each of these parts. We ran each of these file individually and saved the
results to a file.

