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

Below will create a single master and 2 worker node cluster with LB for master and hosts local volume inside the node (container)

`k3d cluster create --agents=2 -p 8081:80@loadbalancer --volume <hostpath>:/pod_data@agent[0] --volume <hostpath>:/pod_data@agent[1] --volume <hostpath>:/pod_data@server[0]`
