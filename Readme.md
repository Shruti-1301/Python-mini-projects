# Email Validation

This mini-project takes an email address as user input and checks whether it is valid or not based on a few simple rules.  
The validation logic uses Python built-in string methods (like `.isalpha()`, `.isdigit()`, `.isspace()`) and also checks for characters like `@` and `.` to ensure the email is in a correct format.

## Validation Rules Implemented

- Email length must be at least 6 characters
- The first character must be an alphabet
- There must be exactly one `@` symbol
- A dot (`.`) must be present in either the 3rd or 4th position from the end (e.g. `.com` or `.in`)
- No spaces are allowed
- No uppercase letters are allowed
- Only the following characters are allowed:
  - alphabets (a–z)
  - digits (0–9)
  - `_`, `.`, `@`

