# k3d-demo
k3d is a wrapper of k3s lightweight k8s distribution. We can spin up the cluster nodes as a docker container.

<h3>Clone this repository</h3>

`git clone https://github.com/udhayaprabakaran/k3d-demo.git`

<h3>Install kubectl</h3>
https://kubernetes.io/docs/tasks/tools/

<h3>Install K3d (Pre-Requisite: Docker)</h3>

`wget -q -O - https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash`

For specific version and more details visit: https://k3d.io/

<h3>Create a cluster with LB and Volume</h3>

Below will create a single master and 2 worker node cluster with LB for master and hosts local volume inside the all the nodes (containers)

`k3d cluster create --agents=2 -p 8081:80@loadbalancer --volume <hostpath>:/pod_data@agent[0] --volume <full path>/kube_vol:/pod_data@all`

<h3> Deploying Apps and Respective services with ClusterIP exposed inside the cluster on port 80 </h3>

`cd deploys`
`kubectl create -f nginx-emoji.yaml -f nginx-happy.yaml -f nginx-sad.yaml -f nginx-emoji-svc.yaml -f nginx-happy-svc.yaml -f nginx-sad-svc.yaml`

<h3> Install libnss-myhostname </h3>
It is used for using localhost as different domain names without adding it to the /etc/hosts
Ex: test.localhost, dev.localhost which points to localhost only.
`sudo apt-get install libnss-myhostname`

<h3> Creating Ingress resource to access the apps from outside </h3>

`cd ingress`
`kubectl create -f ingress_host_based.yaml`

<h3> Access the apps </h3>

`curl emoji.localhost:8080` or `lynx  emoji.localhost:8080`
`curl happy.emoji.localhost:8080` or `lynx  happy.emoji.localhost:8080`
`curl sad.emoji.localhost:8080` or `lynx  sad.emoji.localhost:8080`
 
