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


# Topic 3 — Indexes

## What the index is

The index is the set of row labels printed on the left of a table. It is not a data column.

```python
import pandas as pd
students = pd.read_csv("students.csv")     # name, city, marks (4 rows)
students.index                             # RangeIndex(start=0, stop=4, step=1)
list(students.index)                       # [0, 1, 2, 3]
```

- `df.index` is an attribute (a fact), so no round brackets.
- `RangeIndex` is the default: the numbers 0, 1, 2 ... added automatically.
- The index is not counted in `shape` or `columns`: `(4, 3)` means 4 rows and 3 data columns.
- Labels are names for rows; positions are the place in line. `iloc` uses positions, `loc` uses labels (Topic 2).

## set_index: choose a column as the labels

```python
by_name = students.set_index("name")    # the name column becomes the row labels
by_name
```

| name | city | marks |
|---|---|---|
| Asha | Indore | 82 |
| Vivek | Pune | 91 |
| Ravi | Delhi | 67 |
| Meena | Indore | 75 |

- It returns a new table; `students` itself is unchanged (save the result in a variable).
- The column leaves `columns` and becomes the index: `by_name.shape` is `(4, 2)`.
- The index gets a name, `by_name.index.name` is `'name'`, shown above the labels.
- Use a column whose values identify rows (an id, a name) so a row can be looked up by that value.

## loc with a custom index

```python
by_name.loc["Vivek"]              # the whole row for Vivek (Series)
by_name.loc["Vivek", "marks"]     # one cell -> 91
by_name.loc["Asha":"Ravi"]        # labels from Asha to Ravi, stop included (3 rows)
by_name.iloc[0]                   # position still works -> Asha's row
```

- Once the labels are words, `loc` takes the words: `loc["Vivek"]`, not `loc[1]`.
- `loc[1]` now gives `KeyError: 1`, because no label is the number 1.
- Position still works with `iloc`; labels and positions are two separate systems.
- A slice on labels follows the table order and includes the stop.
- A label that does not exist gives KeyError (`by_name.loc["Rahul"]`).

## reset_index: put the labels back

```python
restored = by_name.reset_index()               # name goes back to being a column
renumbered = students.tail(2).reset_index(drop=True)   # labels 0, 1 again
by_name.reset_index(drop=True)                 # labels gone, names LOST
```

| Code | Index becomes | Old index |
|---|---|---|
| `reset_index()` | 0, 1, 2 ... | returns as a column |
| `reset_index(drop=True)` | 0, 1, 2 ... | thrown away |

- `reset_index()` is the reverse of `set_index`.
- After `tail(2)` the labels are 2 and 3; `reset_index(drop=True)` renumbers them 0 and 1.
- Use `drop=True` only when the old labels are plain numbers you do not need.
- With `drop=True` on `by_name`, the names are not kept anywhere.
- It also returns a new table; save it.

## sort_index: order by the labels

```python
by_name.sort_index()                    # labels A to Z
by_name.sort_index(ascending=False)     # labels Z to A
```

- It sorts by the labels, not by a column (sorting by column values comes in Topic 7).
- Numbers sort smallest first, words alphabetically (capitals before small letters).
- It returns a new table; `ascending=False` reverses the order.
- Sorting changes the row order only; each row keeps its own label.

## Duplicate labels and index.name

The index is not forced to be unique.

```python
orders = pd.read_csv("orders.csv")
c = orders.set_index("city")
c.loc["Indore"]               # several rows -> DataFrame (3 rows)
c.loc["Mumbai"]               # one row -> Series
c.loc["Indore", "amount"]     # Series of 3 values
c.index.is_unique             # False
o = orders.set_index("order_id")
o.index.is_unique             # True
o.index.name = "id"           # the index name can be changed
```

| Lookup | Result |
|---|---|
| label appears once | Series (one row) |
| label appears many times | DataFrame (all matching rows) |
| label missing | KeyError |

- `loc` returns every row with that label, so the result type depends on the data.
- `index.is_unique` answers True or False; check it before relying on a label to mean one row.
- An index is like a primary key in a database, with one difference: pandas does not enforce uniqueness.
- A good key column (order_id) is unique; a repeating column (city) is a poor key.
- `index.name` is only a heading for the index; assign it directly (no brackets, an equals sign).

## Quick reference

| Goal | Code |
|---|---|
| see the labels | `df.index` |
| a column becomes the labels | `df.set_index("name")` |
| row by label | `df.loc["Vivek"]` |
| labels back to a column | `df.reset_index()` |
| fresh 0, 1, 2 labels, old ones dropped | `df.reset_index(drop=True)` |
| order by labels | `df.sort_index()` |
| reverse order | `df.sort_index(ascending=False)` |
| are labels unique? | `df.index.is_unique` |
| rename the index | `df.index.name = "id"` |

## Remember

- The index is the row labels; it is not a data column and is not counted in `shape`.
- `set_index` moves a column into the labels; `reset_index` moves it back.
- Every one of these returns a new table; the original does not change unless you save over it.
- After `set_index`, use `loc` with the words and `iloc` with the positions.
- `reset_index(drop=True)` renumbers from 0 after head, tail or cuts.
- A label can repeat; one match gives a Series, many matches give a DataFrame.
- Check `df.index.is_unique` before using a column as a key.

## Watch out

- `df.index()` fails; `index` is an attribute, no round brackets.
- `set_index("name")` without saving does nothing lasting; write `by_name = ...`.
- `by_name["name"]` gives KeyError; the column is now the index, not a column.
- `by_name.loc[1]` gives KeyError; use the label (`"Vivek"`) or `iloc[1]`.
- `reset_index(drop=True)` on a table whose labels matter loses them for good.
- `reset_index()` without `drop=True` adds an `index` column when the old labels were plain numbers.
- `c.loc["Indore"]` on repeated labels returns a DataFrame, so code expecting a single row breaks.
- `sort_index()` sorts by labels; it does not sort a column such as marks.

# Topic 4 — Filtering

Filtering means keeping only the rows that pass a test. Two tables are used below: `students.csv` and `orders.csv`.

| name | city | marks |
|---|---|---|
| Asha | Indore | 82 |
| Vivek | Pune | 91 |
| Ravi | Delhi | 67 |
| Meena | Indore | 75 |

`orders.csv` has the columns `order_id`, `customer`, `city`, `amount`, `items` (8 rows). Order 1002 has an empty `amount` and order 1004 has an empty `items`.

```python
import pandas as pd
students = pd.read_csv("students.csv")
orders = pd.read_csv("orders.csv")
```

## The mask

```python
mask = students["marks"] > 80     # True / False for every row
students[mask]                    # keeps the rows where the mask is True -> Asha, Vivek
students[students["marks"] > 80]  # same thing in one line
```

| marks | > 80 |
|---|---|
| 82 | True |
| 91 | True |
| 67 | False |
| 75 | False |

- A comparison on a column checks every row and gives a Series of True/False, called a mask.
- The mask has one value per row, in the same order and with the same labels.
- `df[mask]` keeps only the rows where the mask is True.
- Comparison signs: `>`, `<`, `>=`, `<=`, `==` (equal), `!=` (not equal).
- Filtering gives a new table; the original is unchanged.
- Labels are kept (Vivek stays row 1); use `reset_index(drop=True)` for a fresh 0, 1, 2.
- A single `=` assigns, `==` compares.
- Comparing a text column with a number (`marks` stored as `object`) gives `TypeError: '>' not supported between instances of 'str' and 'int'`; check `df.dtypes` first.

## Several conditions: `&`, `|`, `~`

```python
in_indore = students["city"] == "Indore"
high = students["marks"] > 80

students[in_indore & high]     # AND: both True -> Asha
students[in_indore | high]     # OR: at least one True -> Asha, Vivek, Meena
students[~in_indore]           # NOT: flips True/False -> Vivek, Ravi

students[(students["city"] == "Indore") & (students["marks"] > 80)]   # one line
```

| Sign | Meaning | Row stays when |
|---|---|---|
| `&` | and | both True |
| `\|` | or | at least one True |
| `~` | not | the mask is False |

- Each condition goes in its own round brackets inside one line. Without brackets `&` runs before `>` and the result is wrong or an error.
- Wrong: `(df["a"]) > 1`. The bracket must hold the whole test: `(df["a"] > 1)`.
- Python's words `and`, `or`, `not` do not work on masks (`ValueError: The truth value of a Series is ambiguous`).
- A text comparison needs quotes and `==`; capitals must match exactly.
- Named masks (`in_indore`, `high`) keep long filters readable.

## isin and between

```python
students[students["city"].isin(["Pune", "Delhi"])]    # city is on the list -> Vivek, Ravi
students[~students["city"].isin(["Pune", "Delhi"])]   # not on the list -> Asha, Meena
students[students["marks"].between(75, 82)]           # 75 <= marks <= 82 -> Asha, Meena
```

- `isin([a, b, c])` is True where the value is any item in the list; the list is in square brackets.
- It replaces a long chain of `==` joined with `|`.
- `isin("Pune")` with a plain string fails (TypeError); use `isin(["Pune"])`.
- `between(low, high)` includes both ends. It equals `(col >= low) & (col <= high)`.

## Missing values: isna and notna

```python
orders["amount"].isna()          # True where the amount is empty (NaN)
orders[orders["amount"].isna()]  # only order 1002
orders["amount"].notna()         # opposite of isna
orders["amount"].isna().sum()    # how many are missing -> 1
orders.isna().sum()              # missing count for every column
```

