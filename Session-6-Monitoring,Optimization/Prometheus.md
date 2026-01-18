# Prometheus

- Powerfull Monitoring Tool

## Setup

[Download From this link](https://prometheus.io/download/)

- download .tar file for linux
- extract to downloads folder only
- go to wsl

```bash
mv /mnt/c/Users/Admin/Downloads/prometheus-3.9.1.linux-amd64 prometheus
# moving entire folder to prometheus folder under wsl /home/skills

cd prometheus
ls # check files

# edit prometheus.yml
nano prometheus.yml
# add below code
```

```yml
# my global config
global:
  scrape_interval: 15s

scrape_configs:

  - job_name: "prometheus"

    static_configs:
      - targets: ["localhost:9090"]
        labels:
          app: "prometheus"
```

- save file ctrl+o enter ctrl+x
- now let's start prometheus

```bash
./prometheus
```

- access it in browser 
![Result in Terminal](images/promethues-start.png)

[Prometheus Dashboard](http://localhost:9090)

[Check No of targets running](http://localhost:9090)

### Monitoring

![Monitoring using Query](images/query1.png)

![Graph Visualization](images/query2.png)

- type in query and check

- process_cpu_seconds_total
- process_virtual_memory_bytes