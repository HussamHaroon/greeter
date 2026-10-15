# greeter

A tiny Python "greeter" web app built for the Git & Docker assignment. It uses only the
Python standard library (`http.server`) and serves a greeting with today's date on port 8000.

## Build and run with Docker

```bash
docker build -t greeter:1.0 .
docker run -d -p 8000:8000 greeter:1.0
```

Then open http://localhost:8000 in a browser.
