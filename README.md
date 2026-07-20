# Appointment Scheduling System

## Overview

This project implements an AI-powered orthopedic appointment scheduling backend designed to integrate with a Vogent voice agent.

The architecture separates conversational logic from scheduling logic:

```
Vogent Agent
      │
      ▼
 Flask API
      │
      ▼
Service Layer
      │
      ▼
SQLite Database
```

The backend is the single source of truth for patients, physician routing, scheduling, appointment booking, and call history.

---

# Features Implemented

## Database

- SQLite database
- Normalized relational schema
- SQLAlchemy ORM models
- Seed scripts for physicians, locations, specialties, and appointment slots

Models:

- Patient
- Doctor
- Location
- DoctorLocation
- DoctorSpecialty
- Slot
- Appointment
- Call

---

## Patient Management

- Automatic lookup by phone number
- Existing patient detection
- New patient creation

---

## Physician Routing

Routes patients based on:

- Body part
- Issue type
- Physician specialty
- New patient acceptance rules

Returns the first physician matching all constraints.

---

## Appointment Booking

- Finds earliest available appointment
- Creates appointment
- Marks slot unavailable
- Returns booking confirmation

---

## Call Logging

Every booking attempt creates a Call record.

Successful bookings:

- Scheduled status
- Appointment linked
- Start/end timestamps

Failed bookings:

- Failed status
- Start/end timestamps

---

## Dashboard

Dashboard includes:

- Total patients
- Total appointments
- Total calls
- Successful calls
- Failed calls
- Available slots
- Booked slots
- Recent call history

---

## API

### POST

```
/appointments/book
```

Books an appointment.

### GET

```
/calls
```

Returns call history.

### GET

```
/dashboard
```

Dashboard UI.

### GET

```
/dashboard/stats
```

Dashboard statistics.

### GET

```
/dashboard/calls
```

Recent call history.

---

# Technologies

- Python
- Flask
- SQLAlchemy
- SQLite
- Vogent
- ngrok

---

# Project Priorities

Implementation focused on completing the core scheduling workflow before adding polish.

Prioritized:

- Backend architecture
- Normalized database schema
- Routing engine
- Appointment booking
- Patient lookup
- Vogent backend integration
- Call logging
- Dashboard

Deferred:

- Prompt refinement
- Body-part normalization
- Issue-type normalization
- Better dashboard visualizations
- Comprehensive testing
- Additional dashboard endpoints

---

# Known Issues

- Vogent prompt still allows some free-form responses that should be normalized before reaching the backend.
- Vogent voice testing is currently blocked by account concurrency limits; chat mode is being used during development.
- Transcript storage is implemented but not yet populated from Vogent.
- Dashboard currently refreshes on page load rather than automatically.
- Error handling can be expanded for additional edge cases.

---

# Future Improvements

- Improve prompt engineering
- Alias mapping for body parts and issue types
- Dashboard filters/search
- Appointment cancellation
- Appointment rescheduling
- Better reporting metrics
- Unit tests
- Integration tests
- Voice transcript storage