- `isna()` is True for empty cells; `notna()` is True where a value is held. `notna()` equals `~isna()`.
- `isna().sum()` counts the True values (True counts as 1).
- `isnull()` and `notnull()` are other names for the same tools.
- A comparison with NaN is always False: `NaN > 1000`, `NaN == 5` and `NaN < 5` are all False.
- So `orders[~(orders["amount"] > 1000)]` also keeps order 1002 (amount empty), because `~False` is True.
- To avoid it, add `notna()` to the same filter: `orders[orders["amount"].notna() & (orders["amount"] <= 1000)]`.
- `df["col"] == None` and `df["col"] == np.nan` do not find empty cells; use `isna()`.

## Text filters: the .str tools

```python
names = orders["customer"]
names.str.startswith("A")            # Asha, Arjun
names.str.endswith("a")              # Asha, Meena, Zoya, Neha
names.str.contains("ee")             # Meena
names.str.contains("a", case=False)  # ignore capitals
names.str.len() == 4                 # 4-letter names
orders["city"].str.lower() == "pune" # lower-case first, then compare
```

| Tool | True when |
|---|---|
| `str.startswith("A")` | text begins with A |
| `str.endswith("a")` | text ends with a |
| `str.contains("ee")` | "ee" appears anywhere |
| `str.len()` | (gives a number) length of the text |
| `str.lower()`, `str.upper()` | (gives text) changes the capitals |

- Text tools sit behind `.str` and work on one column, not on the whole table.
- Capitals matter: `contains("a")` does not find "Arjun"; add `case=False`.
- `str.contains` reads its text as a pattern (regex); add `regex=False` for symbols such as `.` or `+`.
- On a column holding NaN the result has NaN too and the filter fails with ValueError; add `na=False`.
- `.str` on a number column gives `AttributeError: Can only use .str accessor with string values`.

## query: a shorter filter

```python
orders.query("amount > 1000")                          # 1001, 1004, 1007
orders.query('city == "Indore" and amount > 1000')     # 1001, 1004
orders.query('city in ["Pune", "Delhi"]')              # 1002, 1003, 1006, 1007
orders.query('not (city == "Indore")')

limit = 500
orders.query("amount > @limit")                        # @ uses a normal variable

orders.query("amount.isna()")                          # empty amounts
orders.query('customer.str.startswith("A")')           # text tools work too
```

- `query` takes the condition as one text string; column names are written plainly.
- Use the words `and`, `or`, `not` inside it; `&` is also accepted. No extra brackets are needed.
- A text value needs quotes inside the string; use single quotes outside and double inside.
- `@name` uses a Python variable; a column name with a space needs backticks.
- A wrong or wrongly capitalized column gives `UndefinedVariableError: name 'Amount' is not defined`; a column of another table gives the same error.
- The result equals the mask way (`a.equals(b)` is True).
- Use `query` for short readable filters; the mask way is more flexible.

## loc with a mask: rows and columns together

```python
big = orders["amount"] > 1000

orders.loc[big, "customer"]                      # Series: Asha, Meena, Arjun
orders.loc[big, ["customer", "amount"]]          # DataFrame, 2 columns
orders.loc[big, "customer":"amount"]             # column range by name, stop included
orders.loc[orders["city"] == "Indore", "amount"].sum()    # total Indore amount -> 3950.0
orders.loc[big].shape                            # (3, 5): all columns kept
orders.loc[big, ["customer"]].shape              # (3, 1): list of one name stays a table
```

- `df.loc[rows, columns]` takes a row mask and the columns you want, in one step.
- One column name gives a Series (shape `(3,)`); a list of names gives a DataFrame.
- A mask alone, `df.loc[mask]`, keeps every column.
- Both ends of a column range by name are included, in table order.
- Labels are kept after filtering (0, 3, 6).
- For reading, `df[mask]["col"]` and `df.loc[mask, "col"]` give the same values; for changing values (Topic 5) you must use `loc`.
- Each condition inside the mask needs its own brackets: `(orders["city"] == "Indore") & (orders["amount"] > 1000)`.

## Quick reference

| Goal | Code |
|---|---|
| rows where marks above 80 | `df[df["marks"] > 80]` |
| both conditions | `df[(a_test) & (b_test)]` |
| either condition | `df[(a_test) \| (b_test)]` |
| the opposite | `df[~mask]` |
| value on a list | `df[df["city"].isin(["Pune", "Delhi"])]` |
| value in a range | `df[df["marks"].between(75, 82)]` |
| empty cells | `df[df["amount"].isna()]` |
| filled cells | `df[df["amount"].notna()]` |
| count of empty cells per column | `df.isna().sum()` |
| name starts with / ends with / contains | `df["name"].str.startswith("A")` etc. |
| short form | `df.query('city == "Indore" and marks > 80')` |
| chosen rows and columns | `df.loc[mask, ["name", "marks"]]` |

## Remember

- A comparison gives a mask (True/False per row); `df[mask]` keeps the True rows.
- Join masks with `&`, `|`, `~`, each condition in its own brackets; never `and`, `or`, `not` on a mask.
- A comparison with NaN is always False; add `notna()` when empty cells must not slip in.
- `isin` for a list of values, `between` for a range with both ends included.
- Text tools need `.str`; capitals matter unless `case=False`.
- In `query` the words `and`, `or`, `not` work, and `@` brings in a variable.
- `loc[mask, columns]` picks rows and columns together and is the form used for changing values.
- Filtering keeps the original labels.
- Check `df.dtypes` before comparing a column with a number.

## Watch out

- `df[df["marks"] > 80 & df["city"] == "Indore"]` is wrong; each test needs brackets.
- `(df["amount"]) > 1000` inside a bigger test gives a wrong result; the bracket must hold the whole comparison.
- `df[df["marks"] = 80]` is a SyntaxError; use `==` to compare.
- `df[mask1 and mask2]` gives ValueError: The truth value of a Series is ambiguous.
- `~(df["amount"] > 1000)` keeps the rows where the amount is empty.
- `df["col"] == np.nan` finds nothing; use `isna()`.
- `df["city"].isin("Pune")` is a TypeError; use a list.
- `df["name"].str.contains("a")` misses "Arjun"; add `case=False`.
- `df.query("Amount > 1000")` or a column from another table gives UndefinedVariableError.
- `df.loc[mask, "customer":"amount"]` includes both end columns.
- A TypeError with `str` and `int` in a comparison means the column is text (`object`); check `df.dtypes`.


# Topic 5 — Updating, apply and strings

This topic changes the table. The examples use `students.csv`, `orders.csv` and `shop.csv`.

| name | city | marks |
|---|---|---|
| Asha | Indore | 82 |
| Vivek | Pune | 91 |
| Ravi | Delhi | 67 |
| Meena | Indore | 75 |

```python
import pandas as pd
students = pd.read_csv("students.csv")
orders = pd.read_csv("orders.csv")      # order_id, customer, city, amount, items (8 rows)
shop = pd.read_csv("shop.csv")          # item, category, price, qty, rating (6 rows)
```

## Changing values with loc

```python
df = students.copy()                                    # a separate copy, students stays untouched

df.loc[2, "marks"] = 70                                 # row label 2, column marks -> Ravi becomes 70
df.loc[df["city"] == "Indore", "city"] = "Indore City"  # a mask changes every matching row at once
df.loc[df["marks"] >= 80, "grade"] = "A"                # a new column is created; other rows get NaN
```

| Part | Meaning |
|---|---|
| `df.loc[` row `,` column `] = value` | write a value at that place |
| row | a label or a mask |
| column | a column name in quotes (a new name creates a new column) |

- Writing changes the table in place; it does not return a new table.
- `df = students` is only a second name for the same table, so a change through `df` also changes `students`. Use `.copy()`.
- Writing needs `loc` with row and column together. `df[mask]["marks"] = 0` often changes nothing, because `df[mask]` is a temporary copy.
- Rows not matched by the mask get NaN in a newly created column.
- A single `=` writes, `==` compares.

## Column arithmetic and new columns

```python
df["marks"] + 5                                    # a new Series, df unchanged
df["bonus"] = df["marks"] + 5                      # saved as a new column
df["name_city"] = df["name"] + " - " + df["city"]  # text + text joins them row by row
df["country"] = "India"                            # one value goes into every row
orders["per_item"] = orders["amount"] / orders["items"]   # column / column, row by row
shop["sale_price"] = shop["price"] * 0.9
orders["amount"].sum()                             # one number from a column -> 8740.0
```

| Sign | Meaning |
|---|---|
| `+` `-` `*` `/` | add, subtract, multiply, divide |
| `//` | division without the remainder |
| `%` | remainder |
| `**` | power |

- A calculation on a column applies to every row at once.
- Two columns of the same table work row by row.
- `df["new"] = ...` makes a new column; an existing name is overwritten.
- A calculation involving NaN gives NaN in that row (`per_item` for orders 1002 and 1004).
- `sum()`, `mean()`, `max()`, `min()` on a column skip the empty cells.
- Text plus a number gives `TypeError: can only concatenate str (not "int") to str`.

## rename and replace

```python
r = df.rename(columns={"name": "student", "marks": "score"})   # old name : new name
df.rename(columns=str.upper)                  # a tool applied to every name -> NAME, CITY, MARKS
df.rename(columns={"Name": "x"})              # wrong capital: nothing changes, no error
df.columns = ["n", "c", "m"]                  # replace all names at once

df["city"].replace("Indore", "Indore City")                  # one value in one column
df["city"].replace({"Indore": "IDR", "Pune": "PNQ"})         # several at once
df.replace({"city": {"Delhi": "New Delhi"}})                 # on the whole table: {column: {old: new}}
shop["qty"] = shop["qty"].replace("five", 5)                 # fix the stray text cell
```

