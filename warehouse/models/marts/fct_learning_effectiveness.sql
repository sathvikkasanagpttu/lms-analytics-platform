select
  course_key,
  round(
    avg(case when total_video_length_seconds > 0
      then watch_duration_seconds::numeric / total_video_length_seconds * 100
      else null end), 2
  ) as avg_watch_completion_pct,
  round(avg(quiz_score / nullif(quiz_max_score, 0) * 100), 2) as avg_quiz_score_pct,
  round(avg(passed_flag) * 100, 2) as pass_rate_pct
from {{ ref('stg_activity') }}
group by course_key
