# Time Series

> Author:
> - D11202805 - Ian Joseph Chandra
> - M11002818 - Wilfrid Azariah

The result of this project can be seen in this [LSTM.ipynb file](./Forecasting/LSTM.ipynb).

<!-- TOC -->

* [Time Series](#time-series)
* [1. Getting Started](#1-getting-started)
    * [1.1 Navigate to Your Project Directory](#11-navigate-to-your-project-directory)
    * [Result History:](#result-history)
        * [2024-05-10](#2024-05-10)
        * [2024-04-19](#2024-04-19)

<!-- TOC -->

# 1. Getting Started

Follow these steps to create a virtual environment (venv) and install Python dependencies from an `env.txt` file of this
project.

1. Navigate to Your Project Directory:
    ```bash
    cd path/to/your/project
    ```
2. Create a `venv` Virtual Environment
    ```bash
    python -m venv venv
    ```
3. Activate the Virtual Environment:
    - Windows:
        ```bash
        venv\Scripts\activate
        ```
    - macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
4. Install Python Dependencies from the `env.txt` File:
    ```bash
    pip install -r env.txt
    ```
5. Verify Python dependencies installation:
    ```bash
    pip list
    ```

## Result History:

### 2024-05-10

- LSTM:

  Predicted Price Index for the next 5 business days (excluding weekends):
    - 2024-05-10 : 15983.237
    - 2024-05-13 : 15967.462
    - 2024-05-14 : 15918.418
    - 2024-05-15 : 15858.854
    - 2024-05-16 : 15800.044

### 2024-04-19

- LSTM:

  Predicted Price Index for the next 5 business days (excluding weekends):
    * 2024-04-26 : 15320.334
    * 2024-04-29 : 15385.153
    * 2024-04-30 : 15406.4375
    * 2024-05-01 : 15404.063
    * 2024-05-02 : 15390.907