# 02 Window Functions: topics to study

## Base syntax
- `OVER ()`
- `PARTITION BY`
- `ORDER BY` inside `OVER`
- Logical execution order: `FROM → WHERE → GROUP BY → HAVING → window → QUALIFY → SELECT`

## Functions and clauses
| Ex | Topic |
|---|---|
| 1 | `ROW_NUMBER()` |
| 1, 7 | `QUALIFY` |
| 2 | `RANK()` |
| 2 | `DENSE_RANK()` |
| 2 | Window function over an aggregate (`RANK() OVER (ORDER BY COUNT(*))`) |
| 3 | `LAG()` (and its counterpart `LEAD()`) |
| 4 | `SUM() OVER` (running total) |
| 4, 6 | Window frames: `ROWS BETWEEN ... AND ...` |
| 4, 6 | `UNBOUNDED PRECEDING`, `CURRENT ROW`, `UNBOUNDED FOLLOWING` |
| 5 | `NTILE()` |
| 6 | `FIRST_VALUE()` |
| 6 | `LAST_VALUE()` (and why it needs an explicit frame) |
| 8 | Sessionization: `LAG` + gap flag (`CASE WHEN`) + cumulative `SUM` |
| 8 | Timestamp differences (gap in minutes between events) |

## Extra
- `ROWS BETWEEN` vs `RANGE BETWEEN`
- Default frame when `ORDER BY` is present
- `ROW_NUMBER` vs `RANK` vs `DENSE_RANK` on ties
2