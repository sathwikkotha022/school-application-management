# TODO: Fix Duplicate User Creation in POST /api/student

## Steps to Complete

- [x] Add imports for HTTPException in backend/app/api/student/router.py
- [x] Add uniqueness checks for email and username before creating user in create_student_with_user function
- [ ] Test endpoint with duplicate email to ensure 400 error
- [ ] Test endpoint with duplicate username to ensure 400 error
- [ ] Test endpoint with unique data to ensure successful creation
