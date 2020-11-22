# tbsidecar
Exemplo de utilização do Design Pattern Sidecar

**sidecar_python e sidecar_dotnet**: são dois exemplos distindos de servidor gRPC rodando como sidecar

**main_application**: aplicação client gRPC em Python que pode usar um dos dois sidecar acima.

**deployment_python** cria um deployment contendo um container sidecar_python e outro main_application no mesmo pod. 

**deployment_dotnet.yaml** cria um deployment contendo um container sidecar_dotnet e outro main_application no mesmo pod.

Um Makefile na raíz do projeto permite fazer o build e deployment em um "cluster" Minikube

Execute:

Para o deployment_dotnet:

make build_dotnet   (para fazer o build)
make deploy_dotnet  (para fazer o deployment) 

Para o deployment_python:

make build_python   (para fazer o build)
make deploy_python  (para fazer o deployment)
 