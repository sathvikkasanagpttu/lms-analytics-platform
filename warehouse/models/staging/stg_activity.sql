select
  activity_id,
  user_key,
  course_key,
  module_key,
  date_key,
  watch_duration_seconds,
  total_video_length_seconds,
  dropoff_timestamp,
  quiz_score,
  quiz_max_score,
  passed_flag
from public.fact_learner_activity
where activity_id is not null
