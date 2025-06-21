
## Namespaces

# Para saber los espacios creados
kubectl get namespaces
# Para crear un grupo de kubernetes (en minúsculas)
kubectl create namespace <nombre>
# Para borrarlo
kubectl delete namespace <nombre>
# Para crear todo lo del directorio
kubectl apply -f <directorio>
# Para borrar todo lo del directorio
kubectl delete -f <directorio> --force
# Para crear desde fichero
kubectl apply -f <nombre yaml>
# Si parto de un dockerfile
docker imagen build <ruta dokerfile> -t <nombre imagen>

## Pods

# Para ver los pods de un namespace
kubectl -n <namespace> get pods
# Para ver lo que hemos creado
kubectl -n <namespace> describe pod <nombre-pod>
# Para borrar pods
kubectl -n <namespace> delete pod <nombre-pod>
# Entrar en un pod
kubectl exec -it <pod> -- /bin/sh
# Para ver los logs de un pod
kubectl logs <pod>
kubectl describe pods/sqls-input-deployment-879b7c6f9-gnc8x
# Para ver los logs de un pod de forma continua
kubectl logs -f <pod>

## Deployments

# Para ver que pasa con los nodos (PENDING)
kubectl get events -n namespace

## Minikube

# Evantamos minukube, esto levanta el cluster de kubernetes
minikube start

# Forwarding de puertos
kubectl -n cloudnamespace port-forward svc/belts-water-addition-factor-service 8080:80



# Create
minikube start -p cloudcluster
minikube start -p cloudcluster --driver=docker
# set profile
minikube profile cloudcluster
# Add nodes
minikube node add
# Ver profiles
minikube profile list


### Subir imagenes
https://minikube.sigs.k8s.io/docs/handbook/registry/
# Se necesita el registriy de minikube
minikube addons enable registry
# Dos consolas para hacer forwarding the esto y habilitar un punto de entrada
kubectl port-forward --namespace kube-system service/registry 5000:80
docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:host.docker.internal:5000"
# Si las imagenes estan subidas aparece aqui
http://localhost:5000/v2/_catalog
# Se sube asi
docker tag cooling_drum_water_predictor:0.1 localhost:5000/cooling_drum_water_predictor:0.1
docker push localhost:5000/cooling_drum_water_predictor:0.1

# yo he usado esto en linux (usar el docker de minikube)
eval $(minikube docker-env)



kubectl config set-context --current --namespace=cloudnamespace

minikube mount /home/asier/Monolith_to_microservices/Cluster/src/DB/generation_files/sqls/:/db_files/sqls --uid=10001
minikube mount /home/asier/Monolith_to_microservices/Cluster/src/Kafka/generation_files/:/kafka --uid=1000
minikube mount /home/asier/Monolith_to_microservices/Cluster/src/PDagents/generation_files/data/:/input --uid=1000
minikube mount /home/asier/Monolith_to_microservices/Cluster/src/DB/generation_files/mysql/:/db_files/mysql --uid=1000





kafka-topics --bootstrap-server localhost:9092 --list

kafka-topics --bootstrap-server localhost:9092 --describe --topic chemical_composition_file

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
