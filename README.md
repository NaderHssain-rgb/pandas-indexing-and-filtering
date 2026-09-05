# Pandas Indexing and Filtering

Beginner Python practice using **Pandas** to understand DataFrame indexing, selecting values by position or label, and filtering data using conditions.

## 📌 Topics Covered

* Pandas DataFrame
* `iloc`
* `loc`
* `iat`
* `at`
* Position-based indexing
* Label-based indexing
* Boolean filtering
* Selecting rows
* Selecting columns
* Reading Excel files

## 🛠️ Technologies

* Python
* Pandas
* Excel
* OpenPyXL

## 📂 Project Structure

```text
pandas-indexing-and-filtering/
│
├── pandas_indexing_and_filtering.py
├── Employee.xlsx
├── requirements.txt
└── README.md
```

## 🚀 Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python pandas_indexing_and_filtering.py
```

## 📖 Indexing Methods

### `iloc`

`iloc` selects data using numerical positions.

```python
df.iloc[1, 0]
```

This selects the value from the second row and first column.

### `loc`

`loc` selects data using row and column labels.

```python
df.loc["Y", "A"]
```

This selects the value from index `"Y"` and column `"A"`.

### `iat`

`iat` is used to access a single value using numerical positions.

```python
df.iat[1, 0]
```

### `at`

`at` is used to access a single value using labels.

```python
df.at["Y", "A"]
```

## 🔍 `iloc` vs `loc`

| Method | Uses               | Example            |
| ------ | ------------------ | ------------------ |
| `iloc` | Numerical position | `df.iloc[1, 0]`    |
| `loc`  | Label              | `df.loc["Y", "A"]` |

## ⚡ `iat` vs `at`

| Method | Uses               | Example           |
| ------ | ------------------ | ----------------- |
| `iat`  | Numerical position | `df.iat[1, 0]`    |
| `at`   | Label              | `df.at["Y", "A"]` |

The main difference is that `iat` and `at` are designed for accessing a **single value**.

## 🔎 Boolean Filtering

Pandas allows us to filter rows using conditions.

Example:

```python
df["Salary"] > 7000
```

This produces Boolean values:

```text
True
False
True
```

To select the rows that satisfy the condition:

```python
df[df["Salary"] > 7000]
```

For example, to select employees with a salary greater than `10000`:

```python
df[df["Salary"] > 10000]
```

## 🧠 What I Learned

Through this project, I practiced:

* Accessing DataFrame values by position
* Accessing DataFrame values by label
* Using `iloc`
* Using `loc`
* Using `iat`
* Using `at`
* Filtering DataFrame rows
* Working with Excel data
* Understanding Boolean conditions in Pandas

## 🎯 Project Goal

The goal of this project is to build a strong foundation in Pandas indexing and data filtering before moving to more advanced data-analysis operations.

## 📚 Future Improvements

Possible next steps:

* Filtering with multiple conditions
* Using `&` and `|`
* Sorting DataFrames
* Updating values with `loc`
* Adding and deleting columns
* Handling missing values
* Grouping data with `groupby()`
* Working with larger datasets

## 👨‍💻 Author

Nader

## ⭐ Note

This repository is part of my Python and Data Science learning journey.
