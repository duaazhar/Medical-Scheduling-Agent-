# Orthopedic Scheduling Voice Agent

## Overview

This project implements a voice-enabled orthopedic appointment scheduling system designed to integrate with Vogent. The backend serves as the single source of truth for patient records, physician routing, appointment scheduling, call logging, and dashboard analytics.

Patients can:

- Book a new appointment
- Be matched to an appropriate physician based on body part and issue type
- Automatically distinguish between new and returning patients
- View previously scheduled appointments
- Receive the earliest available appointment or appointments matching a requested time preference

The project is built with Flask, SQLAlchemy, SQLite, and a simple HTML/CSS/JavaScript dashboard.

---

## Architecture

```
Vogent Voice Agent
        │
        ▼
    Flask Backend
        │
        ▼
     SQLite Database
        │
        ▼
 Dashboard + REST API
```

The voice agent contains no business logic. All routing, scheduling, and persistence occur in the backend.

---

## Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML/CSS/JavaScript
- Docker
- Ngrok (development)
- Vogent

---

## Features Implemented

### Patient Management

- Create new patients
- Identify returning patients using phone number
- Store patient demographics

### Physician Routing

Routing is based on normalized physician capabilities:

- Body part
- Issue type
- Accepting new patients

Supported body parts:

- Knee
- Hip
- Shoulder
- Hand/Wrist
- Foot/Ankle
- Spine

Supported issue types:

- Fracture
- Sports Medicine
- Joint Replacement
- General

### Scheduling

- Route patients to an eligible physician
- Find available appointment slots
- Respect new-patient eligibility
- Support earliest available scheduling
- Support basic preferred time requests (morning, afternoon, earliest available)
- Book appointments and reserve slots

### Appointment Lookup

Patients can retrieve all scheduled appointments using their phone number.

### Call Logging

Every scheduling attempt creates a call record.

Stored information includes:

- patient
- appointment
- status
- start time
- end time
- transcript (when provided)

### Dashboard

Current dashboard includes:

- Total patients
- Total appointments
- Total calls
- Available slots
- Recent calls
- Doctor availability
- Upcoming appointments

---

## Database Design

Normalized relational schema including:

- Patients
- Doctors
- DoctorCapabilities
- Locations
- DoctorLocations
- BodyParts
- IssueTypes
- Slots
- Appointments
- Calls

Routing rules are stored as structured database records rather than embedded in application logic.

---

## API Endpoints

### Scheduling

```
POST /appointments/book
```

Creates an appointment.

---

### Appointment Lookup

```
POST /appointments/patient
```

Returns all appointments associated with a patient's phone number.

---

### Dashboard

```
GET /dashboard
GET /dashboard/stats
GET /dashboard/calls
GET /dashboard/doctors
GET /dashboard/appointments
```

---

## Docker

The backend has been containerized.

SQLite persistence is maintained using a mounted Docker volume for the Flask `instance` directory.

---

## Testing

Tested manually using:

- Postman
- Vogent Function Calls
- Local dashboard
- Docker container

Scenarios tested include:

- New patient booking
- Returning patient booking
- Physician routing
- No matching physician
- No available slots
- Appointment lookup
- Dashboard statistics
- Call logging

---

## Current Limitations

To prioritize delivering a working end-to-end scheduling system, several features were intentionally simplified.

### Time Preferences

Preferred scheduling currently supports broad requests such as:

- Morning
- Afternoon
- Earliest available

It does not yet optimize for exact dates or perform conversational negotiation over multiple candidate slots.

### Natural Language Normalization

The voice prompt guides callers toward supported body parts and issue types, but backend synonym mapping and fuzzy matching are limited.

### Dashboard

The dashboard focuses on operational visibility and does not yet include filtering, search, analytics over time, or richer visualizations.

### Authentication

No authentication or authorization has been implemented because it was outside the scope of the assignment.

### Production Deployment

The backend has been Dockerized locally. Deployment to AWS EC2 was planned but not completed due to AWS account/payment setup requirements.

---

## Prioritization Decisions

The primary goal was to deliver a complete scheduling workflow rather than maximize feature count.

Priority was given to:

1. Reliable physician routing
2. Appointment scheduling
3. Patient lookup
4. Vogent integration
5. Call logging
6. Dashboard visibility

Features such as richer dashboard analytics, rescheduling, cancellations, advanced NLP normalization, and production infrastructure were intentionally deferred.

---

## Future Improvements

With additional development time I would prioritize:

- AWS EC2 deployment
- Docker Compose configuration
- Improved natural-language normalization
- Flexible scheduling based on specific dates and times
- Appointment cancellation and rescheduling
- Dashboard filtering and search
- Historical analytics and reporting
- Automated testing
- Authentication and authorization
- Background task processing for call logging and notifications

---

## Repository Structure

```
backend/
    models/
    routes/
    services/
    seed/
    templates/
    static/
    instance/
    Dockerfile
    app.py
```