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
# Topic 2 — Series and DataFrames

## The example table

`students.csv`, used in every example below:

| | name | city | marks |
|---|---|---|---|
| 0 | Asha | Indore | 82 |
| 1 | Vivek | Pune | 91 |
| 2 | Ravi | Delhi | 67 |
| 3 | Meena | Indore | 75 |

```python
import pandas as pd
df = pd.read_csv("students.csv")     # df is used in all examples below
```

- The top row (name, city, marks) holds the column names: `df.columns`.
- The numbers on the left (0, 1, 2, 3) are the row labels, called the index. They are not a data column.
- Every row has two identities: a label (what is printed on the left) and a position (its place in line, counting from 0). Labels and positions start equal but can differ later (see loc).

## Lists and dictionaries

| Type | Example | Found by |
|---|---|---|
| list | `[82, 91, 67]` | position, starting at 0 |
| dictionary | `{"name": "Asha", "marks": 82}` | key |

- `marks[0]` is the first item; `marks[-1]` is the last.
- A slice `marks[0:2]` includes position 0 and excludes position 2.
- A missing dictionary key gives KeyError.
- pandas reuses all of these ideas.

## Building a DataFrame from a dictionary

```python
data = {"name": ["Asha", "Vivek"],     # key = column name, list = values of that column
        "marks": [82, 91]}             # every list must have the same length
small = pd.DataFrame(data)             # capital D and F
```

- Each key becomes a column name; each list becomes that column's values.
- Item 0 of every list forms row 0, item 1 forms row 1, and so on.
- Row labels 0, 1, 2 ... are added automatically.
- Column order follows the order of the keys.
- Lists of different lengths give `ValueError: All arrays must be of the same length`.
- A DataFrame can be built from code like this without any file; useful for small test tables.

## Series

- A Series is one column of a table: values with a label for each value.
- It is one-dimensional; a DataFrame is two-dimensional.

```python
s = pd.Series([82, 91, 67], name="marks")   # name= must be written out
print(s.shape)                              # (3,)  one number, not (3, 1)
print(type(s))                              # <class 'pandas.core.series.Series'>
```

| Printed part | Meaning |
|---|---|
| left numbers | the index (labels) |
| right numbers | the values |
| `Name: marks` | the Series name (the column heading it had) |
| `dtype: int64` | data type of the values |

| | Series | DataFrame |
|---|---|---|
| Looks like | one column | a table |
| Shape example | `(4,)` | `(4, 3)` |
| Heading row | no, only a name at the bottom | yes |

- `pd.Series([82, 91], "marks")` does not set the name; the second plain argument is the index.
- `type(x)` tells you whether you hold a Series or a DataFrame; use it whenever unsure.
- A list containing `None` becomes decimals (float64), because the missing value is NaN.

## Selecting one column

```python
df["marks"]          # the marks column -> a Series
df.marks             # dot shortcut, same result for this name
df["marks"].head(2)  # chaining: select a column, then call a method on it
df["marks"].max()    # 91
```

| Style | Works when |
|---|---|
| `df["marks"]` | always |
| `df.marks` | name has no space and is not a method name |

- The result is a Series, so Series methods can follow straight away.
- A name with a space (`"Job Satisfaction"`) cannot use the dot form.
- A name like `count` or `size` clashes with the method of the same name in the dot form.
- A wrong name gives `KeyError: 'Marks'`. The name must match exactly: capitals, spaces, spelling.
- Make the bracket form the habit; the dot form is only a shortcut.

## Selecting many columns

```python
df[["name", "marks"]]    # inner [] = the list of names, outer [] = the selection
df[["marks"]]            # a list holding one name -> still a DataFrame
df["marks"]              # no inner list -> a Series
```

| Code | Result |
|---|---|
| `df["marks"]` | Series |
| `df[["marks"]]` | DataFrame (one column) |
| `df[["name", "marks"]]` | DataFrame (two columns) |

- One name is one request; several names need a list of names, so the list brackets go inside the selection brackets.
- The order inside the list sets the order of the columns in the result.
- The result is a new object; `df` is not changed.
- `df["name", "marks"]` gives `KeyError: ('name', 'marks')`, because pandas looks for one column with that pair as its name.

## The columns attribute

```python
df.columns              # Index(['name', 'city', 'marks'], dtype='object')
list(df.columns)        # ['name', 'city', 'marks']
len(df.columns)         # 3
"name" in df.columns    # True
"Name" in df.columns    # False, capitals matter
```

