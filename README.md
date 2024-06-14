# Stock HashTable Management System

## Description

This program provides a simple yet effective system for managing stock information using a hash table. It allows users to store, search, delete stock data, and import price data from CSV files. Additionally, the program supports plotting the closing prices of stocks for the last 30 days in an ASCII chart and allows saving and loading the hash table to and from a file.

## Features

- **Hashing Methods:** Supports three different probing methods for the hash table: quadratic probing, linear probing, and double hashing.
- **CRUD Operations:** Allows adding, deleting, and searching for stocks in the hash table.
- **Importing Price Data:** Supports importing stock price data from CSV files.
- **Data Visualization:** Displays the closing prices of a stock for the last 30 days in an ASCII chart.
- **Persistence:** Enables saving the hash table to a file and loading it from a file.

## Instructions

### Requirements

- Python 3.4 or higher
- Libraries: `csv`, `pickle`, `collections.namedtuple`, `asciichart`

### Usage
1. Start the program.
2. Choose a hashing method from the provided options.
3. Use the following commands for various operations:
   - ADD: Adds a new stock.
   - DEL: Deletes an existing stock.
   - IMPORT: Imports price data for a stock from a CSV file.
   - SEARCH: Searches for a stock and displays the latest price data, if available.
   - PLOT: Displays the closing prices of the last 30 days for a stock in ASCII format.
   - SAVE <filename>: Saves the current hash table to a file.
   - LOAD <filename>: Loads a hash table from a file.
   - QUIT: Exits the program.
