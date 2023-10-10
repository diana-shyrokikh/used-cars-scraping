FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get -y install libpq-dev gcc gnupg
RUN apt-get install -y wget curl unzip libglib2.0-0  \
    libnss3 libx11-6 libx11-xcb1 libxcb1 libxcomposite1  \
    libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2  \
    libxrender1 libxss1 libxtst6 libappindicator1 libasound2  \
    libatk-bridge2.0-0 libatk1.0-0 libcairo2 libcups2 libdbus-1-3  \
    libexpat1 libfontconfig1 libgbm1 libgtk-3-0 libnspr4 libnss3  \
    libpango-1.0-0 libxcomposite1 libxcursor1 libxdamage1 libxfixes3  \
    libxi6 libxrandr2 libxrender1 libxss1 libxtst6 libappindicator3-1  \
    libatk-bridge2.0-0 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4  \
    libnss3 libxss1 libxtst6 xdg-utils

RUN apt-get install -y fonts-liberation libu2f-udev libvulkan1

RUN curl -LO https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.149/linux64/chrome-linux64.zip && \
    unzip chrome-linux64.zip -d /opt && \
    rm chrome-linux64.zip && \
    ln -s /opt/chrome-linux64/chrome /usr/bin/chrome

RUN curl -LO https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.149/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip -d /usr/local/bin && \
    rm chromedriver-linux64.zip

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN adduser \
    --disabled-password \
    --no-create-home \
    user

RUN chown -R user:user /app/
RUN chown -R user:user /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver-linux64/chromedriver

USER user