- `rename` and `replace` return new objects; save the result with `=` to keep the change.
- A wrong old name in `rename` is ignored silently; check with `list(df.columns)`.
- `str.upper` is written without brackets: `rename` runs the tool itself on each name.
- `df.columns = [...]` needs exactly one name per column, or ValueError.
- `replace` matches the whole cell, not a part of the text.
- After `replace("five", 5)` the column is still `object`, because the other cells are text; `astype` (cleaning topic) turns it into numbers.

## map

```python
state_of = {"Indore": "MP", "Pune": "MH", "Delhi": "DL"}   # city -> state
df["state"] = df["city"].map(state_of)
df["city"].map({"Indore": "MP"})              # MP, NaN, NaN, MP  (unmatched become NaN)
df["city"].replace({"Indore": "MP"})          # MP, Pune, Delhi, MP  (unmatched are kept)
df["name"].map(str.upper)                     # a function also works
df["city"].map({"Indore": "MP", "Pune": "MH"}).fillna("unknown")
```

| | `map` | `replace` |
|---|---|---|
| Unmatched values | become NaN | stay as they are |
| Best for | turning every value into another kind (city to state) | fixing a few values |

- `map` works on one column (a Series), not on the whole table.
- Capitals and spaces must match exactly: `"indore"` does not find `"Indore"`.
- `fillna("word")` fills the NaN boxes left by missing keys.

## apply

```python
def grade(m):                                     # takes one mark, returns one grade
    if m >= 80:
        return "A"
    elif m >= 70:
        return "B"
    else:
        return "C"

df["grade"] = df["marks"].apply(grade)            # no brackets after grade
df["marks"].apply(lambda m: m + 5)                # a one-line rule with no name
df["intro"] = df.apply(lambda row: row["name"] + " from " + row["city"], axis=1)   # a rule on each ROW
```

- `df["col"].apply(function)` runs the function on every value and returns a new Series.
- `def` makes your own rule; `return` is what comes back for each value.
- `lambda x: x + 5` is a one-line function with no name.
- `df.apply(function, axis=1)` gives the function a whole row; read values with `row["col"]`.
- NaN is passed into the function too. `NaN > 1000` is False, so the empty amount of order 1002 lands in the else branch (`small`). Repair those rows with a `loc` mask afterwards.
- Use column arithmetic where possible (faster); use `apply` when the rule needs if/else or several steps.
- `map(dictionary)` is for lookups, `apply(function)` is for rules.
- `apply(grade())` with brackets fails: `grade() missing 1 required positional argument`.

## String cleaning with .str

```python
raw = pd.DataFrame({"name": ["  asha SHARMA ", "VIVEK  singh", "Ravi-Kumar", "meena patel"]})
c = raw.copy()
c["name"] = c["name"].str.strip()                          # spaces at the start and end go
c["name"] = c["name"].str.title()                          # Asha Sharma
c["name"] = c["name"].str.replace("-", " ", regex=False)   # dash to space, as plain text
c["name"] = c["name"].str.replace("  ", " ", regex=False)  # two spaces to one

parts = c["name"].str.split(" ", expand=True)              # pieces in separate columns 0, 1
c["first"] = parts[0]
emails = pd.Series(["asha@gmail.com", "vivek@yahoo.com"])
domain = emails.str.split("@").str[1]                      # cut at @, take piece number 1 -> gmail.com, yahoo.com
c["first"].str[:3]                                         # the first 3 letters
```

| Tool | Gives |
|---|---|
| `str.strip()` | no spaces at the start and end (`lstrip`, `rstrip` for one side) |
| `str.lower()`, `str.upper()`, `str.title()` | changed capitals |
| `str.replace(old, new, regex=False)` | part of each text changed |
| `str.split(sep)` | a list per row |
| `str.split(sep, expand=True)` | the pieces in separate columns |
| `.str[1]`, `.str[:3]` | piece number 1 of a list, or the first 3 letters of a text |

- Text tools need `.str`; `df["name"].strip()` fails with AttributeError.
- `strip()` removes spaces only at the ends, not in the middle.
- `regex=False` treats the text as plain characters. With regex on, `.` matches every character and `+` or `(` can cause errors.
- Tools chain in order: `df["email"].str.strip().str.lower()`.
- Clean first, then compare or group: `" Pune"` and `"Pune"` are different values until stripped.
- A column holding NaN gives NaN for those rows; `.str` on a column of numbers gives AttributeError.

## Quick reference

| Goal | Code |
|---|---|
| change one cell | `df.loc[2, "marks"] = 70` |
| change many rows | `df.loc[mask, "col"] = value` |
| keep the original safe | `df = students.copy()` |
| new column from a calculation | `df["bonus"] = df["marks"] + 5` |
| rename columns | `df.rename(columns={"old": "new"})` |
| change values in a column | `df["col"].replace({"old": "new"})` |
| turn values through a lookup | `df["col"].map(dictionary)` |
| your own rule on a column | `df["col"].apply(function)` |
| your own rule on each row | `df.apply(function, axis=1)` |
| clean text | `df["col"].str.strip().str.lower()` |
| cut text | `df["col"].str.split(" ", expand=True)` |

## Remember

- Work on a copy (`.copy()`) before changing a table you need to keep.
- Writing into a table needs `loc[row, column] = value`.
- Column arithmetic works on every row at once; NaN stays NaN.
- `rename`, `replace`, `map`, `apply` and the `.str` tools all return new objects; save them with `=`.
- `map` turns unmatched values into NaN; `replace` keeps them.
- Pass a function to `apply` or `rename` without brackets.
- Comparisons with NaN are False, so empty cells fall into an else branch; repair them with a mask afterwards.
- Text tools need `.str`, and use `regex=False` for plain text.

## Watch out

- `df2 = df` is not a copy; changes to `df2` change `df`.
- `df[mask]["col"] = value` may change nothing; use `df.loc[mask, "col"] = value`.
- Text plus a number gives TypeError.
- `df.rename(columns={"Name": "x"})` does nothing when the column is `name`, and shows no error.
- `df.columns = ["a", "b"]` with the wrong number of names gives ValueError.
- `replace` and `rename` do not change the table unless the result is saved.
- `map` with a missing key gives NaN.
- `apply(grade())` with brackets is an error; write `apply(grade)`.
- `df.apply(f)` without `axis=1` runs on columns, so `row["name"]` raises KeyError.
- `df["name"].strip()` without `.str` fails.
- `str.replace(".", "-")` with regex on replaces every character.
- After `replace("five", 5)` the column is still `object`.


# Topic 6 — Adding and removing: drop, add a row, concat, insert

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
students = pd.read_csv("students.csv")
df = students.copy()                 # work on a copy so the original stays safe
```

## Removing columns and rows: drop

```python
df.drop(columns=["city"])            # remove one column
df.drop(columns=["city", "marks"])   # remove several columns
df.drop(index=[1, 3])                # remove rows by LABEL (Vivek and Meena)
df.drop(index=1)                     # one label does not need a list
df.drop(index=[1, 3]).reset_index(drop=True)   # remove, then renumber 0, 1
```

| Goal | Code |
|---|---|
| remove columns | `df.drop(columns=[...])` |
| remove rows by label | `df.drop(index=[...])` |
| remove rows by a rule | `df.drop(df[df["marks"] < 80].index)` |

- `drop` returns a new table; `df` is not changed. Save the result.
- Always write `columns=` or `index=`. `df.drop("city")` looks for a row label called city and gives `KeyError: "['city'] not found in axis"`.
- A wrong name gives KeyError. `errors="ignore"` skips names that do not exist.
- Labels are kept after dropping rows, so use `reset_index(drop=True)` for a fresh 0, 1, 2.
- Dropping by a rule gives the same result as a filter. `df[df["marks"] >= 80]` is usually shorter.

### del and pop

```python
del c["city"]            # remove a column in place; returns nothing
m = d.pop("marks")       # remove a column in place AND get it back as a Series
```

| | `del df["col"]` | `m = df.pop("col")` |
|---|---|---|
| Removes the column from `df` | yes | yes |
| Gives the column back | no | yes, a Series |
| Use when | the values are not needed | the values are still needed |

- Both change the table itself, so `.copy()` first if the original must be safe.
- Use `drop(columns=...)` when you want a new table and the original untouched.

## Adding a row

```python
df.loc[4] = ["Kiran", "Pune", 88]         # label 4 is new -> a row is added at the bottom
df.loc[len(df)] = ["Kiran", "Pune", 88]   # len(df) is the next free label
df.loc[1] = ["Zed", "Goa", 50]            # label 1 EXISTS -> Vivek's row is replaced
```

- `loc[new_label] = [values]` works in place and returns nothing.
- The list needs one value per column, in column order. Otherwise `ValueError: cannot set a row with mismatched columns`.
- An existing label is overwritten without any warning.
- `df.append(...)` no longer exists in pandas 2; use `concat`.
- Adding rows one by one in a loop is slow. Collect the rows in a list, build one table, then `concat` once.

## concat top to bottom

```python
a = pd.DataFrame({"name": ["Asha", "Vivek"], "city": ["Indore", "Pune"], "marks": [82, 91]})
b = pd.DataFrame({"name": ["Ravi", "Meena"], "city": ["Delhi", "Indore"], "marks": [67, 75]})

