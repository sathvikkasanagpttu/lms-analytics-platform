# Telemetry Event Contract

Example JSON:

{
  "event_id": "evt_01HXYZ",
  "event_name": "video_progress",
  "event_version": 1,
  "occurred_at": "2026-09-23T08:30:00Z",
  "user_id": "USR001",
  "course_id": "CRS001",
  "module_id": "MOD004",
  "session_id": "SES001",
  "properties": {
    "position_seconds": 842,
    "video_length_seconds": 1200,
    "device": "web"
  }
}

Required fields:
event_id, event_name, event_version, occurred_at, user_id, session_id.

Recommended governance:
- Never place passwords, payment data or unnecessary PII in telemetry.
- Version event contracts.
- Deduplicate on event_id.
- Store source and ingestion timestamps.
