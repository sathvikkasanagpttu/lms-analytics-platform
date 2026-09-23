# KPI Definitions

## DAU / MAU
Distinct active learners in a day divided by distinct active learners in the month.

## Average Watch Completion %
sum(watch_duration_seconds) / sum(total_video_length_seconds) * 100

For better accuracy, compute at the intended grain and exclude impossible durations.

## Course Completion Rate
completed enrollments / total enrollments * 100

## First-Attempt Quiz Pass Rate
passed first-attempt quizzes / submitted first-attempt quizzes * 100

## Revenue
sum(transaction_amount - discount_applied)

## Drop-off
A learner's final observed progress position before an abandonment window. Define the inactivity threshold explicitly (for example, 30 minutes or 24 hours) so the metric is reproducible.
