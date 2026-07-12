# ELK Setup

- create Folder Named ELK Demo
- move to that folder
- docker-compose.yml create (setup code given)
- app.py (for generating Logs)
- logstash.conf


```bash
docker compose up -d
docker ps
docker logs elasticsearch
docker logs kibana
# in logs when you see its available (It takes time to up)
# localhost:9200
# localhost:5601 (Kibana Dashboard)
# Generate Logs
python3 app.py
```
# Go to Kibana

- left side panel click on discover
- create Index Pattern
- type: python-logs-*
- ok (click on discover again)

## KQL
- just run it will show all
- filter by Log Level
- level : "ERROR"
- you can see 10 no of logs for Error
- filter by message:
    - message: "failed"