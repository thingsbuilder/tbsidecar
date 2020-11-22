default: build_dotnet

build_dotnet:
	eval $(minikube docker-env) && cd sidecar_dotnet && $(MAKE) stopc && $(MAKE) buildc
	eval $(minikube docker-env) && cd main_application && $(MAKE) stopc && $(MAKE) buildc

deploy_dotnet:
	-kubectl delete services sidecar-dotnet
	-kubectl delete deployment sidecar-dotnet
	-kubectl delete secret sidecar-secrets
	kubectl create secret generic sidecar-secrets --from-env-file=sidecar_dotnet/dev.env
	kubectl apply -f deployment_dotnet.yaml

build_python:
	eval $(minikube docker-env) && cd sidecar_python && $(MAKE) stopc && $(MAKE) buildc
	eval $(minikube docker-env) && cd main_application && $(MAKE) stopc && $(MAKE) buildc

deploy_python:
	-kubectl delete services sidecar_python
	-kubectl delete deployment sidecar_python
	-kubectl delete secret sidecar-secrets
	kubectl create secret generic sidecar-secrets --from-env-file=sidecar_python/dev.env
	kubectl apply -f deployment_python.yaml