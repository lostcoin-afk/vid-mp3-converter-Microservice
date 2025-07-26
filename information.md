We just use one instance of RabbitMQ however there can be more than that following the master-slave architecture where the data is persisted in just one server and the others read from that server.

we need persistence of RabbitMQ incase of failure of of some servers or some other server or client error so that the task can begin from where it was left off untill the entire task is comleted after which it can be removed from the queue or the server.

This configration of Rabbit is acheved using a StatefulSet kind which is one of the kubernetes object.


-----------Strong and Eventual Consistency--------------------
These topics arise from the superset topics of Sychronous and Asynchronous InterService Communication.
Wherein Sychronous means if one service is running then the client cant interact with any other service untill that service has completed its task For Example making an payment thorugh UPI.
Whereas in Asynchronous the user can use or interact with other services.

How is this Synchronous or Asycnrhonous related async/await in JS?



kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.1/deploy/static/provider/kind/deploy.yaml