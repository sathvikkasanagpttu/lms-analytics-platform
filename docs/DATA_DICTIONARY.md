# Data Dictionary

## Dim_User
One record per analytical user version in the simplified demo.
- UserKey: surrogate warehouse key
- User_ID: source-system identifier
- Role: Learner / Instructor / Admin
- Signup_Date: registration date
- Country: learner geography
- Account_Status: current account status

## Dim_Course
One record per course.
- CourseKey: surrogate key
- Course_ID: source course identifier
- Course_Name: display name
- Category: business category
- Difficulty_Level: course difficulty
- Price: list price
- Instructor_ID: source instructor identifier

## Dim_Module
One record per course module.
- ModuleKey: surrogate key
- Module_ID: source module identifier
- CourseKey: related course
- Sequence_Order: module sequence
- Content_Type: Video / Quiz / Reading

## Fact_Enrollment
Grain: one row per purchase/registration.
Measures include transaction amount, discount, completion status and days to complete.

## Fact_Learner_Activity
Grain: one row per atomic learning interaction/session log.
Measures include watch duration, video length, drop-off timestamp, quiz score and pass flag.