pd.concat([a, b])                         # stack b under a; labels 0 1 0 1 (repeated)
pd.concat([a, b], ignore_index=True)      # labels 0 1 2 3
pd.concat([a, c], join="inner", ignore_index=True)   # keep only the shared columns
pd.concat([a, b], keys=["sec_A", "sec_B"])           # remember which table each row came from
```

| Situation | Result |
|---|---|
| same columns | rows stack cleanly |
| a column in only one table | the other rows get NaN |
| a column order that differs | still correct, columns are matched by name |
| `join="inner"` | only the shared columns are kept |

- The tables go inside one list: `pd.concat([a, b])`. `pd.concat(a, b)` gives `TypeError`.
- Without `ignore_index=True` the labels repeat.
- A column with NaN becomes `float64` (20 shows as 20.0).
- `keys=` adds an outer label; `.loc["sec_B"]` pulls that table back out.
- `concat` stacks rows. Matching rows by a shared column (an id) is `merge`, which comes later.

## concat side by side

```python
pd.concat([n, c], axis=1)                 # axis=1 -> side by side (axis=0 is top to bottom)
pd.concat([n, s], axis=1)                 # a Series can be glued too; its name becomes the column name
pd.concat([n, z], axis=1, join="inner")   # keep only labels found in both tables
```

- Rows are matched by LABEL, not by position.
- A label found in only one table gives NaN in the other table's columns.
- Danger: if the labels do not describe the same rows (after shuffling or filtering), the data is mixed up silently. Run `reset_index(drop=True)` on the tables first when they are in the same order but have different labels.
- For a single new column from a list, `df["new"] = [values]` is simpler. The length must equal the row count.

## Adding a column at a chosen place, and reordering

```python
df["grade"] = ["A", "A", "B", "B"]                       # new column at the far right
df.insert(1, "roll", [101, 102, 103, 104])               # insert(position, name, values)
df[["marks", "name", "city"]]                            # reorder: select in the order you want
df[["city"] + [c for c in df.columns if c != "city"]]    # move one column to the front
```

- `insert` works in place and returns nothing, so `df = df.insert(...)` would set `df` to None.
- Position 0 is the front. A position above the column count gives `IndexError: loc must be an integer between -3 and 3`.
- An existing name gives `ValueError: cannot insert roll, already exists`.
- The values can be a list, one single value (repeated for every row), or a calculated column.
- Reordering changes only the display order; the data and labels stay the same.

## Quick reference

| Goal | Code |
|---|---|
| remove columns | `df.drop(columns=["a", "b"])` |
| remove rows by label | `df.drop(index=[1, 3])` |
| remove a column in place | `del df["a"]` |
| remove a column and keep it | `m = df.pop("a")` |
| add a row (in place) | `df.loc[len(df)] = [...]` |
| stack tables | `pd.concat([a, b], ignore_index=True)` |
| glue tables side by side | `pd.concat([a, b], axis=1)` |
| add a column at the end | `df["new"] = [...]` |
| add a column at a position | `df.insert(1, "new", [...])` |
| reorder columns | `df[["c", "a", "b"]]` |

## Remember

- `drop`, `concat` and column selection return a new table; save the result.
- `loc[...] = row`, `insert`, `del` and `pop` change the table itself; use `.copy()` first when the original matters.
- Always write `columns=` or `index=` in `drop`.
- `concat` takes a list of tables. `axis=0` stacks, `axis=1` glues.
- `concat` matches columns by name when stacking and rows by label when gluing.
- Use `ignore_index=True` after stacking, and `reset_index(drop=True)` before gluing tables whose labels differ.
- When a KeyError appears, print `list(df.columns)` first.

## Watch out

- `df.drop("city")` gives KeyError; write `df.drop(columns=["city"])`.
- Forgetting to save the result of `drop` or `concat` changes nothing.
- `df.loc[1] = [...]` on an existing label overwrites that row.
- A row list with too few or too many values gives ValueError.
- `pd.concat(a, b)` gives TypeError; write `pd.concat([a, b])`.
- Missing columns in `concat` give NaN, and an int column with NaN becomes float.
- Gluing side by side with different labels gives NaN or wrongly matched rows.
- `df = df.insert(...)` sets `df` to None.
- `insert` with an existing name gives ValueError; a too-large position gives IndexError.
- Only the last line of a cell is shown; wrap the other lines in `print()`.


# Topic 6A — get_dummies: turning text columns into 0/1 columns

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
df = pd.read_csv("students.csv")
```

## Why it is needed

- A model can only do maths on numbers, and a column like `city` holds words.
- Numbering the cities (Delhi=1, Indore=2, Pune=3) is avoided, because it tells the model that the cities have an order and a size (Pune is three times Indore).
- `get_dummies` makes one column per distinct value, with 1 where the row has that value and 0 elsewhere. This is called one-hot encoding.

## The basic call

```python
pd.get_dummies(df["city"])                  # one column per city; True/False in new pandas
pd.get_dummies(df["city"], dtype=int)       # 0 and 1 instead of False/True
pd.get_dummies(df["city"], prefix="city", dtype=int)   # names become city_Delhi, city_Indore, city_Pune
```

```
   Delhi  Indore  Pune
0      0       1     0
1      0       0     1
2      1       0     0
3      0       1     0
```

- New columns are in alphabetical order of the values.
- Every row has exactly one 1: `d.sum(axis=1)` is 1 for every row.
- The sum of a column is the number of rows with that value: `d.sum()` gives Delhi 1, Indore 2, Pune 1.
- It returns a new table; `df` is not changed. Save the result.

## Encoding inside the whole table

```python
pd.get_dummies(df, columns=["city"], dtype=int)
```

```
    name  marks  city_Delhi  city_Indore  city_Pune
0   Asha     82           0            1          0
1  Vivek     91           0            0          1
2   Ravi     67           1            0          0
3  Meena     75           0            1          0
```

- `columns=["city"]` names the column to encode. The other columns are kept as they are.
- The old `city` column is replaced by its boxes, with `city_` added in front automatically.
- Always give `columns=`. Without it pandas encodes every text column, so `name` turns into `name_Asha`, `name_Meena`, ... (8 columns instead of 5).
- Number columns such as `marks` are never encoded.
- The manual equivalent: `pd.concat([df.drop(columns=["city"]), pd.get_dummies(df["city"], prefix="city", dtype=int)], axis=1)`.

## drop_first

```python
pd.get_dummies(df, columns=["city"], drop_first=True, dtype=int)
```

- It removes the first box (Delhi). If all remaining boxes are 0, the row belongs to the dropped value (Ravi), so no information is lost.
- It is useful for linear models, where the full set of boxes always adds up to 1 and duplicates the information.

## Missing values

```python
pd.get_dummies(df["city"], dtype=int)                  # a missing city gets 0 in every box
pd.get_dummies(df["city"], dummy_na=True, dtype=int)   # an extra box for "missing"
```

## The train / test trap

`get_dummies` makes boxes only for the values it sees in that table. A second table with fewer cities gets fewer columns, so the two tables no longer line up.

```python
tr = pd.get_dummies(train, columns=["city"], dtype=int)    # city_Delhi, city_Indore, city_Pune
te = pd.get_dummies(test, columns=["city"], dtype=int)     # city_Indore, city_Pune  (no Delhi in test)
list(tr.columns) == list(te.columns)                       # False

fixed = te.reindex(columns=tr.columns, fill_value=0)       # exactly the train columns; missing boxes become 0
```

| Fix | How | Note |
|---|---|---|
| 1 | `te.reindex(columns=tr.columns, fill_value=0)` | train stays the single source of truth |
| 2 | `pd.concat([train, test], ignore_index=True)`, then one `get_dummies`, then split with `iloc` | simple, but test values leak into the encoding |

- A value that is new in test (Goa) has no box in the fixed table, so its row is all 0. The model never saw it.
- Check `list(train_encoded.columns) == list(test_encoded.columns)` before giving data to a model.
- scikit-learn's `OneHotEncoder` handles this automatically, which is the reason it exists.

## Quick reference

| Goal | Code |
|---|---|
| boxes for one column | `pd.get_dummies(df["city"], dtype=int)` |
| names with a prefix | `pd.get_dummies(df["city"], prefix="city", dtype=int)` |
| encode inside the table | `pd.get_dummies(df, columns=["city"], dtype=int)` |
| drop one box per column | `drop_first=True` |
| a box for missing values | `dummy_na=True` |
| match test to train | `te.reindex(columns=tr.columns, fill_value=0)` |

## Remember

- One value, one box; each row has exactly one 1.
- Give `columns=[...]` so only the intended column is encoded.
- Use `dtype=int` to get 0/1.
- `get_dummies` returns a new table; save the result.
- Test data must end with exactly the train columns, in the same order.

## Watch out

- `pd.get_dummies(df)` without `columns=` also encodes `name`, giving one box per person.
- Forgetting to save the result changes nothing in `df`.
- Without `dtype=int` the boxes show as True/False in new pandas.
- Encoding train and test separately gives different columns when a value is missing from one of them.
- A new value in test becomes an all-0 row after `reindex`.
- With `drop_first=True`, remember which value was dropped; it is the first one alphabetically.
- Only the last line of a cell is shown; wrap the other lines in `print()`.


# Topic 7 — Sorting: sort_values, nlargest, sort_index, rank

## The example tables

`students` (used for most examples):

| | name | city | marks |
|---|---|---|---|
| 0 | Asha | Indore | 82 |
| 1 | Vivek | Pune | 91 |
| 2 | Ravi | Delhi | 67 |
| 3 | Meena | Indore | 75 |

`exam` has ties (Vivek and Kiran both 91, Asha and Meena both 82, Ravi and Dev both 67), and `shop` has missing ratings:

```python
import pandas as pd
df = pd.read_csv("students.csv")

exam = pd.DataFrame({"name": ["Asha", "Vivek", "Ravi", "Meena", "Kiran", "Dev"],
                     "city": ["Indore", "Pune", "Delhi", "Indore", "Pune", "Delhi"],
                     "marks": [82, 91, 67, 82, 91, 67]})

shop = pd.DataFrame({"item": ["pen", "doll", "novel", "rice", "ball"],
                     "price": [10, 250, 400, 60, 120],
                     "rating": [4.5, None, 3.8, None, 4.2]})
```

