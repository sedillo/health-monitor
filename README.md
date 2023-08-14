# healht-monitor

A monitoring solution for Docker hosts and containers with [Prometheus](https://prometheus.io/), [cAdvisor](https://github.com/google/cadvisor), and alerting with [AlertManager](https://github.com/prometheus/alertmanager).

## Install

Clone this repository on your Docker host, cd into dockprom directory and run compose up:

```bash
git clone https://github.com/sedillo/health-monitor.git
cd health-monitor
docker compose up
```

## Containers

* Prometheus `http://localhost:9090`
* AlertManager `http://localhost:9093`
* cAdvisor `http://localhost:8080`


