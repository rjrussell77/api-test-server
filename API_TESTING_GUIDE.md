# 🚀 Flask API Testing Guide

## 📋 Overview

This guide covers testing the Flask API endpoints in your `api-test-server` project. The server runs on **port 5001** (changed from 5000 to avoid conflicts with Apple's AirPlay service).

## 🏃‍♂️ Quick Start

### Start the Server
```bash
# Activate virtual environment
source venv/bin/activate

# Start Flask app
python app.py
```

The server will be available at: `http://localhost:5001`

## 🔗 Available Endpoints

### 1. Health Check
- **URL**: `GET /`
- **Auth**: None required
- **Description**: Returns server status

```bash
curl http://localhost:5001/
```

### 2. Get All Users
- **URL**: `GET /users`
- **Auth**: **Required** (any Authorization header)
- **Description**: Returns list of all users

```bash
# With authorization (SUCCESS)
curl -H "Authorization: Bearer test-token" http://localhost:5001/users

# Without authorization (FAILS)
curl http://localhost:5001/users
```

### 3. Get Single User
- **URL**: `GET /users/<id>`
- **Auth**: None required
- **Description**: Returns specific user by ID

```bash
curl http://localhost:5001/users/1
```

### 4. Update User
- **URL**: `PUT /users/<id>`
- **Auth**: None required
- **Description**: Updates user information

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated"}' \
  http://localhost:5001/users/1
```

### 5. Get All Posts
- **URL**: `GET /posts`
- **Auth**: None required
- **Description**: Returns list of all posts

```bash
curl http://localhost:5001/posts
```

### 6. Create New Post
- **URL**: `POST /posts`
- **Auth**: None required
- **Description**: Creates a new post

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title": "My New Post"}' \
  http://localhost:5001/posts
```

### 7. Delete Post
- **URL**: `DELETE /posts/<id>`
- **Auth**: None required
- **Description**: Deletes a post by ID

```bash
curl -X DELETE http://localhost:5001/posts/1
```

## 🔐 Authorization Details

### How Authorization Works
- **Only `/users` endpoint requires authorization**
- **Any Authorization header value works** (token validation is not implemented)
- **Other endpoints** (`/`, `/posts`, `/users/<id>`) **don't require auth**

### Authorization Header Formats
```bash
# Bearer token (recommended)
curl -H "Authorization: Bearer your-token" http://localhost:5001/users

# Basic auth
curl -H "Authorization: Basic dGVzdA==" http://localhost:5001/users

# Custom format
curl -H "Authorization: Token my-secret" http://localhost:5001/users
```

### Testing Authorization
```bash
# This will work (returns user list)
curl -H "Authorization: Bearer test-token" http://localhost:5001/users

# This will fail (returns {"error": "Unauthorized"})
curl http://localhost:5001/users
```

## 🧪 Complete Test Suite

Run this complete test to verify all endpoints:

```bash
#!/bin/bash
echo "🧪 Testing Flask API on port 5001..."

# 1. Health check
echo "1. Health check..."
curl -s http://localhost:5001/ | jq .

# 2. Get users (with auth)
echo -e "\n2. Get users (with auth)..."
curl -s -H "Authorization: Bearer test-token" http://localhost:5001/users | jq .

# 3. Get users (without auth) - should fail
echo -e "\n3. Get users (without auth) - should fail..."
curl -s http://localhost:5001/users | jq .

# 4. Get single user
echo -e "\n4. Get single user..."
curl -s http://localhost:5001/users/1 | jq .

# 5. Update user
echo -e "\n5. Update user..."
curl -s -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated"}' \
  http://localhost:5001/users/1 | jq .

# 6. Get posts
echo -e "\n6. Get posts..."
curl -s http://localhost:5001/posts | jq .

# 7. Create post
echo -e "\n7. Create post..."
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"title": "My New Post"}' \
  http://localhost:5001/posts | jq .

# 8. Delete post
echo -e "\n8. Delete post..."
curl -s -X DELETE http://localhost:5001/posts/1 | jq .

echo -e "\n✅ Test suite complete!"
```

## 🚨 Troubleshooting

### Port Conflicts
- **Issue**: `curl http://localhost:5000/` returns `HTTP/1.1 403 Forbidden` from `AirTunes/860.7.1`
- **Solution**: Use port 5001 instead (already configured in `app.py`)

### Server Not Responding
```bash
# Check if server is running
ps aux | grep python

# Check what's using port 5001
lsof -i :5001

# Restart server
python app.py
```

### Authorization Issues
- **Problem**: Getting `{"error": "Unauthorized"}` on `/users`
- **Solution**: Add any Authorization header:
  ```bash
  curl -H "Authorization: Bearer any-token" http://localhost:5001/users
  ```

## 📁 Project Structure

```
api-test-server/
├── app.py                 # Flask application (runs on port 5001)
├── requirements.txt       # Python dependencies
├── venv/                 # Virtual environment
└── API_TESTING_GUIDE.md  # This file
```

## 🔧 Configuration

### Server Configuration
- **Port**: 5001 (configured in `app.py`)
- **Debug Mode**: Enabled
- **Host**: localhost

### Dependencies

#### Option 1: Full Requirements (Recommended)
```bash
# Install all dependencies including testing tools
pip install -r requirements.txt
```

#### Option 2: Minimal Requirements
```bash
# Install only essential packages
pip install -r requirements-minimal.txt
```

#### Option 3: Development Requirements
```bash
# Install development tools and full requirements
pip install -r requirements-dev.txt
```

#### Manual Installation
```bash
# Just Flask (minimal)
pip install flask

# Flask + testing
pip install flask requests pytest
```

### Requirements Files Available
- **`requirements.txt`** - Full requirements with testing, validation, and optional packages
- **`requirements-minimal.txt`** - Just Flask, requests, and pytest
- **`requirements-dev.txt`** - Development tools (formatters, linters, etc.)

## 🎯 Key Points

1. **Port 5001**: Server runs on port 5001 to avoid Apple AirPlay conflicts
2. **Authorization**: Only `/users` endpoint requires auth, any header value works
3. **JSON**: Use `-H "Content-Type: application/json"` for POST/PUT requests
4. **Virtual Environment**: Always activate `venv` before running the server
5. **Testing**: Use `jq` for pretty JSON output in curl commands

## 🚀 Next Steps

1. **Add more endpoints** as needed
2. **Implement proper token validation** for production use
3. **Add database integration** for persistent data
4. **Add comprehensive error handling**
5. **Create automated test suite** with pytest
