# How to setup two-tier application deployment on kubernetes cluster
  
## SetUp
- First clone the code to your machine
```bash
git clone https://github.com/yashsharma127/flask-careers-website-devops.git
```
- Move to k8s directory
```bash
cd flask-careers-website-devops/k8s
```
- Now, execute below commands one by one
```bash
kubectl apply -f two-tier-app-pod.yml
```
```bash
kubectl apply -f two-tier-app-deployment.yml
```
```bash
kubectl apply -f two-tier-app-svc.yml
```
```bash
kubectl apply -f mysql-deployment.yml
```
```bash
kubectl apply -f mysql-svc.yml
```
```bash
kubectl apply -f mysql-pv.yml
```
```bash
kubectl apply -f mysql-pvc.yml
```
