FROM python:3.11-slim

#Installing the necessary dependencies 
RUN apt-get update && apt-get install -y --no-install-recommends \
    vim\
    unzip\
    curl\
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

#Set environment variables 
ENV PATH="/usr/lib/chromium-browser:${PATH}"
ENV CHROME_BIN="/usr/bin/chromium"
ENV CHROMEDRIVER_PATH="/usr/lib/chromium-browser/chromedriver" 

#Set working directory
WORKDIR /app

#copy files 
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

#Expose port 8000 for django
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
