-- Gold assessment mart pattern. Replace source names with production assessment tables.
select
  course_key,
  count(*) as attempts,
  round(avg(quiz_score / nullif(quiz_max_score,0) * 100),2) as avg_score_pct,
  round(avg(passed_flag)*100,2) as pass_rate_pct
from {{ ref('stg_activity') }}
where quiz_score is not null
group by course_key
