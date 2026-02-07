How to deploy new things in the k8s cluster

- First check the bash script which is being used for deployment
- Build the docker image with the new code, for example:
-  sudo docker build -q -t data-crawling:$VERSION -f ./deploy/ai-bubbles/docker/Dockerfile.data-crawling .

Q is for quiet building if you want to see the logs of building then remove that

export VERSION="v1.0.0" export the version for that instance in before deploying 

After building the image tag that image to latest or anything else:
sudo docker tag data-crawling:$VERSION data-crawling:latest


Export the cluster name export CLUSTER_NAME="ai-bubbles”… pretty much optional can give it directly


We are using kind for cluster management so after building and tagging load the new image in the cluster : sudo kind load docker-image data-crawling:latest --name $CLUSTER_NAME


Check all the nodes inside the cluster: sudo kind get nodes --name $CLUSTER_NAME


After loading the new image the depreciated pod is still there in the cluster so now just delete the pod because for the cluster configuration when it set to deployment type that its gonna deploy a new pod if the existing pod is being destroyed so just delete it, it will spawn again

Now check the changes inside the pod

For airflow deployment 

Run the sync dag from the deployment script


Some other commands:


Kubectl exec -it pod_name — bash —> to get into the pod

Kubectl cp pod_name:path local path —> if you want to copy something from pod to local