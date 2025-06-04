# zionix-be-v1

## Domain and Applications API Service

This is a FastAPI-based microservice for managing domains and applications.

## Deployment on Render

### Prerequisites
- A GitHub account
- A Render account (https://render.com)
- Your code pushed to a GitHub repository

### Deployment Steps

1. Fork or push this repository to your GitHub account

2. In Render Dashboard:
   - Click "New +"
   - Select "Web Service"
   - Connect your GitHub repository
   - Choose the repo and branch

3. Configure the Web Service:
   - Name: admin-service (or your preferred name)
   - Environment: Python
   - Region: (Choose nearest to your users)
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

4. Add Environment Variables:
   The render.yaml file will automatically configure most environment variables when using Render's database service.

5. Deploy:
   - Click "Create Web Service"
   - Render will automatically deploy your application

### Local Development

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd zionix-be-v1
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   .\venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   alembic upgrade head
   ```

5. Start the service:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

Once deployed, API documentation is available at:
- Swagger UI: `https://your-service.onrender.com/docs`
- ReDoc: `https://your-service.onrender.com/redoc`