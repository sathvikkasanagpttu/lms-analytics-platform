CREATE TABLE IF NOT EXISTS dim_user (
  user_key BIGSERIAL PRIMARY KEY,
  user_id VARCHAR(50) NOT NULL,
  role VARCHAR(20) NOT NULL,
  signup_date DATE NOT NULL,
  country VARCHAR(80),
  account_status VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS dim_course (
  course_key BIGSERIAL PRIMARY KEY,
  course_id VARCHAR(50) NOT NULL,
  course_name VARCHAR(200) NOT NULL,
  category VARCHAR(100),
  difficulty_level VARCHAR(30),
  price NUMERIC(12,2),
  instructor_id VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS dim_module (
  module_key BIGSERIAL PRIMARY KEY,
  module_id VARCHAR(50) NOT NULL,
  course_key BIGINT,
  module_title VARCHAR(200),
  sequence_order INT,
  content_type VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS dim_date (
  date_key INT PRIMARY KEY,
  full_date DATE NOT NULL,
  day_of_week VARCHAR(15),
  month INT,
  quarter INT,
  year INT,
  is_weekend BOOLEAN
);

CREATE TABLE IF NOT EXISTS fact_enrollment (
  enrollment_id VARCHAR(60) PRIMARY KEY,
  user_key BIGINT,
  course_key BIGINT,
  date_key INT,
  transaction_amount NUMERIC(12,2),
  discount_applied NUMERIC(12,2),
  completion_status INT,
  days_to_complete INT
);

CREATE TABLE IF NOT EXISTS fact_learner_activity (
  activity_id VARCHAR(60) PRIMARY KEY,
  user_key BIGINT,
  course_key BIGINT,
  module_key BIGINT,
  date_key INT,
  watch_duration_seconds INT,
  total_video_length_seconds INT,
  dropoff_timestamp INT,
  quiz_score NUMERIC(8,2),
  quiz_max_score NUMERIC(8,2),
  passed_flag INT
);

INSERT INTO dim_date(date_key,full_date,day_of_week,month,quarter,year,is_weekend)
VALUES (20260923,'2026-09-23','Wednesday',9,3,2026,false)
ON CONFLICT DO NOTHING;

INSERT INTO dim_user(user_id,role,signup_date,country,account_status)
VALUES
('USR001','Learner','2026-01-10','India','Active'),
('USR002','Learner','2026-02-17','India','Active'),
('USR003','Instructor','2025-11-02','India','Active')
ON CONFLICT DO NOTHING;

INSERT INTO dim_course(course_id,course_name,category,difficulty_level,price,instructor_id)
VALUES
('CRS001','Python for Data Analytics','Data Analytics','Intermediate',7999,'USR003'),
('CRS002','SQL Mastery','Data Analytics','Intermediate',5999,'USR003'),
('CRS003','Power BI Business Intelligence','BI','Intermediate',6999,'USR003')
ON CONFLICT DO NOTHING;