| Code | Gives |
|---|---|
| `df.columns` | the names as an Index |
| `list(df.columns)` | a normal list, easier to read |
| `len(df.columns)` | the number of columns (same as the second number of `shape`) |
| `"name" in df.columns` | True or False: does this exact name exist? |

- `columns` is an attribute (a fact), so no round brackets: `df.columns()` gives TypeError.
- When a KeyError appears, print `list(df.columns)` first.
- Usual causes: a capital letter, an extra space in the name, a spelling slip.

## iloc: select by position

```python
df.iloc[0]        # first row, as a Series
df.iloc[-1]       # last row
df.iloc[[0, 2]]   # rows at positions 0 and 2 (a list inside the brackets)
df.iloc[0:2]      # positions 0 and 1; the stop is excluded
df.iloc[2, 1]     # row position 2, column position 1 -> Delhi
```

| Code | Gives |
|---|---|
| `iloc[0]` | Asha's row (Series) |
| `iloc[-1]` | Meena's row |
| `iloc[[0, 2]]` | Asha and Ravi (DataFrame) |
| `iloc[0:2]` | Asha and Vivek (2 rows) |
| `iloc[2, 1]` | `Delhi` (a single cell) |

- iloc means integer location: it counts positions from 0 and ignores the labels.
- Always square brackets; `df.iloc(0)` is an error.
- A negative position counts from the end; -1 is the last row.
- A slice `a:b` includes position a and excludes position b, like a Python list.
- In `iloc[row, column]` both parts are numbers; column positions are name = 0, city = 1, marks = 2.
- A single number gives a Series (one row); a list or a slice gives a DataFrame.
- A position outside the table gives `IndexError: single positional indexer is out-of-bounds` (position 4 on 4 rows).

## loc: select by label

```python
df.loc[0, "name"]    # row label 0, column "name" -> Asha
df.loc[0:2]          # labels 0, 1 and 2; the stop is included -> 3 rows
df.loc[:, "city"]    # every row (the lone colon), only the city column
```

- loc selects by label: the index names on the left and the column names on top.
- The column part is a column name in quotes, never a number.
- A lone colon `:` means "all of them".
- The stop of a slice is included. This is the opposite of `iloc`, because labels are names and "up to name 2" includes 2.
- A label that does not exist gives KeyError.

### iloc and loc side by side

| | `iloc` | `loc` |
|---|---|---|
| Points by | position | label |
| Column part | a number | a name in quotes |
| Slice `0:2` gives | 2 rows (stop excluded) | 3 rows (stop included) |
| Missing row gives | IndexError | KeyError |

### When position and label differ

```python
t = df.tail(2)     # keeps Ravi and Meena with their original labels
t.iloc[0]          # position 0 -> Ravi
t.loc[2]           # label 2 -> Ravi
t.loc[0]           # KeyError: 0, there is no label 0 any more
```

| label | position | name |
|---|---|---|
| 2 | 0 | Ravi |
| 3 | 1 | Meena |

- `head()`, `tail()`, filtering and slicing keep the original labels; positions always restart from 0.
- So `loc[0]` can work on the full table and fail on a cut one.
- `df.loc[0, 1]` gives `KeyError: 1`; loc needs the column name, not a number. Use `df.iloc[0, 1]` for numbers.

### Which one to use

| Situation | Use |
|---|---|
| the first 5 rows, the last row, the 3rd row | `iloc` |
| the row with label 2, the row for order 1004 | `loc` |
| a cell by its column name | `loc` (or `df["col"]`) |
| unsure | print `df`; the numbers on the left are the labels |

## value_counts

```python
df["city"].value_counts()                         # count of each value, biggest first
df["city"].value_counts(normalize=True)           # shares from 0 to 1
df["city"].value_counts(normalize=True) * 100     # percentages
```

```
city
Indore    2
Pune      1
Delhi     1
Name: count, dtype: int64
```

- It counts how many times each distinct value appears in a column, like a tally chart.
- Call it on one column (a Series), never on the whole table.
- The result is a Series: the labels are the values, the numbers are the counts, sorted biggest first.
- For tied counts (Pune and Delhi above) do not rely on the order between them.
- `normalize=True` divides each count by the total (4), so Indore is 2/4 = 0.50. It gives decimals, not percentages; multiply by 100.

### Missing values

```python
r = pd.Series([4, None, None, None, 5, 4], name="rating")
r.value_counts()                 # NaN hidden: 4.0 -> 2, 5.0 -> 1
r.value_counts(dropna=False)     # NaN counted: NaN -> 3, 4.0 -> 2, 5.0 -> 1
```

