# 🧠 AI Resume Screener

> An AI-powered SaaS tool that analyzes resumes against job descriptions — scoring match quality, identifying skill gaps, and delivering actionable improvement suggestions.

![Tech Stack](https://img.shields.io/badge/Frontend-React%20%2B%20Vite-61DAFB?style=for-the-badge&logo=react)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)
![Database](https://img.shields.io/badge/Database-MongoDB%20Atlas-47A248?style=for-the-badge&logo=mongodb)
![AI](https://img.shields.io/badge/AI-Claude%20%28Anthropic%29-CC785C?style=for-the-badge)
![Deploy](https://img.shields.io/badge/Deploy-Railway%20%2B%20Vercel-black?style=for-the-badge)

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [API Reference](#-api-reference)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

AI Resume Screener lets users upload a resume (PDF) and paste a job description. Claude AI analyzes both documents and returns:

- A **match score** (0–100%)
- **Matched skills** found in both resume and JD
- **Missing skills** required by the JD but absent from the resume
- **Improvement suggestions** to tailor the resume better

Built as a full-stack SaaS with user authentication, scan history, and a clean dashboard — all using free-tier services from the **GitHub Student Developer Pack**.

---

## ✨ Features

- 📄 Upload resume as PDF — text extracted automatically
- 📝 Paste any job description
- 🤖 Claude AI analyzes and scores the match
- ✅ See matched skills at a glance
- ❌ Identify missing/gap skills instantly
- 💡 Get actionable resume improvement tips
- 🔐 JWT-based user authentication
- 📂 View history of past scans per user
- 🚀 Fully deployed (Railway + Vercel + Namecheap)

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 18 + Vite |
| Backend | Python + FastAPI |
| AI Provider | Anthropic Claude API |
| Database | MongoDB Atlas |
| Auth | JWT (JSON Web Tokens) |
| PDF Parsing | pdfplumber |
| Backend Hosting | Railway |
| Frontend Hosting | Vercel |
| Domain | Namecheap |

---

## 📁 Project Structure

```
ai-resume-screener/
├── backend/
│   ├── main.py                  # FastAPI app entry point
│   ├── routes/
│   │   ├── analyze.py           # Resume analysis endpoints
│   │   └── auth.py              # Register / Login endpoints
│   ├── services/
│   │   ├── pdf_parser.py        # Extract text from PDF uploads
│   │   └── ai_analyzer.py       # Claude API integration
│   ├── db/
│   │   └── mongo.py             # MongoDB Atlas connection
│   ├── .env                     # Environment variables (not committed)
│   ├── .env.example             # Example env file
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/          # Reusable UI components
│   │   ├── pages/               # Upload page, Results page, History page
│   │   └── App.jsx
│   ├── .env                     # Frontend env variables
│   └── vite.config.js
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- MongoDB Atlas account (free M0 tier)
- Anthropic API key ([get one here](https://console.anthropic.com))

---

### 1. Clone the Repository

```bash
git clone https://github.com/MayankHenry/Resume-Screener.git
cd Resume-Screener
```

---

### 2. Backend Setup

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

Run the backend:

```bash
uvicorn main:app --reload
```

Backend runs at `http://localhost:8000`

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`

---

## 🔐 Environment Variables

### `backend/.env`

```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/resume-screener
JWT_SECRET=your_super_secret_jwt_key
```

### `frontend/.env`

```env
VITE_API_URL=http://localhost:8000/api
```

> ⚠️ Never commit `.env` files. They are listed in `.gitignore`.

---

## 📡 API Reference

### `POST /api/analyze`
Upload a resume PDF and job description for AI analysis.

**Request:** `multipart/form-data`
| Field | Type | Description |
|---|---|---|
| `resume` | File (PDF) | Resume file to analyze |
| `job_description` | string | Full job description text |

**Response:**
```json
{
  "match_score": 78,
  "matched_skills": ["Python", "FastAPI", "REST APIs", "MongoDB"],
  "missing_skills": ["Docker", "Kubernetes", "CI/CD"],
  "suggestions": [
    "Add Docker experience to your skills section",
    "Mention any CI/CD pipelines you have worked with",
    "Quantify your project outcomes with metrics"
  ]
}
```

---

### `POST /api/auth/register`
Register a new user.

```json
{ "email": "user@example.com", "password": "securepassword" }
```

---

### `POST /api/auth/login`
Login and receive a JWT token.

```json
{ "email": "user@example.com", "password": "securepassword" }
```

---

### `GET /api/history`
Get all past scans for the authenticated user. Requires `Authorization: Bearer <token>` header.

---

## 🗺 Roadmap

- [x] Phase 1 — Project setup & structure
- [ ] Phase 2 — PDF parsing + Claude API integration
- [ ] Phase 3 — Frontend UI (upload + results dashboard)
- [ ] Phase 4 — Auth + scan history
- [ ] Phase 5 — Deploy to Railway + Vercel + Namecheap

---

## 🤝 Contributing

This is a personal SaaS project built for learning and portfolio purposes. Feel free to fork it and build your own version.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'feat: add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

MIT License — feel free to use this project as a reference or starting point.

---
