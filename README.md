# Simple Notes API

A RESTful API built with Django REST Framework that allows users to create, read, update, and delete notes.

## Features

- Create new notes with title and content
- Retrieve a list of all notes
- View specific notes by ID
- Update existing notes
- Delete notes
- Automatic timestamp for creation and updates

## Tech Stack

- Django 4.2
- Django REST Framework
- MySQL 8.0
- Docker
- Docker Compose

## API Endpoints

- `GET /api/notes/` - List all notes
- `POST /api/notes/` - Create a new note
- `GET /api/notes/{id}/` - Retrieve a specific note
- `PUT /api/notes/{id}/` - Update a specific note
- `DELETE /api/notes/{id}/` - Delete a specific note

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd simple_notes_api
