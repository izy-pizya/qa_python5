# README.md


# test log in
This repository contains automated tests for the registration, sign-in, error password handling, personal area log-in, sign-in after registration, sign-in by password recovery button, and logout functionalities of a web application. The tests are designed to be run using Selenium and Python.

## Test Cases

### Registration
This test case verifies the registration process by simulating a user's click on the login button, followed by the registration button. It then enters a valid email, password, and submits the registration form. After waiting for 1 second, it checks if the current URL matches the expected redirection URL.

### Sign in
This test case covers the sign-in process from the main page. It enters a valid email and password, signs in, navigates to the personal area, and checks for the presence of the profile button.

### Error Password
Here, the test case attempts to sign in with an incorrect password and verifies that the appropriate error message is displayed.

### Personal Area Log In
This case logs in from the personal area and validates the presence of the profile button.

### Sign in After Registration
It registers a new account and immediately logs in with the created credentials.

### Sign in by Password Recovery Button
This test scenario covers signing in using the password recovery button and verifies access to the personal area.

### Logout
The final test logs in, visits the personal account, then logs out and verifies that the logout confirmation button appears.


# test tabs

This repository contains automated tests for the functionality of navigating to personal accounts and using certain features on a website.

## Test Cases

### 1. Test Go to Personal Account
- Method: `test_go_to_personal_account(go_to_personal_account)`
- Description: This test verifies that the user can go to their personal account.
- Steps:
    1. Find the accept button using XPath.
    2. Verify if the accept button exists.
    3. Close the driver.

### 2. Test Transition from Personal Account to the Constructor
- Method: `test_transition_from_personal_account_to_the_constructor(go_to_personal_account)`
- Description: This test verifies the transition from the personal account to the constructor feature.
- Steps:
    1. Find the constructor button using XPath.
    2. Click on the constructor button.
    3. Find the "assemble the burger" element using XPath.
    4. Verify if the "assemble the burger" element exists.
    5. Close the driver.

### 3. Test Transition from Personal Account by Logo
- Method: `test_transition_from_personal_account_by_logo(go_to_personal_account)`
- Description: This test verifies the transition from the personal account to the homepage by clicking on the logo button.
- Steps:
    1. Find the logo button using XPath.
    2. Click on the logo button.
    3. Verify if the current URL is 'https://stellarburgers.nomoreparties.site/'.
    4. Close the driver.

## Tools Used
- Selenium WebDriver
- Python

## How to Run the Tests
1. Clone the repository.
2. Install the necessary dependencies.
3. Execute the test files using a test runner or IDE that supports Python testing.

## Contributors
- [Your Name]

## License
This project is licensed under the [License Name] License - see the LICENSE.md file for details.


# test product table

### Navigation Tests
1. **Test Go to Sauce**
   - Method: `test_go_to_sauce(open_hello_window)`
   - Description: Navigates to the sauce section and verifies if the correct element is selected.
   - Expected Outcome: Asserts that the selected element text is 'Соусы'. Quits the driver after the test.

2. **Test Go to Fillings**
   - Method: `test_go_to_fillings(open_hello_window)`
   - Description: Navigates to the fillings section and verifies if the correct element is selected.
   - Expected Outcome: Asserts that the selected element text is 'Начинки'. Quits the driver after the test.

3. **Test Go to Rolls**
   - Method: `test_go_to_rolls(open_hello_window)`
   - Description: Navigates to the rolls section from the fillings section and verifies if the correct element is selected.
   - Expected Outcome: Asserts that the selected element text is 'Булки'. Quits the driver after the test.