# Engineering Design

**Team members: Owen Wetherell, Ty Williams**

Plan how your code will meet the product requirements. Keep answers brief.

## Inputs

(string) Client Name

(float) Estimated work hours

(float) Hourly rate

(float) Direct Expenses


## Processing

Multiply estimated work hours by hourly rate to calculate labor cost

strip and title client name

round dollar amounts to two decimal places and add a dollar sign in front of the value

## Output

program will display the following format

PROJECT ESTIMATE\
Client: Alex Taylor\
Labor cost: $300.00\
Direct expenses: $25.00\
Total estimate: $325.00

## Functions

`main()` will call the other functions in order, accepts no parameters and does not return

`project_estimate()` takes parameters name, hours, hourly rate, and direct expenses, calculates the estimated labor cost and total cost, and returns them
