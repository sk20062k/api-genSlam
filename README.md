# 🚀 API-GenSlam

A lightweight **FastAPI** backend designed for communication between a mobile app and a robot system.  
Built using **uv** for dependency management, with automated linting, formatting, and testing pipelines.

---

## 📦 Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** — high-performance Python web framework  
- **[uv](https://docs.astral.sh/uv/)** — fast Python package manager  
- **[Ruff](https://github.com/astral-sh/ruff)** — fast linter and static code analyzer  
- **[Black](https://github.com/psf/black)** — code formatter  
- **[Pytest](https://pytest.org/)** — test framework  
- **[Pre-commit](https://pre-commit.com/)** — manage and run checks before commits

---

## ⚙️ Project Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sk20062k/api-genSlam.git
cd api-genSlam
```

### 2️⃣ Install dependencies
```bash
uv sync
```

### 3️⃣ Run the FastAPI server
```bash
uv run fastapi dev main.py
```
or if you prefer `uvicorn` directly:
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 4️⃣ Test the API
Use `curl`, `Postman`, or your Flutter/FlutterFlow app to hit the endpoints.

#### GET /
```bash
curl http://localhost:8000/
```

#### POST /move
```bash
curl -X POST http://localhost:8000/move -H "Content-Type: application/json" -d '{"command": "move_forward", "speed": 1000}'
```

Expected response:
```json
{
  "status": "success",
  "received": {
    "command": "move_forward",
    "speed": 1000
  }
}
```

---

## 🧪 Testing

### Run all tests with coverage
```bash
uv run pytest --cov=main
```

Tests are located under the `tests/` directory.

---

## 🧹 Code Quality & Automation

### Run format and lint checks manually
```bash
uv run black .
uv run ruff check .
```

### Run pre-commit hooks
```bash
uv run pre-commit run --all-files
```

These are automatically triggered before each commit.

---

## 🧱 Folder Structure
```
api-genSlam/
├── main.py              # FastAPI entrypoint
├── test.py / tests/     # Test files
├── pyproject.toml       # Project configuration (uv, ruff, black, pytest)
├── .pre-commit-config.yaml
├── README.md
└── uv.lock
```

---

## 🌐 Local Network Access

To allow your **mobile app (Flutter/FlutterFlow)** to access this API:
1. Find your local IP using:
   ```bash
   ifconfig
   ```
   Example: `192.168.1.16`
2. Start your API using:
   ```bash
   uv run uvicorn main:app --host 0.0.0.0 --port 8000
   ```
3. In your app, call:
   ```
   http://192.168.1.16:8000/move
   ```

---

## 🧰 CI/CD (Optional)
You can enable automated linting, formatting, and tests by adding a **GitHub Actions** workflow at  
`.github/workflows/ci.yml` (ask ChatGPT to generate this for you).

---

## 📄 License
This project is licensed under the **MIT License**.

---

**Developed by:** [@sk20062k](https://github.com/sk20062k)
