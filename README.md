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

`k3d cluster create --agents=2 -p 8080:80@loadbalancer --volume <full path>/kube_vol:/pod_data@all`

<h3> Deploying Apps and Respective services with ClusterIP exposed inside the cluster on port 80 </h3>

`cd deploys` <br>
`kubectl create -f nginx-emoji.yaml -f nginx-happy.yaml -f nginx-sad.yaml -f nginx-emoji-svc.yaml -f nginx-happy-svc.yaml -f nginx-sad-svc.yaml`

<h3> Install libnss-myhostname </h3>
It is used for using localhost as different domain names without adding it to the /etc/hosts
Ex: test.localhost, dev.localhost which points to localhost only.</br>
`apt-get install libnss-myhostname`

<h3> Creating Ingress resource to route to different services based on hostname </h3>

`cd ingress` <br>
`kubectl create -f ingress_host_based.yaml`

<h3> Access the apps </h3>

`curl emoji.localhost:8080` or `lynx  emoji.localhost:8080` <br>
`curl happy.emoji.localhost:8080` or `lynx  happy.emoji.localhost:8080`<br>
`curl sad.emoji.localhost:8080` or `lynx  sad.emoji.localhost:8080`<br>

Emojis :)
![image](https://user-images.githubusercontent.com/13021094/129744068-0198c6fd-3115-4a5d-87bc-9361882d72af.png)

Happy Emojis :D
![image](https://user-images.githubusercontent.com/13021094/129744194-ce1594fa-a6eb-4e3f-88c7-fd13a85bea58.png)

Sad Emojis :(
![image](https://user-images.githubusercontent.com/13021094/129744267-5abc65f9-fe76-4a42-94ef-a2542c8843a2.png)


<h1>Building Custome image and loading the image layer caches inside the cluster</h1>

`cd sample-python` <br>
`docker build . -t sample-python:1.0`<br>

`k3d image import sample-python:1.0`<br>

The above command will create a another container called k3d-tools which saves and wraps the image into tarball from local and push it to the nodes image volumes and run ctr import inside the container.

Create Pod, Service, Ingress<br>
`kubectl run flaskapp --image=sample-python:1.0`<br>
`cd ..`<br>
`kubectl create -f deploys/flask-app-svc.yaml -f ingress/flask-app-ing.yaml`<br>

`lynx localhost:8080`

