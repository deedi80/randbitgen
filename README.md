# 🧮 10,000-Bit Pseudo-Random Sequence Generator

## 📘 Project Overview

This repository contains a simple Python utility designed to generate a
sequence of **10,000 pseudo-random binary digits (0s and 1s)** and save
them to a formatted text file.

The primary purpose is to provide a **customizable and statistically
sound source of pseudo-random binary data** for testing, simulation, or
data analysis tasks.

## WebAPP Preview
https://randbitgen.vercel.app

------------------------------------------------------------------------

## 🚀 Getting Started

### 🔧 Prerequisites

You only need **Python 3** installed on your system to run this script.

### ▶️ Running the Generator

Clone the repository (if you haven't already):

``` bash
git clone https://github.com/deedi80/randbitgen
cd randbitgen
```

Execute the Python script in your terminal:

``` bash
python randbitgen.py
```

When the script finishes, you will find the generated output in a new
file named **random_bits.txt** in the same directory.

------------------------------------------------------------------------

## 📁 Output File: `rand_bits.txt`

The script is configured to produce **10,000 bits** and format the
output for readability:

  Feature             Value
  ------------------- --------
  **Total Bits**      10,000
  **Bits Per Line**   100
  **Total Lines**     100

This formatting ensures that the sequence is easy to inspect and process
line-by-line.

------------------------------------------------------------------------

## ⚙️ Configuration

You can easily modify the generation parameters by editing the constant
variables at the top of the **`randbitgen.py`** file:

``` python
# Here is the config
BIT_COUNT = 10000
BITS_PER_LINE = 100 
OUTPUT_FILENAME = "rand_bits.txt"
```

-   **BIT_COUNT:** Change the total length of the desired sequence.\
-   **BITS_PER_LINE:** Adjust the line wrapping for the output file.\
    *(Note: BIT_COUNT should be cleanly divisible by BITS_PER_LINE).*

------------------------------------------------------------------------

## 💻 Technology

The script uses Python's built-in **`random`** module, which relies on
the **Mersenne Twister algorithm** for fast and high-quality
pseudo-random number generation (suitable for non-cryptographic use).
