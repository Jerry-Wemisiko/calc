# Basic Calculator Program

## Description
This is a simple Python calculator that allows users to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division). The program then performs the selected operation and displays the result.

## Features
- Accepts user input for two numbers.
- Supports basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Handles division by zero with an appropriate error message.
- Uses formatted string literals (`f-strings`) for clear output.

## Usage
### 1. Run the program
Ensure you have Python installed and run the script from a terminal:
```sh
python3 calc.py
```

### 2. Enter inputs
The program will prompt you to enter:
1. First number
2. Second number
3. Mathematical operation (`+`, `-`, `*`, `/`)

Example:
```
Enter first number: 10
Enter second number: 5
Enter math operation (+, -, *, /): +
10 + 5 = 15
```

## Requirements
- Python 3.x

## Possible Errors and Fixes
- **Invalid Input:** If the user enters a non-numeric value, the program will crash. Handling exceptions (`try-except`) can improve this.
- **Division by Zero:** The program already includes a check to prevent division by zero.

## Future Enhancements
- Implement exception handling for invalid inputs.
- Add support for more mathematical operations (exponentiation, modulus, etc.).
- Create a GUI version using Tkinter or PyQt.

## Author
[Skyles]

## License
This project is licensed under the MIT License.

