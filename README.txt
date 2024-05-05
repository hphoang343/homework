-- Homework
===== Technical task =========
- Kubernetes
- ELK
- Grafana + Prometheus
- Ansible
- Helm 
- Nginx for LB
===== Infrastructure requirement =====
- Kubernetes: deploy with rke (on-permiss deploy)
- Docker hub: store images
- Ansible 
================= install =============
* services 
 - PRD: deploy database on kubernetes not good idea. If you can, we can deploy replication/ clusters architect (cluster/percona/mariadb ...).
 In this case, i use hostpath for store data of database (in production, you)

	cd deploy/ansible
	ansible-playbook main.yml


* Install Prometheus + Grafana for monitoring 
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install monitoring prometheus-community/kube-prometheus-stack

* install ELK for log (install in server not in kubernetes because it's not good for Production)
	
 Reference: https://www.elastic.co/guide/en/elastic-stack/current/installing-elastic-stack.html
 
* Security
    Code : Sonaque
    Network: Use services Discovery of kubernetes .(all service communication with in ternal network and service name , External/ User access via Ingress/API manager)
    Container: trivy (aqua)
    CIS
    Config application: use secret or config map
    
* Scale:
  - Sevices Scale: 
    + Method 1: increate replication 1 to N in deployment file
    + Method 2: use HPA
  - Sever scale: add node to kubernetes cluster
  
