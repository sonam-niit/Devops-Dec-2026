# Monitor Python Application using Prometheus

1. Setup Python app as shown here
2. Setup Prometheus.yml as shown here
3. Setup docker-Compose.yml: having 3 services

```bash
docker compose up -d --build
# build needs incase you required to rebuild your image
# docker logs (Incase of errors)
```

## Verify using links

1. localhost:5000 
2. localhost:5000/metrics
3. localhost:9090
4. localhost:9090/targets
5. localhost:3000
    - access using default password: admin/admin

- run sample sample queries:
    - http_request_total 
    - refresh localhost:5000 - check query again to see no of request increase
    - rate(http_request_total[5m])

- to stop all running services

```bash
docker compose down
```