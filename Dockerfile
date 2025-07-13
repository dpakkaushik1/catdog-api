# Use Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Render
EXPOSE 5000

# Start the app using gunicorn (production-ready)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
