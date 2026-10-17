\# Known Issue Table — Bike-Share Station Manager



| Issue | Type | Line(s) | Description | Fix Approach |

|---|---|---|---|---|

| SQL Injection | Security | 11 | SQL query uses string concatenation to insert station details, which can allow SQL injection. | Use parameterized SQL queries with `?` placeholders. |

| Weak Random PIN | Security | 22 | `random.randint()` is not suitable for generating security-sensitive PINs. | Replace `random` with the `secrets` module. |

| Broad Exception Handling | Code Quality | 30–31 | `except Exception: pass` hides errors and makes debugging difficult. | Catch `sqlite3.Error` and handle the error explicitly. |

| Mutable Default Argument | Bug | 10 | `log=\[]` is shared across calls, so station names can accumulate unexpectedly. | Use `None` as the default and initialize a new list inside the function. |

| Missing Return Value | Bug | 16–20 | `rentBike()` returns `None` when a bike cannot be rented, making the result inconsistent. | Return `False` explicitly when the bike rental fails. |

| Unused Variable | Code Quality | 27 | The `summary` variable is calculated but never used. | Remove the unused variable. |

| Incorrect `None` Comparison | Code Quality | 39 | The code uses `row\[0] == None`, which does not follow recommended Python style. | Use `is None` and check whether the database row exists. |

| Long Lines | Formatting | 6, 11, 16, 17, 27, 31, 38 | Several lines exceed the recommended line length, reducing readability. | Split long statements across multiple lines. |

