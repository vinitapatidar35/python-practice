# Pandas quick revision (Topics 1 to 12)

Read top to bottom in about 15 minutes. Each line is "goal -> code". Details and traps are in the full `notes.md`.

```python
import pandas as pd
df = pd.DataFrame({"name": ["Asha", "Ravi", "Meena", "Dev"],
                   "city": ["Indore", "Pune", "Delhi", "Pune"],
                   "marks": [82, 67, 75, 91]})
```

## 1 to 5. Basics: make, look, select, filter, new columns

| Goal | Code |
|---|---|
| make a table / read a file | `pd.DataFrame({...})`, `pd.read_csv("f.csv")` |
| first / last rows | `df.head(2)`, `df.tail(1)` |
| size, names, types | `df.shape`, `df.columns.tolist()`, `df.dtypes` |
| summary | `df.info()`, `df.describe()` |
| one column (Series) | `df["name"]` |
| several columns (table) | `df[["name", "marks"]]` |
| by label | `df.loc[0:1, ["name", "marks"]]` (end included) |
| by position | `df.iloc[0:2, 0:2]` (end excluded) |
| filter rows | `df[df["marks"] > 70]` |
| two conditions | `df[(df["city"] == "Pune") & (df["marks"] > 80)]` (use `&` `\|` `~`, brackets needed) |
| value in a list | `df[df["city"].isin(["Pune", "Delhi"])]` |
| in a range | `df[df["marks"].between(70, 85)]` (both ends included) |
| text contains | `df[df["name"].str.contains("a")]` (case matters) |
| new column | `df["double"] = df["marks"] * 2` |
| rename | `df.rename(columns={"marks": "score"})` |
| quick stats | `df["marks"].mean()`, `.sum()`, `.max()`, `.min()` |
| counts | `df["city"].value_counts()`, `.nunique()`, `.unique()` |

- Most methods return a new table. Save it: `df = df.something(...)`.
- Conditions use `&` `|` `~`, not `and` `or` `not`.

## 6. Adding and removing

| Goal | Code |
|---|---|
| remove columns | `df.drop(columns=["a", "b"])` |
| remove rows by label | `df.drop(index=[1, 3])` |
| remove a column and keep it | `m = df.pop("a")` |
| add a row | `df.loc[len(df)] = [...]` |
| stack tables | `pd.concat([a, b], ignore_index=True)` |
| glue side by side | `pd.concat([a, b], axis=1)` (matches by label) |
| column at a position | `df.insert(1, "new", [...])` |
| reorder columns | `df[["c", "a", "b"]]` |

- Always write `columns=` or `index=` in `drop`. `pd.concat` takes a list.
- `df = df.insert(...)` makes `df` None.

## 6A. get_dummies (text to 0/1 columns)

- `pd.get_dummies(df, columns=["city"])`, `drop_first=True` to drop one column, `dtype=int` for 0/1 numbers.
- Do it on train and test together (or reindex the test), or the columns will not match.

## 7. Sorting

| Goal | Code |
|---|---|
| sort | `df.sort_values("marks", ascending=False)` |
| several columns | `df.sort_values(["city", "marks"], ascending=[True, False])` |
| top / bottom n | `df.nlargest(2, "marks")`, `df.nsmallest(2, "marks")` |
| sort by row labels | `df.sort_index()` |
| rank | `df["marks"].rank(ascending=False).astype(int)` |

- NaN goes last by default. Ties in `rank` share an average rank unless `method="min"` is set.

## 8. Groupby

| Goal | Code |
|---|---|
| one number per group | `df.groupby("city")["marks"].mean()` |
| as a table | `.reset_index()` or `groupby("city", as_index=False)` |
| many numbers | `df.groupby("city").agg(avg=("marks", "mean"), n=("name", "count"))` |
| two group columns | `df.groupby(["city", "x"])` (one list) |
| group label of the max | `.idxmax()` |
| keep original length | `df.groupby("city")["marks"].transform("mean")` |
| share of group total | `df["x"] / df.groupby("g")["x"].transform("sum")` |
| keep big groups | `df.groupby("g").filter(lambda g: len(g) > 1)` |
| top rows per group | sort first, then `groupby("g").head(2)` |