## sort_values: one column

```python
df.sort_values("marks")                              # low to high (the default)
df.sort_values("marks", ascending=False)             # high to low
df.sort_values("marks", ascending=False, ignore_index=True)   # and renumber the labels 0, 1, 2 ...
df.sort_values("name")["name"].tolist()              # text sorts A to Z -> ['Asha', 'Meena', 'Ravi', 'Vivek']
df["marks"].sort_values(ascending=False).head(2)     # sorting one column (a Series): the top two marks
```

- It re-stacks the same rows in a new order. Each row keeps its own label, so after sorting the labels are out of order (2, 3, 0, 1).
- It returns a new table; `df` keeps its old order. Save the result.
- For fresh labels use `reset_index(drop=True)` or `ignore_index=True`.
- After sorting, position and label differ: `iloc[0]` is the first row of the new order, `loc[0]` is the row with label 0.
- Capital letters come before small letters in a text sort.
- A wrong column name gives `KeyError: 'Marks'`.
- The chain `df.sort_values("name")["name"].tolist()` sorts the table, selects the column, then turns it into a plain list.

## Sorting by several columns

```python
exam.sort_values(["marks", "name"], ascending=[False, True])
```

```
    name    city  marks
4  Kiran    Pune     91
1  Vivek    Pune     91
0   Asha  Indore     82
3  Meena  Indore     82
5    Dev   Delhi     67
2   Ravi   Delhi     67
```

- The columns go inside one list. The first column is the main rule; the next one only settles ties in the first.
- `ascending=[False, True]` gives one direction per column, in the same order. A list of the wrong length gives `ValueError: Length of ascending (1) != length of by (2)`.
- A single `ascending=False` applies to every column.
- The order in the list matters: `["city", "marks"]` and `["marks", "city"]` give different tables.
- Ties that no column settles can come out in any order, so keep adding columns until the order is fixed.
- Top N by a rule: `exam.sort_values(["marks", "name"], ascending=[False, True]).head(3)`.

## Missing values in a sort

```python
shop.sort_values("rating")                                   # NaN rows go to the END
shop.sort_values("rating", ascending=False)                  # NaN rows are STILL at the end
shop.sort_values("rating", na_position="first")              # NaN rows on top
shop.dropna(subset=["rating"]).sort_values("rating", ascending=False)   # leave the NaN rows out
```

- `sort_values` always puts NaN at the end, in both directions.
- `na_position="first"` moves them to the top.
- `dropna(subset=[...])` removes the rows with a missing value in the named column.

## nlargest and nsmallest

```python
shop.nlargest(2, "price")        # the 2 rows with the biggest price, biggest first
shop.nsmallest(2, "price")       # the 2 rows with the smallest price, smallest first
shop["price"].nlargest(2)        # on a single column: just the values with their labels
shop.nlargest(3, ["rating", "price"])   # a list of columns also works
```

- `df.nlargest(2, "price")` gives the same rows as `df.sort_values("price", ascending=False).head(2)`, and it is shorter.
- NaN rows are never picked as largest or smallest.
- For ties at the edge, `keep="first"` (default) keeps the earlier row, and `keep="all"` keeps every tied row.

## sort_index

```python
a = df.set_index("name")
a.sort_index()                       # rows sorted by their LABELS: Asha, Meena, Ravi, Vivek
a.sort_index(ascending=False)        # Z to A
df.sort_values("marks").sort_index() # back to the original 0, 1, 2, 3 order
df.sort_index(axis=1)                # sort the column names instead
```

- `sort_values` sorts by what is inside the table; `sort_index` sorts by the row labels on the left.
- `sort_index()` undoes any `sort_values` as long as the labels are the original ones.

## rank

```python
df["marks"].rank(ascending=False).tolist()         # [2.0, 1.0, 4.0, 3.0]
df["rank"] = df["marks"].rank(ascending=False).astype(int)
df.sort_values("rank")                             # the rank list
```

- A rank is a place number: 1st, 2nd, 3rd. `rank` gives each row its number and moves no rows.
- By default the smallest value gets rank 1. Use `ascending=False` so the highest value gets rank 1.
- It returns decimals, so use `.astype(int)` when there are no ties and no missing values.
- To see the rank list, add the numbers as a column and then use `sort_values("rank")`.

### Ties (only needed when values repeat)

| method | the two 91s, then the 82s | idea |
|---|---|---|
| `average` (default) | 1.5, 1.5, then 3.5, 3.5 | the average of the positions they share |
| `min` | 1, 1, then 3, 3 | the best shared position (race style) |
| `dense` | 1, 1, then 2, 2 | no gap after a tie |
| `first` | 1, 2, then 3, 4 | the table order breaks the tie |

## Quick reference

| Goal | Code |
|---|---|
| sort by one column | `df.sort_values("marks")` |
| high to low | `df.sort_values("marks", ascending=False)` |
| several columns | `df.sort_values(["a", "b"], ascending=[False, True])` |
| fresh labels | `ignore_index=True` or `.reset_index(drop=True)` |
| missing values first | `na_position="first"` |
| top n rows | `df.nlargest(n, "col")` |
| bottom n rows | `df.nsmallest(n, "col")` |
| sort by labels | `df.sort_index()` |
| place numbers | `df["col"].rank(ascending=False)` |

## Remember

- `sort_values` and `sort_index` return a new table; save the result.
- Labels travel with their rows when you sort.
- The first column in a list of columns is the main rule.
- NaN goes to the end of a sort unless `na_position="first"`.
- `nlargest(n, "col")` is the short form of sort high to low plus `head(n)`.
- `rank` numbers the rows and moves nothing; `ascending=False` makes the highest value rank 1.

## Watch out

- `df.sort_values("Marks")` gives KeyError; check `list(df.columns)`.
- `ascending=[False]` for two columns gives ValueError; one direction per column.
- `df.sort_values("marks", "name")` fails; the columns go inside one list.
- A forgotten save leaves `df` in the old order.
- After sorting, `loc[0]` and `iloc[0]` are different rows.
- `rank` without `ascending=False` gives the smallest value rank 1.
- A rank column of decimals (2.0) needs `.astype(int)`.
- Only the last line of a cell is shown; wrap the other lines in `print()`.

# Topic 8 — groupby: sum, agg, transform

## The example table

```python
import pandas as pd

orders = pd.DataFrame({"order_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
                       "customer": ["asha", "ravi", "zoya", "meena", "asha", "zoya", "ravi", "kiran"],
                       "city": ["Indore", "Delhi", "Pune", "Indore", "Indore", "Pune", "Delhi", "Pune"],
                       "category": ["Food", "Toys", "Books", "Food", "Books", "Food", "Toys", "Toys"],
                       "amount": [1200, 800, 1500, 950, 400, 300, 600, 1100]})
```

## The idea

`groupby("city")` sorts the rows into one pile per city. Nothing is calculated until you choose a column and a method.

```python
orders.groupby("city")["amount"].sum()
#       ^ pile by     ^ which number  ^ what to do with each pile
```

| city | pile (amounts) | sum | mean | max | size |
|---|---|---|---|---|---|
| Delhi | 800, 600 | 1400 | 700.0 | 800 | 2 |
| Indore | 1200, 950, 400 | 2550 | 850.0 | 1200 | 3 |
| Pune | 1500, 300, 1100 | 2900 | 966.7 | 1500 | 3 |

## One number per group

```python
orders.groupby("city")["amount"].sum()      # Delhi 1400, Indore 2550, Pune 2900
orders.groupby("city")["amount"].mean()
orders.groupby("city")["amount"].max()
orders.groupby("city").size()               # rows per group (needs no column)
orders.groupby("city")["amount"].count()    # non-empty values per group
```

- The result is a Series. The group names are its labels, sorted by name.
- `.reset_index()` (or `groupby("city", as_index=False)`) turns the labels back into a normal column.
- `idxmax()` gives the label of the biggest value: `orders.groupby("city")["amount"].sum().idxmax()` is `'Pune'`.
- `count` skips empty values; `size` counts rows.
- `orders.groupby("city").mean()` without choosing a column fails on text columns.
- The original table is unchanged, and the group totals add up to the grand total.

## Several numbers at once: agg

```python
r = orders.groupby("city").agg(
    total   = ("amount", "sum"),          # new_name = ("column", "method")
    biggest = ("amount", "max"),
    bills   = ("order_id", "count"),
    buyers  = ("customer", "nunique"),    # different customers, each counted once
)
```

```
        total  biggest  bills  buyers
city
Delhi    1400      800      2       1
Indore   2550     1200      3       2
Pune     2900     1500      3       2
```

- You choose the new column names.
- The result is a normal table with the group names as labels: `r.reset_index()`, `r.sort_values("total", ascending=False)`, `r.loc["Pune", "total"]`, `r["total"].idxmax()` all work.
- Older ways you may see: a list `["sum", "mean", "max"]` (columns named after the methods) and a dict `{"amount": "sum", "order_id": "count"}` (column names stay as they were).
- Use `agg` only when you want two or more numbers or your own names. For one number use `.sum()`.

## Two group columns

```python
orders.groupby(["city", "category"])["amount"].sum()
orders.groupby(["city", "category"], as_index=False).agg(total=("amount", "sum"), bills=("order_id", "count"))
```

- Put the columns inside one list.
- The result has two labels; use `.reset_index()` or `as_index=False`.

## Keep only some groups

