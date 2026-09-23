# 5-Minute Demo Script

1. Open the dashboard and explain the separation between OLTP and OLAP.
2. Start with the executive KPI cards: learner population, active learners, completion and assessment pass rate.
3. Explain the enrollment trend as a Gold-layer aggregation.
4. Show learning engagement by module and explain how event-level telemetry identifies drop-off.
5. Explain the course-performance table and how the same facts support curriculum decisions.
6. Open `/docs` on the FastAPI server to demonstrate API contracts.
7. Show `warehouse/models` and explain Bronze -> Silver -> Gold.
8. Explain that Superset/Power BI can connect to Gold models without querying the live LMS.
