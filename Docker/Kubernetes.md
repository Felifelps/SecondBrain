[Base de estudo](https://docs.docker.com/get-started/orchestration/) + [Esse outro](https://kubernetes.io/docs/tutorials/kubernetes-basics/)

Pra ativar o kubernetes no windows, vá até a aba `Settings` do Docker Desktop. Lá, abra a opção `Kubernetes`. Basta selecionar a caixinha "Enable Kubernetes" e clicar em "Apply and Restart" lá em baixo. Talvez demore, mas quando funcionar, vai aparecer em verde lá em baixo, em verde, o símbolo que ele está rodando.

![Imagem do kubernetes rodando no docker desktop](https://i0.wp.com/charliedigital.com/wp-content/uploads/2021/07/2021-07-01_162032.png?resize=660%2C374&ssl=1)

O Docker Desktop instala automaticamente o `kubectl`, uma ferramenta de terminal que é útil pra mexer com o Kubernetes.
Aí é o seguinte, você descreve uma implementação Kubernetes (k8s) em um manifest, um arquivo .yaml pra criar e organizar esses containers. O nome pode ser qualquer um, o importante é estar na raiz do projeto e ser .yaml.

Vamos lá, cada projeto kubernetes gera um `cluster`, que possui três camadas: 
* `Control plane`: responsável por organizar tudo
* `Nodes`: máquinas físicas ou virtuais (cria e gerencia de acordo com o hardware disponível) que rodam vários Pods
* `Pods`: são as menores unidades dos clusters. É um grupo de um ou mais containers que compartilham armazenamento e rede, com especificações para rodar os mesmos.

# .yaml

Dentro do .yaml, você pode setar várias configurações diferentes, separando-as com `---`.
Cada configuração tem sempre as mesmas partes:
* `apiVersion`: diz qual a versão da api k8s que deve ler a configuração
* `kind`: indica que tipo de configuração é. Tem três principais:
	* `Pod`: cria um pod específico. [Ver](#Pod)
	* `Deployment`: permite criar vários Pods idênticos e organizá-los (configurar reação em caso de falha, entre outras possibilidades). [Ver](#Deployment)
	* `Service`: permite setar um método para a exposição dos containers dos pods à rede externa. [Ver](#Service)
 * `metadata`: especifica alguns dados da configuração, como nome, namespace e labels
 * `spec`: especifica todos os parametros da configuração
 
Vamos falar de cada tipo de configuração.
## Pod
Cria um pod isolado. Não é tão usado assim, por quê o [Deployment](#Deployment) organiza vários facilmente, e ele é o protagonista de apps em produção.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo
spec:
  containers:
  - name: testpod
    image: alpine:latest
    command: ["ping", "8.8.8.8"]
  - name: testdb
    image: mysql
```

No `metadata` você define o nome, o `kind` tem que ser Pod, e no `spec` você define os containers que você quer rodar no pod. 
Pra ver os Pods rodando no momento, use `kubectl get pods`.
## Deployment
A galinha dos ovos de ouro do Kubernetes. Essa instância organiza vários Pods e Nodes de seus containers, permitindo que eles sempre estejam no estado ideal que você definir aqui.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
   name: bb-demo
   namespace: default
spec:
   replicas: 1
   selector:
      matchLabels:
         bb: web
   template:
      metadata:
         labels:
            bb: web
      spec:
         containers:
            - name: bb-site
              image: getting-started
```

No exemplo acima, definimos o `kind` como `Deployment`, e colocamos em `metadata` o `name` como `bb-demo` e o `namespace`(forma de organizar sub-clusters virtuais dentro de um cluster) como o padrão.
Agora indo para o principal, em `spec`, setamos o número de pods criados como 1 em `replicas`(pode ser qualquer número). No `selector`, definimos em `matchLabels` que os Pods gerenciados por essa instância Deploymen serão aqueles que possuírem a label `bb` com o valor `web`.
Na seção `template`, definiremos um padrão para os Pods que criaremos. Os valores aqui usados são os mesmos usados em uma instância Pod. Na seção `metadata` dos Pods, definimos nas `labels` o par `bb: web`, permitindo que os Pods criados entrem no critério de uso definido no `selector`. Por fim, em `spec`, definimos os containers utilizados como fizemos na configuração [Pod](#Pod)

> Labels são pares chave/valor que são usados para divisão lógica dos Pods e objetos do kubernetes. São úteis nesse quesito.

Para ver os Deployments rodando use `kubectl get deployments`.
## Service
O tipo Service é bastante importante: ele configura a exposição dos Pods para a rede externa. E tem uma função muito útil no `type`: `LoadBalance`, que faz com que o Kubernetes divida o tráfego de rede entre os diversos Pods.

```yaml
# Outras configurações
---
apiVersion: v1
kind: Service
metadata:
   name: bb-entrypoint
   namespace: default
spec:
   type: NodePort
   selector:
      bb: web
   ports:
      - port: 3000
        targetPort: 3000
        nodePort: 30001
```

Mesma lógica dos anteriores, mas no `spec` diferencia. O `type` define como os Pods vão se relacionar com a rede. Tem quatro valores:
* `ClusterIP`: é o padrão. Expõe os Pods dentro do Cluster por meio de IPs internos.
* `NodePort`: permite linkar uma porta do Node numa porta externa. Usa a opção anterior por baixo dos panos.
* `LoadBalancer`: expõe o serviço pra rede externa usando um balanceador de tráfego externo. É necessário configurar, pois o K8s não tem um próprio.
* [`ExternalName`](https://kubernetes.io/docs/concepts/services-networking/service/#externalname): seta um nome DNS pro seu cluster.

Para ver os Services rodando use `kubectl get services`.
# Rodando

Para rodar um cluster K8s, crie seu arquivo de configuração, vá até a pasta onde ele se encontra e rode `kubectl apply -f my-file.yaml`(o -f é de *force*). 
Para destruir sua aplicação, rode `kubectl delete -f my-file.yaml`, também no diretório do arquivo.
Quando uma aplicação estiver rodando em produção, e você precisar atualizá-la ou escalá-la sem parar os serviços, você pode usar os comandos `set` e `scale`:
## set
Usado para atualizações rápidas e simples. Se a alteração for muito complexa, é recomendado alterar o arquivo .yaml. Tem vários usos:

1. **kubectl set image**:
   - **Resumo**: Atualiza a imagem de um contêiner em um recurso Kubernetes, como Deployment, StatefulSet ou DaemonSet.
   - **Exemplo**:
     ```
     kubectl set image deployment/nginx nginx=nginx:1.19
     ```

2. **kubectl set resources**:
   - **Resumo**: Atualiza os recursos (CPU e memória) atribuídos a um pod.
   - **Exemplo**:
     ```
     kubectl set resources deployment/nginx --limits=cpu=0.5,memory=256Mi --requests=cpu=0.2,memory=128Mi
     ```

3. **kubectl set env**:
   - **Resumo**: Atualiza variáveis de ambiente em pods.
   - **Exemplo**:
     ```
     kubectl set env deployment/nginx ENV_VAR1=value1 ENV_VAR2=value2
     ```

4. **kubectl set service**:
   - **Resumo**: Atualiza a especificação de um serviço Kubernetes.
   - **Exemplo**:
     ```
     kubectl set service my-service --external-ip=1.2.3.4 --selector=app=nginx
     ```

5. **kubectl set ingress**:
   - **Resumo**: Atualiza a especificação de um ingress Kubernetes.
   - **Exemplo**:
     ```
     kubectl set ingress my-ingress --annotation=nginx.ingress.kubernetes.io/rewrite-target=/ --path=/app
     ```

6. **kubectl set volume**:
   - **Resumo**: Adiciona, modifica ou remove volumes de um pod.
   - **Exemplo**:
     ```
     kubectl set volume deployment/nginx my-volume --add=configMap=my-configmap --remove=my-secret
     ```

Esses exemplos ilustram como cada comando pode ser usado para fazer atualizações específicas em recursos Kubernetes de maneira rápida e eficiente. Certifique-se de adaptar os exemplos às necessidades e configurações específicas do seu ambiente Kubernetes.
## scale