```python
# original rows of cities whose total is above 2000
orders.groupby("city").filter(lambda g: g["amount"].sum() > 2000)

# the same in two steps
t = orders.groupby("city")["amount"].sum()
big = t[t > 2000].index
orders[orders["city"].isin(big)]
```

## Top rows in each group

```python
s = orders.sort_values("amount", ascending=False)   # sort first
s.groupby("city").head(1)                           # biggest bill of each city
s.groupby("city").head(2)                           # top 2 of each city
orders.loc[orders.groupby("city")["amount"].idxmax()]   # biggest row of each city
```

- Sort first, then `head(n)`. Without sorting, `head` only takes the first rows in table order.

## transform: the group's number on every row

```python
orders.groupby("city")["amount"].transform("sum")   # 8 values, same order as orders

o = orders.copy()
o["city_total"] = o.groupby("city")["amount"].transform("sum")
o["city_avg"]   = o.groupby("city")["amount"].transform("mean").round(1)
o[o["amount"] > o["city_avg"]]                      # bills above their own city's average
```

| | result length | use it when |
|---|---|---|
| `.sum()`, `.agg(...)` | one row per group | you want a summary table |
| `.transform("sum")` | one value per original row | you want the group number beside every row |

## Share, rank and fill inside groups

```python
# share of the city's total
o["share_pct"] = (o["amount"] / o["city_total"] * 100).round(1)

# rank inside each city (biggest = 1, restarts in every city)
o["rank_in_city"] = o.groupby("city")["amount"].rank(ascending=False).astype(int)
o[o["rank_in_city"] <= 2]                           # top 2 per city

# fill empty values with the group's average
m["filled"] = m["amount"].fillna(m.groupby("city")["amount"].transform("mean"))
```

- Empty values (NaN) are skipped when the group mean is worked out.

## Quick reference

| Goal | Code |
|---|---|
| one number per group | `df.groupby("g")["x"].sum()` |
| rows per group | `df.groupby("g").size()` |
| group names as a column | `.reset_index()` or `as_index=False` |
| many numbers | `df.groupby("g").agg(new=("x", "sum"), ...)` |
| two group columns | `df.groupby(["a", "b"])["x"].sum()` |
| keep some groups | `df.groupby("g").filter(lambda g: g["x"].sum() > n)` |
| top n per group | `df.sort_values("x", ascending=False).groupby("g").head(n)` |
| group number on every row | `df.groupby("g")["x"].transform("sum")` |
| rank inside group | `df.groupby("g")["x"].rank(ascending=False)` |
| fill by group | `df["x"].fillna(df.groupby("g")["x"].transform("mean"))` |

## Remember

- `groupby` makes piles; you must choose a column and a method.
- The result of `sum()`, `mean()`, `agg(...)` has one row per group, with the group names as labels.
- `agg(new_name=("column", "method"))` is the clearest way to get several numbers.
- `transform` keeps the length of the original table, so it fits into a new column.
- Sort first, then `groupby(...).head(n)` for the top rows per group.
- Group total, share, rank and fill are all `groupby` + `transform`.

## Watch out

- `groupby("a", "b")` is wrong; use a list `["a", "b"]`.
- `df.groupby("g").mean()` fails when text columns are present; choose the number column.
- A wrong column name gives KeyError (check capitals), also inside `agg`.
- `agg(total="amount")` gives TypeError; it needs `("amount", "sum")`.
- `df["new"] = df.groupby("g")["x"].sum()` gives NaN everywhere, with no error; use `transform("sum")`.
- `rank` or `mean` without `groupby` works over the whole table, with no error.
- `head(n)` without sorting first is not "top n".
- `size` counts rows; `count` skips empty values.
- Only the last line of a cell is shown; wrap the other lines in `print()`.


# Topic 9 — Cleaning and missing values: isna, dropna, fillna, astype, duplicates

## The example tables

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({"name":   ["Asha", "Ravi", "Meena", "Kiran", "Dev", "Zoya"],
                   "city":   ["Indore", None, "Pune", "Delhi", None, "Pune"],
                   "age":    [25, 31, None, 28, None, 40],
                   "salary": [50000, 62000, 45000, None, 58000, 71000]})

raw = pd.DataFrame({"item":  ["pen", "book", "bag", "ball"],
                    "price": ["100", "250", "abc", "80"],     # numbers stored as text, one bad entry
                    "qty":   [2, 5, 1, 3],
                    "size":  ["10", "20", "30", "40"]})

d = pd.DataFrame({"order_id": [1, 2, 3, 4, 5, 6],
                  "customer": ["asha", "ravi", "asha", "meena", "ravi", "asha"],
                  "item":     ["pen", "book", "pen", "bag", "book", "ball"],
                  "amount":   [100, 250, 100, 400, 250, 90]})
```

An empty box is `NaN` ("not a number"). A CSV's empty cell becomes `NaN`, and a number column that holds a `NaN` becomes decimals (25.0).

## Finding missing values

```python
df.isna()                       # True/False table, True = missing (isnull() is the same)
df.notna()                      # the opposite
df.isna().sum()                 # blanks per column (run this first on any new data)
df.isna().sum().sum()           # blanks in the whole table
(df.isna().mean() * 100).round(1)   # percent missing per column
df["age"].isna().sum()          # blanks in one column
df[df["age"].isna()]            # rows where age is missing
df[df["city"].notna()]          # rows where city is filled
df[df.isna().any(axis=1)]       # rows with at least one blank
df.info()                       # Non-Null Count lower than the row count = missing values
df["city"].value_counts(dropna=False)   # show NaN in the count (it is skipped by default)
```

- `any(axis=1)` asks, for each row, "is any box True?".
- `df["x"] == np.nan` is always False, with no error. Use `isna()`.
- `info()` prints by itself; do not wrap it in `print(...)`.

## Removing missing values: dropna

```python
df.dropna()                          # drop every row with ANY blank
df.dropna(subset=["city"])           # look only at these columns
df.dropna(subset=["age", "salary"])  # age OR salary blank -> row dropped
df.dropna(how="all")                 # drop a row only if ALL its boxes are blank
df.dropna(thresh=3)                  # keep rows with at least 3 filled boxes
df.dropna(axis=1)                    # drop COLUMNS that have a blank
df.dropna().reset_index(drop=True)   # renumber the labels afterwards
```

## Filling missing values: fillna

```python
d2 = df.copy()
d2["age"] = d2["age"].fillna(0)                          # a number
d2["city"] = d2["city"].fillna("Unknown")                # a text
d2["age"] = d2["age"].fillna(d2["age"].mean())           # mean
d2["salary"] = d2["salary"].fillna(d2["salary"].median())   # median
d2["city"] = d2["city"].fillna(df["city"].mode()[0])     # most common value (mode)

df.fillna({"city": "Unknown", "age": df["age"].median(), "salary": 0})   # several columns at once

# by group (Topic 8)
df["salary"].fillna(df.groupby("city")["salary"].transform("mean"))
```

- Mean and median skip the blanks when they calculate. The median is safer when a few values are very large or very small.
- `mode()` can return several values; `[0]` picks the first.

| Situation | Usually |
|---|---|
| a column is almost empty | drop the column |
| very few rows are blank | drop those rows with `subset=` |
| a number column with many blanks | fill with the median or mean |
| a text column | fill with `"Unknown"` or the mode |
| the target column of a model | drop those rows, do not invent the answer |

## Fixing types: astype and to_numeric

```python
raw.dtypes                                        # check the types first
raw["size"].sum()                                 # '10203040' -> text is glued together (no error)

r = raw.copy()
r["size"] = r["size"].astype(int)                 # text -> whole numbers
r["qty"] = r["qty"].astype(float)                 # whole -> decimals
r["qty"] = r["qty"].astype(str)                   # numbers -> text
pd.Series([3.7, 2.2]).astype(int)                 # [3, 2] -> decimals are cut off, not rounded

raw["price"].astype(int)                          # ValueError: 'abc' cannot become a number

r = raw.copy()
r["price"] = pd.to_numeric(r["price"], errors="coerce")   # bad entries -> NaN
r["price"].isna().sum()                                   # how many were bad
r["price"] = r["price"].fillna(r["price"].mean())         # fill them
r["price"] = r["price"].astype(int)                       # whole numbers again

# symbols inside the text: remove them first (.str from Topic 5)
m = pd.DataFrame({"cost": ["Rs 1,200", "Rs 850", "Rs 99"]})
m["cost"] = m["cost"].str.replace("Rs ", "").str.replace(",", "").astype(int)

pd.Series([1.0, 2.0, np.nan]).astype(int)         # IntCastingNaNError: a whole-number column cannot hold NaN
pd.Series([1.0, 2.0, np.nan]).astype("Int64")     # [1, 2, <NA>] -> the special type that allows blanks
```

- Recipe for a text column that should be numbers: `to_numeric(errors="coerce")`, count the NaN, fill or drop, then `astype(int)`.
- Type names: `int`, `float`, `str`, `bool`, `"category"`.

## Duplicates

```python
d.duplicated()                                          # all False: order_id makes every row different
d.duplicated(subset=["customer", "item"])               # True for rows that repeat an earlier one
d[d.duplicated(subset=["customer", "item"])]            # the repeated rows
d[d.duplicated(subset=["customer", "item"], keep=False)]   # the originals and their repeats
d.duplicated(subset=["customer", "item"]).sum()         # how many repeats

d.drop_duplicates(subset=["customer", "item"])                 # keep the first of each
d.drop_duplicates(subset=["customer", "item"], keep="last")    # keep the last of each
d.drop_duplicates(subset=["customer", "item"], keep=False)     # drop every row that has a repeat
d.drop_duplicates(subset=["customer", "item"], ignore_index=True)   # and renumber

