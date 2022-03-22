FROM python:3

ENV TZ Asia/Hong_Kong
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
    
COPY . .

CMD ["mabinogi_discord_bot.py"]
ENTRYPOINT ["python3"]