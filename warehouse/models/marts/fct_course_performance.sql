select
  c.course_key,
  c.course_name,
  count(distinct e.enrollment_id) as enrollments,
  round(avg(e.completion_status)::numeric * 100, 2) as completion_rate,
  round(sum(e.transaction_amount)::numeric, 2) as revenue
from {{ ref('stg_enrollment') }} e
join public.dim_course c on e.course_key = c.course_key
group by c.course_key, c.course_name
