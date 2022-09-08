# LOGIN AND REGISTRATION

***

## Tasks:

- [x] 1 Create a new Flask project.
- [x] 2 Create a new MySQL database with a table and the appropriate fields.
- [x] 3 The root route should display a template with the login and registrations forms.
- [x] 4 Validate the registration input.
- [x] 5 If registration is invalid, error messages should be displayed on the index page.
- [x] 6 If registration is valid, hash the password and save the user in the database.
    * [x] 6.1 Store the user in session and then redirect to the success page.
- [x] 7 Valdiate login input.
    - Check the notes in the platform to learn how to check passwords with bcrypt
- [x] 8 If invalid login, display an error message on the index page.
- [x] 9 If login valid, store the user in session and redirect to the success page.
- [x] 10 Add logout functionality to success page which clears the session.
- [x] 11 After logging out, verify you cannot reach the success page.
- [ ] NINJA Bonus: Add addtional validation on passwords to have at least 1 number and 1 uppercase letter.
- [ ] SENSEI Bonus: Add additional input types on the form. Get creative with validations.