- `df["new"] = df.groupby(...).sum()` gives all NaN with no error. Use `transform`.
- `groupby("a", "b")` is wrong. Use `groupby(["a", "b"])`.

## 9. Cleaning and missing values

| Goal | Code |
|---|---|
| find missing | `df.isna().sum()`, `(df.isna().mean() * 100).round(1)` |
| drop | `df.dropna()`, `dropna(subset=["a"])`, `dropna(how="all")`, `dropna(thresh=2)` |
| fill | `df["a"].fillna(df["a"].mean())`, `fillna({"a": 0, "b": "unknown"})` |
| fill by group | `df["a"].fillna(df.groupby("g")["a"].transform("mean"))` |
| change type | `astype(int)`, `astype("category")`, `pd.to_numeric(s, errors="coerce")` |
| strip "Rs " and "," | `s.str.replace("Rs ", "").str.replace(",", "")` then `astype(int)` |
| duplicates | `df.duplicated()`, `df.drop_duplicates(subset=["a"], keep="first")` |
| clean text first | `s.str.strip().str.lower()` before checking duplicates |
| fresh row numbers | `reset_index(drop=True)` |

- `astype(int)` on a column with NaN fails (IntCastingNaNError). Fill first, or use `"Int64"`.
- `dropna(subset=...)`, not `isna(subset=...)`.

## 10. Dates

| Goal | Code |
|---|---|
| text to dates | `pd.to_datetime(s)`, `format="%d/%m/%Y"` for day first, `errors="coerce"` for bad ones |
| parts (no brackets) | `s.dt.year`, `.month`, `.day`, `.hour`, `.dayofweek` (Mon = 0), `.quarter` |
| names (brackets) | `s.dt.day_name()`, `s.dt.month_name()` |
| weekend | `s.dt.dayofweek >= 5` |
| days between | `(d2 - d1).dt.days` |
| add days / months | `d + pd.Timedelta(days=7)`, `d + pd.DateOffset(months=1)` |
| total per month | `df.groupby(df["d"].dt.to_period("M"))["x"].sum()` |
| date to text | `s.dt.strftime("%d-%m-%Y")` |

- Convert first and save it back; `.dt` on text gives AttributeError.
- Wrong `format` day/month swap gives no error, so check one value by eye.

## 11. Read and write

| Goal | Code |
|---|---|
| save | `df.to_csv("f.csv", index=False)` |
| read | `pd.read_csv("f.csv")` |
| options | `usecols=[...]`, `nrows=n`, `skiprows=n`, `index_col="id"`, `sep=";"` |
| types at read time | `parse_dates=["date"]`, `dtype={"id": str}` |
| extra missing words | `na_values=["-", "NA_"]` |
| no header line | `header=None, names=[...]` |
| check after reading | `shape`, `head()`, `info()`, `isna().sum()` |
| other formats | `to_json` / `read_json`, `to_excel` / `read_excel` (needs openpyxl) |

- No `index=False` gives an `Unnamed: 0` column later.
- `df = df.to_csv(...)` makes `df` None. The `sep` used to save must be used to read.

## 12. Merge

| Goal | Code |
|---|---|
| join on a key | `pd.merge(orders, customers, on="cust_id")` (inner by default) |
| keep all of the first table | `how="left"` (also `"right"`, `"outer"`) |
| see what matched | `how="outer", indicator=True` then `value_counts()` on `_merge` |
| different key names | `left_on="cid", right_on="cust_id"`, then drop one |
| same column name | `suffixes=("_a", "_b")` or select needed columns first |
| guard against duplicates | `df["key"].is_unique`, `validate="m:1"` |

- Inner drops unmatched rows silently, so compare `shape` before and after.
- Duplicate keys copy rows and make sums wrong, with no error.

## Daily habits

1. After reading or merging: `shape`, `head()`, `info()`, `isna().sum()`.
2. Save the result of every method; print only what you need.
3. When a KeyError appears: print `df.columns.tolist()`.
4. Check totals before and after merge or groupby.
