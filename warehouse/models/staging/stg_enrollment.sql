select
  enrollment_id,
  user_key,
  course_key,
  date_key,
  cast(transaction_amount as numeric(12,2)) as transaction_amount,
  cast(discount_applied as numeric(12,2)) as discount_applied,
  completion_status,
  days_to_complete
from public.fact_enrollment
where enrollment_id is not null
