default: build_all

build_all:
	eval $(minikube docker-env) && cd sidecar && $(MAKE) stopc && $(MAKE) buildc
	eval $(minikube docker-env) && cd main_application && $(MAKE) stopc && $(MAKE) buildc

deploy:
	-kubectl delete services sidecar
	-kubectl delete deployment sidecar
	-kubectl delete secret sidecar-secrets
	kubectl create secret generic sidecar-secrets --from-env-file=sidecar/dev.env
	kubectl apply -f deployment.yaml