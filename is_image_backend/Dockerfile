FROM python:3.12.4-alpine


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /home/app
ENV APP_HOME=/home/app

WORKDIR ${APP_HOME}


# Create a user group 'xyzgroup'
RUN addgroup -S appgroup
# Create a user 'appuser' under 'xyzgroup'
RUN adduser -S -D -h ${APP_HOME} appuser appgroup

# Copy files
COPY . .

RUN chown -R appuser:appgroup ${APP_HOME}
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x run.sh

USER appuser

ENTRYPOINT [ "./run.sh" ]