d["customer"].nunique()      # number of different values
d["customer"].unique()       # the different values

# clean the text first, otherwise repeats stay hidden
s = pd.DataFrame({"name": ["Asha", "asha ", "ASHA"]})
s["name"] = s["name"].str.strip().str.lower()
s.duplicated().sum()         # 2
```

- By default `duplicated` compares ALL columns, so a unique id column hides every repeat. Give `subset` the columns that define a repeat.
- The first row of a group of repeats is `False`; the later ones are `True`.

## Quick reference

| Goal | Code |
|---|---|
| blanks per column | `df.isna().sum()` |
| rows with a blank in a column | `df[df["c"].isna()]` |
| drop rows with a blank | `df.dropna(subset=["c"])` |
| keep rows with enough filled boxes | `df.dropna(thresh=n)` |
| fill with a value | `df["c"].fillna(value)` |
| fill with mean / median / mode | `fillna(df["c"].mean())`, `.median()`, `.mode()[0]` |
| fill by group | `fillna(df.groupby("g")["c"].transform("mean"))` |
| check types | `df.dtypes`, `df.info()` |
| text to whole numbers | `df["c"].astype(int)` |
| messy text to numbers | `pd.to_numeric(df["c"], errors="coerce")` |
| whole numbers with blanks | `df["c"].astype("Int64")` |
| find repeats | `df.duplicated(subset=[...])` |
| remove repeats | `df.drop_duplicates(subset=[...])` |

## Remember

- Run `df.isna().sum()` and `df.dtypes` first on any new table.
- `dropna`, `fillna`, `astype`, `drop_duplicates` return new results; save them back.
- `subset=` in `dropna`, `duplicated` and `drop_duplicates` limits the check to some columns.
- Fill number columns with the median or mean, text columns with `"Unknown"` or the mode.
- `to_numeric(errors="coerce")` turns bad entries into NaN, so you can count and fix them.
- Clean the text (`.str.strip().str.lower()`, remove symbols) before converting or finding duplicates.

## Watch out

- `df["x"] == np.nan` is always False; use `isna()`.
- `df.isna.sum()` without `()` gives AttributeError.
- `df.dropna()` on its own leaves `df` unchanged; save the result.
- `dropna()` with no `subset` may drop almost every row.
- `df.fillna(df.mean())` fails when text columns exist; choose the column.
- `astype(int)` fails on a bad entry (ValueError) and on NaN (IntCastingNaNError).
- Float to int cuts off the decimals, it does not round.
- Text that looks like numbers adds up as glued text (`'10203040'`), with no error.
- `duplicated()` with a unique id column finds nothing; use `subset`.
- A typo in `subset=[...]` gives KeyError.
- Only the last line of a cell is shown; wrap the other lines in `print()`.

# Topic 10 — Dates: to_datetime, .dt parts, date maths

## The example tables

```python
import pandas as pd

t = pd.DataFrame({"trip":   [1, 2, 3, 4, 5, 6],
                  "start":  ["2026-10-01 09:30", "2026-10-05 18:45", "2026-09-28 07:10",
                             "2026-10-12 14:00", "2026-09-13 22:15", "2026-11-02 11:20"],
                  "amount": [500, 300, 450, 800, 250, 600]})

o = pd.DataFrame({"order_id":  [1, 2, 3, 4, 5],
                  "ordered":   ["2026-10-01", "2026-10-03", "2026-09-25", "2026-10-10", "2026-09-30"],
                  "delivered": ["2026-10-04", "2026-10-10", "2026-09-27", None, "2026-10-02"],
                  "amount":    [500, 300, 450, 800, 250]})
```

## Text to dates: to_datetime

A date read from a CSV is text (`str` / `object`). Convert it to a real date (`datetime64`) so pandas can compare, sort and calculate.

```python
t["start"] = pd.to_datetime(t["start"])     # save it back
t.info()                                    # start is now datetime64

t["start"].min()                            # earliest date
t["start"].max()                            # latest date
t.sort_values("start")                      # sorted by date
t[t["start"] > "2026-10-01"]                # filter by date (compare with a plain text date)
```

- A date with no time shows `00:00:00`.
- Standard text is year-month-day (`2026-10-05`). For another style give `format`.

```python
pd.to_datetime("15/10/2026", format="%d/%m/%Y")            # 2026-10-15
pd.to_datetime("10/05/2026")                               # 2026-10-05 -> read MONTH first
pd.to_datetime("10/05/2026", format="%d/%m/%Y")            # 2026-05-10 -> day first
pd.to_datetime(pd.Series(["15/10/2026", "01/09/2026"]), format="%d/%m/%Y")
pd.to_datetime("15 Oct 2026")                              # pandas reads this by itself
```

| Code | Meaning | Example |
|---|---|---|
| `%d` | day | 15 |
| `%m` | month number | 10 |
| `%Y` | year, 4 digits | 2026 |
| `%y` | year, 2 digits | 26 |
| `%b` | short month name | Oct |
| `%B` | full month name | October |
| `%H:%M` | hour:minute | 14:30 |

Bad dates:

```python
pd.to_datetime(pd.Series(["2026-10-01", "hello", "2026-10-03"]))                    # ValueError
pd.to_datetime(pd.Series(["2026-10-01", "hello", "2026-10-03"]), errors="coerce")   # hello -> NaT
```

- `NaT` is the date version of `NaN`. `isna()`, `dropna()` and `fillna()` work on it.

A date built from separate columns:

```python
d = pd.DataFrame({"day": [15, 16], "month": [10, 10], "year": [2026, 2026]})
pd.to_datetime(d)                          # columns must be named year, month, day
```

## Parts of a date: .dt

The date column must be a real date (`to_datetime` first).

```python
t["start"].dt.year           # no brackets
t["start"].dt.month          # month number
t["start"].dt.day            # day of the month
t["start"].dt.hour
t["start"].dt.minute
t["start"].dt.dayofweek      # Monday = 0 ... Sunday = 6
t["start"].dt.quarter
t["start"].dt.dayofyear
t["start"].dt.day_name()     # with brackets: 'Thursday'
t["start"].dt.month_name()   # with brackets: 'October'
```

Save the parts as columns (they become features for ML):

```python
t["month"] = t["start"].dt.month
t["weekday"] = t["start"].dt.day_name()
t["is_weekend"] = t["start"].dt.dayofweek >= 5      # Saturday or Sunday
```

Filter with a part or a range:

```python
t[t["start"].dt.month == 10]                                           # October trips
t[t["start"].dt.hour >= 12]                                            # afternoon and evening
t[(t["start"] >= "2026-10-01") & (t["start"] < "2026-11-01")]          # a whole month
t[t["start"].between("2026-09-20", "2026-10-05")]                      # inclusive of both ends
```

- A text date means midnight at the start of that day, so `between(..., "2026-10-05")` leaves out 5 Oct 18:45.
- To take a whole month, use `>= first day` and `< first day of next month`.

Group by a part:

```python
t.groupby("month")["amount"].sum()
t.groupby(t["start"].dt.month_name())["amount"].sum()      # names sort A to Z, not by calendar
t["start"].dt.month.value_counts().sort_index()
```

Dates back to text:

```python
t["start"].dt.strftime("%d-%m-%Y")       # '01-10-2026'
t["start"].dt.strftime("%b %Y")          # 'Oct 2026'
t["start"].dt.normalize()                # same date, time set to 00:00:00
```

## Date maths

```python
o["ordered"] = pd.to_datetime(o["ordered"])
o["delivered"] = pd.to_datetime(o["delivered"])

o["days_taken"] = (o["delivered"] - o["ordered"]).dt.days      # gap in plain days (NaN if NaT)
o["days_taken"].mean()                                         # NaN is skipped
o[o["days_taken"] > 3]                                         # slow deliveries
o[o["delivered"].isna()]                                       # not delivered yet

