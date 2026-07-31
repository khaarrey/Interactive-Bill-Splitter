# Interactive Bill Splitter

A simple Python command-line application that calculates a restaurant bill, applies a custom tip percentage, and splits the total equally among a group of people.

## Features

- Accepts user input for:
  - Number of people
  - Appetizers
  - Main courses
  - Desserts
  - Drinks
  - Tip percentage
- Calculates the total bill.
- Calculates the tip based on the user's chosen percentage.
- Displays the total bill including the tip.
- Splits the bill equally among all participants.
- Prevents division by zero by validating the number of people.
- Formats all monetary values to two decimal places.

## Technologies Used

- Python 3

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/khaarrey/interactive-bill-splitter.git
```

2. Navigate into the project folder:

```bash
cd interactive-bill-splitter
```

3. Run the program:

```bash
python main.py
```

## Example Output

```text
Enter the number of people: 3
Enter the total cost of appetizers: 50
Enter the total cost of main courses: 80
Enter the total cost of desserts: 70
Enter the total cost of drinks: 150

Total bill so far: ₦350.00

Enter the tip percentage (%): 12.5

Tip amount: ₦43.75
Total with tip: ₦393.75
Bill per person: ₦131.25
```

## What I Learned

This project helped me practice:

- User input
- Variables
- Arithmetic operations
- Conditional statements (`if` and `else`)
- Input validation
- Floating-point formatting (`:.2f`)
- Writing interactive Python programs

## Future Improvements

- Allow users to split the bill unevenly.
- Save receipts to a file.
- Build a graphical user interface (GUI).
- Develop a web version using Django.

## Author

**Omobude Wisdom**

- GitHub: https://github.com/khaarrey
- LinkedIn: Omobude Wisdom
