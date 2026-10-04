# Topic 1 — Getting Started

## What pandas is

pandas is a Python library for working with tables of data using code.

| Term | Meaning |
|---|---|
| Row | One record (one person, one product) |
| Column | One kind of information, for every row |
| DataFrame | The whole table |
| Series | A single column |
| NaN | An empty (missing) cell |

```python
import pandas as pd        # standard import; always use the nickname pd
pd.__version__             # check the installed version
```

Install once per environment with `%pip install pandas` (no comment on the same line), then restart the kernel.

## CSV files

- CSV (Comma-Separated Values) is a table stored as plain text.
- The first line is the header: the column names. It is not a row.
- Every other line is one row; commas separate the columns.
- Number of columns = number of commas in a line + 1.

## Reading a CSV

```python
df = pd.read_csv("students.csv")                                               # file next to the notebook
survey = pd.read_csv("../data/raw/stackoverflow_2019/survey_results_public.csv")  # file in another folder
```

- `read_csv` loads the file into memory as a DataFrame; all further work happens on the DataFrame.
- The DataFrame is a snapshot. Editing the file later does not change it; run `read_csv` again.
- Restarting the kernel or reopening the notebook clears memory; re-run the `read_csv` cells first.
- Changes to a DataFrame do not change the file on disk (saving comes later with `to_csv`).

## Paths

| Symbol | Meaning |
|---|---|
| `..` | go up one folder |
| `/` | go into a folder |

- A relative path starts from the folder the notebook is in.
- FileNotFoundError means the path is wrong or the file is not there.
- Datasets stay out of git: list their folders in `.gitignore` and put the download link in the README.

## The schema file

- Survey columns have short names; the schema file explains each one.
- The schema has one row per survey column, so its row count equals the survey's column count.

## First look at a new dataset

| Code | What it gives |
|---|---|
| `df.shape` | (rows, columns) |
| `df.info()` | each column's name, non-null count and dtype |
| `df.head(n)` | first n rows (default 5) |
| `df.tail(n)` | last n rows (default 5) |
| `df.describe()` | summary statistics for every number column |

- Non-null count lower than the number of rows means the column has missing values.
- Common dtypes: `int64` = whole numbers, `float64` = decimals, `object` = text.
- Rows are counted from 0, so the last row's label is (rows - 1).
- `head` and `tail` keep the original row labels.

## describe() rows

| Row | Meaning |
|---|---|
| count | how many values are filled in |
| mean | average |
| std | how spread out the values are |
| min / max | smallest / largest value |
| 25% / 50% / 75% | values a quarter, half and three quarters of the way up the sorted data |

- 50% is the median (middle value); unlike the mean, it is not pulled by a few extreme values.
- Text columns are skipped. A column that looks numeric but contains any text is treated as text.

## Display options

```python
pd.set_option("display.max_columns", None)    # show every column
pd.set_option("display.max_rows", 85)         # show up to 85 rows before hiding the middle
pd.set_option("display.max_colwidth", None)   # show full text in every cell
pd.reset_option("display.max_rows")           # put one setting back to its default
```

- Settings change only what is shown, never the data.
- They start with `pd.`, so they apply to every table in the notebook.
- The value is a limit; a table bigger than the limit is still cut with "...".
- They last until the kernel restarts; keep them in a cell right after the import.

## Showing output in a notebook

| Code | Last line | Middle line |
|---|---|---|
| `df`, `df.shape`, `df.head()` | shown | hidden, wrap in `print()` |
| `df.info()` | shown | shown, never needs `print()` |

- Jupyter shows only the value of the last line in a cell.
- `info()` prints its own report; wrapping it in `print()` adds an extra `None`.
- Wide tables look better as the last line without `print()`.

## Remember

- Load first with `read_csv`, then work on the DataFrame.
- Run `shape`, `info()`, `head()` and `describe()` on every new dataset.
- Facts (attributes) have no brackets: `shape`. Actions (methods) have brackets: `head()`, `info()`.
- Things starting with `pd.` act on pandas as a whole; things starting with a table name act on that table only.
- Read errors from the bottom up: the last line names the problem.

## Watch out

- File names and setting names are text and need quotes; without them you get NameError.
- `df.shape()` fails with "'tuple' object is not callable"; `df.head` without brackets shows a "bound method" message.
- A space after a column name in the header becomes part of the name.
- `set_option` changes a setting; `reset_option` undoes it. Don't mix them up.
- Never set `max_rows` to None for a large table; use `head()` and `tail()` instead.
- `describe()` does not say which row a min or max came from; check the table.