- By default NaN is not counted; `dropna=False` includes it.
- NaN can be the top row, which shows the column has more empty cells than any single value. Without `dropna=False` this stays hidden.
- The numbers show as 4.0 and 5.0 because a column holding NaN is stored as decimals.

### Chaining

```python
df["city"].value_counts().head(1)       # only the top row
df["city"].value_counts().index[0]      # only the top name -> Indore
```

- The result is a Series, so `head()` and `.index` work on it.
- `.index` holds the labels of the result (the city names); `[0]` takes the first.
- The argument names a column, never a value inside it: `df.value_counts("Pune")` gives `KeyError: 'Pune'`.
- `df.value_counts()` with no column counts whole-row combinations; select the column first.

## Quick reference

| Goal | Code | Result |
|---|---|---|
| one column | `df["marks"]` | Series |
| many columns | `df[["name", "marks"]]` | DataFrame |
| one column kept as a table | `df[["marks"]]` | DataFrame |
| all column names | `list(df.columns)` | list |
| row by position | `df.iloc[0]` | Series |
| rows by position, range | `df.iloc[0:2]` | DataFrame (2 rows) |
| one cell by position | `df.iloc[2, 1]` | value |
| row by label | `df.loc[2]` | Series |
| rows by label, range | `df.loc[0:2]` | DataFrame (3 rows) |
| one cell by label | `df.loc[2, "city"]` | value |
| tally of a column | `df["city"].value_counts()` | Series |

## Remember

- A DataFrame is the whole table; a Series is one column.
- Every row has a label (printed on the left) and a position (counted from 0); they can differ.
- One pair of brackets gives a Series; a list inside the brackets gives a DataFrame.
- Facts (attributes) have no brackets: `columns`. Actions (methods) have brackets: `head()`, `value_counts()`.
- `iloc` = position, stop excluded. `loc` = label, stop included.
- After `head`, `tail` or any cut, labels stay the same and positions restart from 0.
- When a KeyError appears, print `list(df.columns)` before anything else.
- Read errors from the bottom up: the last line names the problem.
- Only the last line of a cell is shown; wrap the other lines in `print()`.

## Watch out

- `pd.dataframe` and `pd.series` fail with AttributeError; the names are `DataFrame` and `Series`.
- Lists of different lengths in a dictionary give ValueError.
- `pd.Series([...], "marks")` does not set the name; write `name="marks"`.
- `df["Marks"]` gives KeyError; capitals and spaces must match exactly.
- `df["name", "marks"]` gives KeyError; use `df[["name", "marks"]]`.
- `df.Job Satisfaction` is a SyntaxError; use `df["Job Satisfaction"]`.
- `df.columns()` fails with "'Index' object is not callable"; no round brackets.
- `df.iloc[4]` on a 4-row table gives IndexError; positions go 0 to 3.
- `df.iloc(0)` is an error; use square brackets.
- `df.loc[0, 1]` gives KeyError; loc needs a column name.
- `df.loc[0]` after `tail(2)` gives KeyError; label 0 was cut.
- `df.value_counts("Pune")` gives KeyError; Pune is a value, not a column.
- `normalize=True` shows 0.50, not 50; multiply by 100.
- `value_counts()` without `dropna=False` hides missing values.


## dtypes: the type of each column

```python
df.dtypes             # type of every column (a Series)
df["marks"].dtype     # type of one column
```

| dtype | Holds | Example |
|---|---|---|
| `int64` | whole numbers | 82, 91 |
| `float64` | decimals | 4.5, 3.8 |
| `object` | text | "Asha", "Indore" |
| `bool` | True / False | True |

- A dtype is the kind of data a column holds; every column has exactly one.
- `dtypes` (with s) is for the table, `dtype` is for one column; both are attributes, so no round brackets.
- `info()` also shows each column's dtype.
- The dtype decides what you can do: `df["marks"] + 5` works, `df["city"] + 5` gives TypeError.
- One text cell in a number column (`five` in `shop["qty"]`) makes the whole column `object`.
- An empty cell is NaN, and NaN is a decimal, so a column with NaN is `float64` (4 shows as 4.0).
- An `int64` column that gains a NaN becomes `float64`.
- Changing a type (`astype`) comes later, in cleaning.

Watch out: `df.dtypes()` fails ("'Series' object is not callable"); `df.dtype` fails (AttributeError); a number-looking column with `object` dtype usually has a stray text cell, so check `dtypes` before calculating.