o["due"] = o["ordered"] + pd.Timedelta(days=7)                 # 7 days later (also hours=, weeks=)
```

- date minus date gives a `Timedelta` (a gap). `.dt.days` turns it into plain days.
- `Timedelta` has no months, because months have different lengths.

Group by month with `to_period`:

```python
o.groupby(o["ordered"].dt.to_period("M"))["amount"].sum()
o.groupby(o["ordered"].dt.to_period("M"))["amount"].agg(["sum", "count"])
```

- `to_period("M")` gives labels like `2026-10`, which sort correctly and keep different years apart.

### Optional (use when needed)

```python
o["ordered"] + pd.DateOffset(months=1)                  # calendar months: 15 Oct -> 15 Nov; 31 Jan -> 28 Feb
o["ordered"] - pd.DateOffset(months=1)                  # backwards
today = pd.Timestamp("2026-10-15")                      # a fixed date (pd.Timestamp.today() is the real today)
(today - o["ordered"]).dt.days                          # days since each order
o.sort_values("ordered")["ordered"].diff().dt.days      # days since the previous row (after sorting)
(o["ordered"].max() - o["ordered"].min()).days          # days from first to last
pd.date_range("2026-10-01", periods=4)                  # a list of dates
pd.date_range("2026-10-01", "2026-10-05")
pd.date_range("2026-10-01", periods=3, freq="MS")       # month starts: 1 Oct, 1 Nov, 1 Dec
```

## Quick reference

| Goal | Code |
|---|---|
| text to dates | `df["d"] = pd.to_datetime(df["d"])` |
| day-first text | `pd.to_datetime(df["d"], format="%d/%m/%Y")` |
| bad dates to NaT | `pd.to_datetime(df["d"], errors="coerce")` |
| year / month / day | `df["d"].dt.year`, `.month`, `.day` |
| weekday name | `df["d"].dt.day_name()` |
| weekend | `df["d"].dt.dayofweek >= 5` |
| whole month | `(df["d"] >= "2026-10-01") & (df["d"] < "2026-11-01")` |
| days between | `(df["d2"] - df["d1"]).dt.days` |
| add days | `df["d"] + pd.Timedelta(days=7)` |
| add months | `df["d"] + pd.DateOffset(months=1)` |
| total per month | `df.groupby(df["d"].dt.to_period("M"))["x"].sum()` |
| date to text | `df["d"].dt.strftime("%d-%m-%Y")` |

## Remember

- Run `to_datetime` first and save it back; everything else needs real dates.
- Day-first data needs `format="%d/%m/%Y"`, or pandas reads the month first without any error.
- `errors="coerce"` makes bad dates `NaT`, which you handle like `NaN`.
- `.dt.year`, `.month`, `.day`, `.hour`, `.dayofweek` have no brackets; `day_name()` and `month_name()` have brackets.
- Monday is 0 and Sunday is 6 in `dayofweek`.
- Date minus date is a gap; use `.dt.days` for plain days.
- Group by `dt.to_period("M")` when you need months in the right order.

## Watch out

- `.dt` on a text column gives AttributeError.
- `.dt.month()` with brackets gives TypeError.
- `(d2 - d1).days` without `.dt` gives AttributeError.
- `df["d"] + 5` gives TypeError; write `pd.Timedelta(days=5)`.
- `pd.Timedelta(months=1)` gives ValueError; use `pd.DateOffset(months=1)`.
- One bad date with no `errors="coerce"` stops `to_datetime` with ValueError.
- `between` and text dates mean midnight, so the last day's times are left out.
- Month names sort A to Z, so use the month number or `to_period("M")`.
- Only the last line of a cell is shown; wrap the other lines in `print()`.


# Topic 11 — Read and write: to_csv, read_csv and its options

## The example table

```python
import pandas as pd

df = pd.DataFrame({"name":   ["Asha", "Ravi", "Meena"],
                   "city":   ["Indore", None, "Pune"],
                   "age":    [25, 31, None],
                   "salary": [50000, 62000, 45000]})
```

## Save and read back

A table lives only in the notebook's memory. `to_csv` copies it into a file in the notebook's folder; `read_csv` loads the file back into a table.

```python
df.to_csv("people.csv", index=False)     # save; returns nothing
back = pd.read_csv("people.csv")         # read it back
back.equals(df)                          # True
```

- Always write `index=False`, or the row numbers are saved as a column and come back as `Unnamed: 0`.
- Missing values are written as empty cells and read back as `NaN`. `na_rep="missing"` writes a word instead.
- Save only some columns or a sorted table: `df[["name","salary"]].to_csv(...)`, `df.sort_values("salary").to_csv(...)`.
- Another separator: `to_csv("f.csv", index=False, sep=";")`, and read it back with `sep=";"` too.
- No header line: `to_csv(..., header=False)`.
- Where am I? `os.getcwd()`. Does the file exist? `os.path.exists("people.csv")`.

## read_csv options

| Need | Code |
|---|---|
| only some columns | `pd.read_csv("f.csv", usecols=["city","amount"])` |
| only the first n rows | `pd.read_csv("f.csv", nrows=2)` |
| text column to dates | `pd.read_csv("f.csv", parse_dates=["date"])` |
| force a type | `pd.read_csv("f.csv", dtype={"id": str})` |
| a column as row label | `pd.read_csv("f.csv", index_col="id")` |
| skip junk lines at the top | `pd.read_csv("f.csv", skiprows=1)` |
| extra words that mean missing | `pd.read_csv("f.csv", na_values=["-","NA_"])` |
| file has no header line | `pd.read_csv("f.csv", header=None, names=["name","score"])` |

```python
m = pd.read_csv("messy.csv", skiprows=1, na_values=["-", "NA_"])
m.dtypes          # score is float64 because NaN is inside
```

- `NA`, `NaN`, `null` and empty cells already count as missing. `na_values` is only for extra words.
- A word like `-` in a number column makes the whole column text, so use `na_values`.
- Ids, phone numbers and pin codes are labels, not numbers: `dtype={"id": str}` keeps `007` as `007`.

## Check after reading

```python
df = pd.read_csv("orders.csv")
df.shape            # (rows, columns)
df.head()           # first rows
df.info()           # types and non-null counts
df.isna().sum()     # missing per column
```

## Other formats (optional)

```python
orders.to_json("orders.json", orient="records")
pd.read_json("orders.json")

orders.to_excel("orders.xlsx", index=False)    # needs: pip install openpyxl
pd.read_excel("orders.xlsx")
```

## Remember

- Save with `to_csv(..., index=False)`, read with `read_csv`.
- After every read: `shape`, `head()`, `info()`, `isna().sum()`.
- Use `parse_dates`, `na_values` and `dtype` to get the right types at read time.
- A separator used when saving must be used when reading.
- Use the reader that matches the file: csv, excel, json.

## Watch out

- `df = df.to_csv(...)` makes `df` become `None`, because `to_csv` returns nothing.
- Forgetting `index=False` gives an `Unnamed: 0` column on the next read.
- A wrong file name or folder gives FileNotFoundError.
- A wrong `sep` gives one big column.
- Forgetting `header=None` on a file with no header makes the first data row the column names.
- A wrong column name in `usecols` or `parse_dates` gives ValueError.
- `read_excel` without openpyxl gives ImportError; `read_csv` on an .xlsx file gives garbage or an error.
- The code creates small CSV files in the notebook folder; delete them or add `*.csv` to `.gitignore` before you commit.

# Topic 12 — Merge: joining two tables

## The example tables

```python
import pandas as pd

customers = pd.DataFrame({"cust_id": [1, 2, 3, 4],
                          "name":    ["Asha", "Ravi", "Meena", "Dev"],
                          "city":    ["Indore", "Pune", "Delhi", "Pune"]})

orders = pd.DataFrame({"order_id": [11, 12, 13, 14, 15],
                       "cust_id":  [1, 2, 1, 3, 9],
                       "amount":   [500, 700, 300, 900, 250]})
```

## Merge on a key

The key is the column that appears in both tables. Merge looks up the key of every row of one table in the other table and joins the matching rows side by side.

```python
m = pd.merge(orders, customers, on="cust_id")      # or orders.merge(customers, on="cust_id")
m.shape                                            # (4, 5): orders 5 rows, result 4
m.groupby("name")["amount"].sum()                  # use columns from both tables
```

- The default is an inner merge: only keys present in both tables stay.
- Order 15 (customer 9, not in `customers`) and customer 4 (no orders) disappear, with no error or warning.
- One customer with 2 orders gives 2 result rows.
- Merge does not change the original tables; save the result.

## how= : keep unmatched rows

| how | Keeps | Unmatched side |
|---|---|---|
| `"inner"` (default) | keys in both tables | none |
| `"left"` | all rows of the first table | NaN |
| `"right"` | all rows of the second table | NaN |
| `"outer"` | all rows of both | NaN |

```python
left = pd.merge(orders, customers, on="cust_id", how="left")
left[left["name"].isna()]                           # orders with no customer
nobuy = pd.merge(customers, orders, on="cust_id", how="left")
nobuy[nobuy["order_id"].isna()]["name"].tolist()    # customers who never ordered
chk = pd.merge(orders, customers, on="cust_id", how="outer", indicator=True)
chk["_merge"].value_counts()                        # both / left_only / right_only
left["name"] = left["name"].fillna("unknown")       # Topic 9 tools for the gaps
```

- `left` is the one used most: keep every row of the main table and add information from the other.
- Int columns become float where NaN appears.

## Different key names and same column names

```python
pd.merge(orders, people, left_on="cid", right_on="cust_id")        # keys have different names
m = m.drop(columns="cust_id")                                      # both key columns stay; drop one

pd.merge(a, b, on="id")                                            # same name in another column: city_x, city_y
pd.merge(a, b, on="id", suffixes=("_home", "_work"))               # choose the endings
pd.merge(a, b[["id", "bonus"]], on="id")                           # or bring only the columns you need
```

## Duplicate keys: the silent trap

If a key appears twice in one table, every matching row of the other table is copied twice. There is no error, and sums and means become wrong.

```python
c["cust_id"].is_unique                              # False -> warning sign
pd.merge(o, c, on="cust_id", validate="m:1")        # MergeError if c has duplicate keys
c2 = c.drop_duplicates("cust_id")                   # keep the first row of each key
pd.merge(o, c2, on="cust_id", validate="m:1")
```

- `validate="m:1"` means many rows on the left, one row per key on the right.
- Safe habit: check `is_unique`, compare `shape` and `sum` before and after.

## Remember

- `pd.merge(left, right, on="key", how="...")`; the key must exist in both tables.
- Default is inner; it silently drops rows, so check `shape`.
- "Left" means the table written first.
- `indicator=True` shows where each row came from.
- Use `left_on` / `right_on` for different key names; use `suffixes` for repeated names.
- Check the key is unique where it should be; use `validate="m:1"`.
- Handle the NaN after merge with `fillna` / `dropna`.

## Watch out

- `on="x"` where x is missing in one table gives KeyError.
- A table with no common column and no `on` gives MergeError.
- `how="leftt"` (a wrong word) gives ValueError.
- Duplicate keys change totals with no warning.
- `city_x` / `city_y` columns mean a repeated name was not handled.
- Both key columns stay with `left_on` / `right_on`; drop one.
- Swapping the two tables changes what `left` and `right` keep.