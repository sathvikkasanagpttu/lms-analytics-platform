# Expanded Analytics Modules

## Learning Activities
The activity layer captures atomic learner behavior:
- video_played, video_paused, video_progress, video_completed
- module_opened
- quiz_started, quiz_submitted
- course_completed

Recommended analysis:
1. Session frequency and duration
2. Video completion curve
3. Module drop-off
4. Active learner cohorts
5. Device/channel behavior
6. Content engagement by course

## Courses
Course analytics combines enrollment facts with activity and assessment facts.
Key metrics:
- Enrollment volume
- Revenue
- Completion rate
- Average watch completion
- Quiz pass rate
- Rating
- Time to completion
- Learner cohort performance

## Assessments
Assessment analytics should preserve attempt number and question-level telemetry where available.
Key metrics:
- First-attempt pass rate
- Average score
- Average completion time
- Retry rate
- Difficulty by assessment
- Question-level correctness
- Time spent per question
- Skill/mastery progression

## Data Model
The Gold layer is intentionally dimensional:
- Dimensions provide slicing context.
- Facts provide measurable events.
- Date is a conformed dimension shared by multiple facts.
- Surrogate keys isolate warehouse identity from source-system identifiers.

## Recommended future fact tables
For a production-scale LMS:
- Fact_Assessment_Attempt
- Fact_Assessment_Response
- Fact_Course_Session
- Fact_Content_Progress
- Fact_Subscription
- Fact_Certificate
