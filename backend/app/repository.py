class DemoAnalytics:
    def overview(self):
        return {
            "learners": 12840, "active_learners": 6842, "courses": 86,
            "enrollments": 21756, "completion_rate": 68.4,
            "watch_completion": 74.8, "quiz_pass_rate": 81.6,
            "revenue": 1842500, "dau_mau": 0.53
        }

    def enrollments(self):
        return [
            {"month":"Apr","enrollments":2680,"revenue":218000},
            {"month":"May","enrollments":3010,"revenue":246000},
            {"month":"Jun","enrollments":3290,"revenue":279000},
            {"month":"Jul","enrollments":3475,"revenue":296000},
            {"month":"Aug","enrollments":3810,"revenue":334000},
            {"month":"Sep","enrollments":4120,"revenue":469500}
        ]

    def course_performance(self):
        return [
            {"course_id":"CRS001","course":"Python for Data Analytics","category":"Data Analytics","difficulty":"Intermediate","learners":3840,"completion":82,"quiz_pass":91,"watch":88,"rating":4.7},
            {"course_id":"CRS002","course":"SQL Mastery","category":"Data Analytics","difficulty":"Intermediate","learners":3290,"completion":77,"quiz_pass":86,"watch":81,"rating":4.6},
            {"course_id":"CRS003","course":"Power BI Business Intelligence","category":"BI","difficulty":"Intermediate","learners":2870,"completion":74,"quiz_pass":84,"watch":79,"rating":4.5},
            {"course_id":"CRS004","course":"Statistics Fundamentals","category":"Statistics","difficulty":"Beginner","learners":2210,"completion":63,"quiz_pass":76,"watch":69,"rating":4.3},
            {"course_id":"CRS005","course":"Advanced Excel","category":"Productivity","difficulty":"Advanced","learners":1980,"completion":58,"quiz_pass":71,"watch":64,"rating":4.2}
        ]

    def activity(self):
        return [
            {"module":"Introduction","content_type":"Video","sessions":6820,"watch_completion":94,"dropoff":6,"avg_minutes":8.2},
            {"module":"Data Cleaning","content_type":"Video","sessions":6310,"watch_completion":88,"dropoff":12,"avg_minutes":16.4},
            {"module":"Exploratory Analysis","content_type":"Lab","sessions":5870,"watch_completion":79,"dropoff":21,"avg_minutes":24.8},
            {"module":"Visualization","content_type":"Video","sessions":5120,"watch_completion":71,"dropoff":29,"avg_minutes":19.7},
            {"module":"Final Assessment","content_type":"Quiz","sessions":4460,"watch_completion":62,"dropoff":38,"avg_minutes":28.5}
        ]

    def assessments(self):
        return [
            {"assessment":"Python Fundamentals Quiz","course":"Python for Data Analytics","attempts":4820,"pass_rate":91,"avg_score":87,"avg_time":14.2,"difficulty":"Medium"},
            {"assessment":"SQL Query Challenge","course":"SQL Mastery","attempts":4110,"pass_rate":86,"avg_score":82,"avg_time":18.7,"difficulty":"Hard"},
            {"assessment":"Power BI DAX Test","course":"Power BI Business Intelligence","attempts":3670,"pass_rate":84,"avg_score":80,"avg_time":21.3,"difficulty":"Hard"},
            {"assessment":"Statistics Checkpoint","course":"Statistics Fundamentals","attempts":2910,"pass_rate":76,"avg_score":74,"avg_time":16.8,"difficulty":"Medium"},
            {"assessment":"Excel Modeling Test","course":"Advanced Excel","attempts":2480,"pass_rate":71,"avg_score":69,"avg_time":24.1,"difficulty":"Hard"}
        ]

    def learner_activity(self):
        return {
            "events_today": 186420,
            "video_events": 98240,
            "quiz_events": 28410,
            "module_opens": 41160,
            "active_sessions": 3420,
            "top_events":[
                {"event":"video_progress","count":54280},
                {"event":"video_played","count":31120},
                {"event":"module_opened","count":24780},
                {"event":"quiz_submitted","count":16340},
                {"event":"video_completed","count":12100}
            ],
            "device_mix":[{"device":"Web","share":58},{"device":"Android","share":27},{"device":"iOS","share":15}]
        }

    def data_model(self):
        return {
            "layers":[
                {"name":"Bronze / Raw","purpose":"Immutable source snapshots and raw telemetry payloads","examples":["raw_users","raw_courses","raw_enrollments","raw_events"]},
                {"name":"Silver / Clean","purpose":"Typed, deduplicated and validated records","examples":["stg_users","stg_courses","stg_enrollment","stg_activity"]},
                {"name":"Gold / Semantic","purpose":"Business-ready dimensional models and KPI marts","examples":["Dim_User","Dim_Course","Dim_Module","Dim_Date","Fact_Enrollment","Fact_Learner_Activity"]}
            ],
            "relationships":[
                "Dim_User 1:N Fact_Enrollment",
                "Dim_Course 1:N Fact_Enrollment",
                "Dim_User 1:N Fact_Learner_Activity",
                "Dim_Course 1:N Fact_Learner_Activity",
                "Dim_Module 1:N Fact_Learner_Activity",
                "Dim_Date 1:N Fact_Enrollment",
                "Dim_Date 1:N Fact_Learner_Activity"
            ],
            "grain":[
                {"table":"Fact_Enrollment","grain":"One row per course registration/purchase"},
                {"table":"Fact_Learner_Activity","grain":"One row per atomic learner interaction/session event"}
            ]
        }

    def data_dictionary(self):
        return {
            "dimensions":[
                {"table":"Dim_User","key":"UserKey","columns":["User_ID","Role","Signup_Date","Country","Account_Status"]},
                {"table":"Dim_Course","key":"CourseKey","columns":["Course_ID","Course_Name","Category","Difficulty_Level","Price","Instructor_ID"]},
                {"table":"Dim_Module","key":"ModuleKey","columns":["Module_ID","CourseKey","Module_Title","Sequence_Order","Content_Type"]},
                {"table":"Dim_Date","key":"DateKey","columns":["Full_Date","Day_Of_Week","Month","Quarter","Year","Is_Weekend"]}
            ],
            "facts":[
                {"table":"Fact_Enrollment","grain":"One row per course purchase/registration","measures":["Transaction_Amount","Discount_Applied","Completion_Status","Days_To_Complete"]},
                {"table":"Fact_Learner_Activity","grain":"One row per atomic interaction/session log","measures":["Watch_Duration_Seconds","Total_Video_Length_Seconds","Dropoff_Timestamp","Quiz_Score","Quiz_Max_Score","Passed_Flag"]}
            ]
        }

analytics=DemoAnalytics()
