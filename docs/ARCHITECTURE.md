# LMS Analytics Architecture

## 1. Operational layer

The LMS application uses an OLTP PostgreSQL database for users, courses, enrollments and transactions. Application APIs should never run expensive analytical scans against the production workload.

## 2. Event layer

The client emits canonical telemetry events:

- video_played
- video_paused
- video_progress
- video_completed
- quiz_started
- quiz_submitted
- module_opened
- course_completed

A production deployment can use Kafka, Segment or RudderStack.

## 3. Warehouse layers

### Bronze
Immutable landing data. Preserve the original payload and ingestion timestamp.

### Silver
Validated, deduplicated, typed event data. Resolve identities, timestamps, course/module references and malformed records.

### Gold
Business-ready dimensional models. The star schema makes common slicing and aggregation predictable.

## 4. Star schema

Dimensions:
- Dim_User
- Dim_Course
- Dim_Module
- Dim_Date

Facts:
- Fact_Enrollment
- Fact_Learner_Activity

The grain is explicit for every fact. This is critical because mixing enrollment-level and event-level rows in one fact causes incorrect aggregation.

## 5. Serving

BI tools read Gold models. The LMS should consume pre-aggregated API metrics rather than querying raw telemetry from the browser.
