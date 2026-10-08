# Test Cases

Run both cases separately. Calculate expected labor cost and total before each run.

From the repository folder, run:

```text
python 03_execution/freelance_quote_builder.py
```

For each case, paste the terminal input and output as evidence. Mark Pass or Fail and briefly explain why. A passing run has correct amounts, a cleaned client name, the `PROJECT ESTIMATE` heading, labeled costs, and dollars with two decimal places.

## Case 1: Ordinary values

Enter:

- Client name: `Alex Taylor`
- Estimated hours: `4`
- Hourly rate: `30`
- Direct expenses: `15`

**Expected labor cost and total:**
```
labor cost: $120.00
total: $135.00
```

**Evidence (paste your terminal run):**

```
C:\Users\zelda\Documents\GitHub\wetherell-williams-cpw102-freelance-quote-builder\03_execution>python freelance_quote_builder.py
Client name: Alex Taylor
Estimated work hours: 4
Hourly rate: 30
Direct expenses: 15


PROJECT ESTIMATE
Client name: Alex Taylor
Labor cost: $120.00
Direct cost: $15.00
Total estimate: $135.00
```

**Pass / Fail and why:**

Pass because the terminal output correctly gave the expected labor cost and total.

## Case 2: Partial hours and text cleanup

Enter:

- Client name: `  aLEX tAYLOR  ` (include two spaces before and after the name)
- Estimated hours: `2.5`
- Hourly rate: `30`
- Direct expenses: `0`

The displayed name should be `Alex Taylor` without surrounding spaces.

**Expected labor cost and total:**
```
labor cost: $75
total: $75
```

**Evidence (paste your terminal run):**

```
C:\Users\zelda\Documents\GitHub\wetherell-williams-cpw102-freelance-quote-builder\03_execution>python freelance_quote_builder.py
Client name:   aLEX tAYLOR
Estimated work hours: 2.5
Hourly rate: 30
Direct expenses: 0


PROJECT ESTIMATE
Client name: Alex Taylor
Labor cost: $75.00
Direct cost: $0.00
Total estimate: $75.00
```

**Pass / Fail and why:**

If a case fails, fix the program and add evidence of the rerun below that case.

Pass, the terminal did not include the extra spaces in client name and was able to correctly give the expected labor cost and total.