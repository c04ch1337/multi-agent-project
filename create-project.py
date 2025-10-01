#!/usr/bin/env python3
"""
Multi-Agent AI System - Complete Project Setup Script
Creates full GitHub repository with ALL files and content

Usage: python3 create-project.py [project-name]
"""

import os
import sys
import argparse
from pathlib import Path
import textwrap


class ProjectCreator:
    def __init__(self, project_name: str, base_path: str = "."):
        self.project_name = project_name
        self.base_path = Path(base_path) / project_name
        self.files_created = []
        self.dirs_created = []
    
    def create(self):
        print(f"🚀 Creating project: {self.project_name}")
        print(f"📁 Location: {self.base_path.absolute()}\n")
        
        self._create_directories()
        self._create_all_files()
        self._print_summary()
    
    def _create_directories(self):
        """Create all project directories"""
        dirs = [
            "scripts", "docs", "notebooks", "logs",
            "infrastructure/kubernetes", "infrastructure/docker", "infrastructure/istio",
            "agents/src/common", "agents/src/orchestrator", "agents/src/workers",
            "agents/configs", "agents/protos", "agents/kubernetes",
            "data/models", "data/vector_db", "data/checkpoints", "data/postgres", "data/redis",
            "monitoring/prometheus", "monitoring/grafana/dashboards", "monitoring/grafana/datasources",
            "tests/unit", "tests/integration", "tests/e2e",
            "tools/financial", "tools/common",
        ]
        
        for dir_path in dirs:
            full_path = self.base_path / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            self.dirs_created.append(dir_path)
            
            if dir_path.startswith('data/') or dir_path == 'logs':
                (full_path / '.gitkeep').touch()
    
    def _write_file(self, path: str, content: str):
        """Write content to file"""
        full_path = self.base_path / path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        content = textwrap.dedent(content).strip() + '\n'
        
        with open(full_path, 'w') as f:
            f.write(content)
        
        self.files_created.append(path)
        
        if path.startswith('scripts/') and path.endswith('.sh'):
            os.chmod(full_path, 0o755)
    
    def _create_all_files(self):
        """Create ALL project files with complete content"""
        
        # === ROOT FILES ===
        self._create_readme()
        self._create_gitignore()
        self._create_license()
        self._create_requirements()
        self._create_env_example()
        self._create_makefile()
        
        # === SETUP SCRIPTS ===
        self._create_setup_scripts()
        self._create_utility_scripts()
        
        # === INFRASTRUCTURE ===
        self._create_storage_class()
        self._create_postgresql()
        self._create_qdrant()
        self._create_redis()
        self._create_prometheus()
        self._create_grafana()
        self._create_nvidia_dcgm()
        
        # === AGENT CODE ===
        self._create_proto_file()
        self._create_agent_config()
        self._create_agent_code()
        self._create_financial_tools()
        self._create_dockerfile()
        self._create_agent_manifest()
        
        # === MONITORING ===
        self._create_grafana_dashboard()
        
        # === DOCUMENTATION ===
        self._create_docs()
        
        # === TESTS ===
        self._create_tests()
    
    def _create_readme(self):
        self._write_file('README.md', '''
        # Multi-Agent AI System
        
        Production-ready multi-agent AI system with GPU acceleration on local Kubernetes.
        
        ## Technology Stack
        
        - **Kubernetes**: K3s (lightweight)
        - **Service Mesh**: Istio (automatic mTLS)
        - **Agent Framework**: LangGraph (stateful workflows)
        - **Vector DB**: Qdrant
        - **State Storage**: PostgreSQL
        - **Cache**: Redis
        - **Monitoring**: Prometheus + Grafana
        - **Communication**: gRPC
        
        ## Hardware Requirements
        
        - 4x NVIDIA GTX 1060 (6GB each)
        - 32GB+ RAM
        - 500GB+ SSD
        - Ubuntu 22.04 LTS
        
        ## Quick Start
        
        ```bash
        # One-command setup
        sudo ./scripts/setup-phase1.sh
        
        # After reboot
        sudo ./scripts/setup-phase1-part2.sh
        
        # Test
        make test
        ```
        
        ## Access Dashboards
        
        ```bash
        make port-forward
        ```
        
        - Grafana: http://localhost:3000 (admin/admin)
        - Prometheus: http://localhost:9090
        - Qdrant: http://localhost:6333/dashboard
        
        ## Documentation
        
        - [Installation](docs/INSTALLATION.md)
        - [Operations](docs/OPERATIONS.md)
        - [Troubleshooting](docs/TROUBLESHOOTING.md)
        
        ## Project Structure
        
        ```
        multi-agent-system/
        ├── agents/              # Agent code & configs
        ├── infrastructure/      # K8s manifests
        ├── monitoring/          # Prometheus/Grafana
        ├── scripts/            # Setup scripts
        ├── tools/              # Agent tools
        └── docs/               # Documentation
        ```
        ''')
    
    def _create_gitignore(self):
        self._write_file('.gitignore', '''
        __pycache__/
        *.py[cod]
        venv/
        env/
        .env
        .env.local
        data/models/*
        data/vector_db/*
        data/checkpoints/*
        data/postgres/*
        data/redis/*
        !data/*/.gitkeep
        logs/*.log
        *.log
        .vscode/
        .idea/
        .ipynb_checkpoints/
        test_results_*.json
        .pytest_cache/
        .coverage
        *.kubeconfig
        .terraform/
        *.tfstate
        *.pem
        *.key
        ''')
    
    def _create_license(self):
        self._write_file('LICENSE', '''
        MIT License
        
        Copyright (c) 2024 Multi-Agent AI System
        
        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:
        
        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.
        
        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
        ''')
    
    def _create_requirements(self):
        self._write_file('requirements.txt', '''
        langgraph==0.2.16
        langchain==0.1.0
        langchain-openai==0.0.5
        langchain-core==0.1.10
        psycopg2-binary==2.9.9
        redis==5.0.1
        qdrant-client==1.7.0
        yfinance==0.2.33
        numpy==1.24.3
        pandas==2.0.3
        grpcio==1.60.0
        grpcio-tools==1.60.0
        protobuf==4.25.1
        prometheus-client==0.19.0
        python-dotenv==1.0.0
        pydantic==2.5.0
        requests==2.31.0
        pytest==7.4.3
        pytest-asyncio==0.21.1
        ''')
    
    def _create_env_example(self):
        self._write_file('.env.example', '''
        OPENAI_API_KEY=your_openai_key_here
        ANTHROPIC_API_KEY=your_anthropic_key_here
        LANGCHAIN_TRACING_V2=true
        LANGCHAIN_API_KEY=your_langsmith_key_here
        LANGCHAIN_PROJECT=multi-agent-local
        POSTGRES_HOST=postgres.infrastructure.svc.cluster.local
        POSTGRES_PORT=5432
        POSTGRES_USER=agentuser
        POSTGRES_PASSWORD=agentpass123
        POSTGRES_DB=agent_state
        REDIS_HOST=redis.infrastructure.svc.cluster.local
        REDIS_PORT=6379
        QDRANT_HOST=qdrant.infrastructure.svc.cluster.local
        QDRANT_PORT=6333
        CUDA_VISIBLE_DEVICES=0,1,2,3
        DATA_DIR=/data
        LOG_LEVEL=INFO
        ''')
    
    def _create_makefile(self):
        self._write_file('Makefile', '''
        .PHONY: help install setup deploy test clean
        
        help:
        \t@echo "Multi-Agent AI System Commands:"
        \t@echo "  make install       - Install prerequisites"
        \t@echo "  make setup         - Setup K3s cluster"
        \t@echo "  make deploy        - Deploy agents"
        \t@echo "  make test          - Run tests"
        \t@echo "  make status        - Show status"
        \t@echo "  make port-forward  - Forward services"
        \t@echo "  make clean         - Clean up"
        
        install:
        \t./scripts/install-prerequisites.sh
        
        setup:
        \t./scripts/install-k3s.sh
        \t./scripts/deploy-infrastructure.sh
        
        deploy:
        \t./scripts/build-agent.sh financial-analyst
        \t./scripts/deploy-agent.sh financial-analyst
        
        test:
        \tpython tests/test_agent_basic.py
        
        status:
        \tkubectl get nodes
        \tkubectl get pods --all-namespaces
        
        port-forward:
        \t./scripts/port-forward-services.sh
        
        clean:
        \tkubectl delete namespace agents infrastructure monitoring --ignore-not-found
        ''')
    
    def _create_setup_scripts(self):
        # Main setup script
        self._write_file('scripts/setup-phase1.sh', '''
        #!/bin/bash
        set -e
        
        echo "Multi-Agent System - Phase 1 Setup"
        echo "==================================="
        
        if [ "$EUID" -ne 0 ]; then 
            echo "Please run with sudo"
            exit 1
        fi
        
        ACTUAL_USER=${SUDO_USER:-$USER}
        echo "Installing for user: $ACTUAL_USER"
        
        ./scripts/install-prerequisites.sh
        
        echo ""
        echo "System needs to reboot for NVIDIA drivers"
        echo "After reboot run: sudo ./scripts/setup-phase1-part2.sh"
        read -p "Reboot now? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            reboot
        fi
        ''')
        
        self._write_file('scripts/setup-phase1-part2.sh', '''
        #!/bin/bash
        set -e
        
        echo "Phase 1 Setup - Part 2"
        nvidia-smi || exit 1
        
        ./scripts/install-k3s.sh
        ./scripts/deploy-infrastructure.sh
        ./scripts/build-agent.sh financial-analyst
        ./scripts/deploy-agent.sh financial-analyst
        
        echo "Phase 1 Complete!"
        echo "Test: python tests/test_agent_basic.py"
        ''')
        
        self._write_file('scripts/install-prerequisites.sh', '''
        #!/bin/bash
        set -e
        
        echo "Installing prerequisites..."
        apt update && apt upgrade -y
        apt install -y build-essential git curl wget python3.11 python3-pip
        
        # Docker
        curl -fsSL https://get.docker.com | sh
        usermod -aG docker $SUDO_USER
        
        # NVIDIA drivers
        apt install -y linux-headers-$(uname -r)
        wget -q https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
        dpkg -i cuda-keyring_1.1-1_all.deb
        apt update
        apt install -y nvidia-driver-535 cuda-toolkit-12-3
        
        # NVIDIA Container Toolkit
        distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
        curl -s -L https://nvidia.github.io/libnvidia-container/gpgkey | apt-key add -
        curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \\
          tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
        apt update
        apt install -y nvidia-container-toolkit
        nvidia-ctk runtime configure --runtime=docker
        systemctl restart docker
        
        echo "Prerequisites installed. Reboot required."
        ''')
        
        self._write_file('scripts/install-k3s.sh', '''
        #!/bin/bash
        set -e
        
        echo "Installing K3s..."
        
        curl -sfL https://get.k3s.io | sh -s - \\
          --write-kubeconfig-mode 644 \\
          --disable traefik \\
          --disable servicelb
        
        sleep 10
        mkdir -p $HOME/.kube
        cp /etc/rancher/k3s/k3s.yaml $HOME/.kube/config
        chown $USER:$USER $HOME/.kube/config
        
        snap install kubectl --classic
        
        kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.14.3/nvidia-device-plugin.yml
        sleep 10
        
        kubectl create namespace agents
        kubectl create namespace infrastructure
        kubectl create namespace monitoring
        kubectl create namespace istio-system
        
        # Install Istio
        curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.20.2 sh -
        cd istio-1.20.2
        ./bin/istioctl install --set profile=minimal -y
        kubectl label namespace agents istio-injection=enabled --overwrite
        cd ..
        
        echo "K3s installed successfully!"
        kubectl get nodes
        ''')
        
        self._write_file('scripts/deploy-infrastructure.sh', '''
        #!/bin/bash
        set -e
        
        echo "Deploying infrastructure..."
        
        kubectl apply -f infrastructure/kubernetes/storage-class.yaml
        kubectl apply -f infrastructure/kubernetes/postgresql.yaml
        kubectl apply -f infrastructure/kubernetes/qdrant.yaml
        kubectl apply -f infrastructure/kubernetes/redis.yaml
        kubectl apply -f infrastructure/kubernetes/prometheus.yaml
        kubectl apply -f infrastructure/kubernetes/grafana.yaml
        kubectl apply -f infrastructure/kubernetes/nvidia-dcgm-exporter.yaml
        
        echo "Waiting for pods to be ready..."
        kubectl wait --for=condition=ready pod -l app=postgres -n infrastructure --timeout=300s
        kubectl wait --for=condition=ready pod -l app=qdrant -n infrastructure --timeout=300s
        kubectl wait --for=condition=ready pod -l app=redis -n infrastructure --timeout=300s
        
        echo "Infrastructure deployed!"
        ''')
        
        self._write_file('scripts/build-agent.sh', '''
        #!/bin/bash
        set -e
        
        AGENT_NAME=${1:-financial-analyst}
        echo "Building agent: $AGENT_NAME"
        
        # Generate protobuf
        python3 -m grpc_tools.protoc \\
          -I agents/protos \\
          --python_out=agents/src/common \\
          --grpc_python_out=agents/src/common \\
          agents/protos/agent_service.proto
        
        docker build -t ${AGENT_NAME}:latest -f agents/Dockerfile .
        echo "Agent built successfully!"
        ''')
        
        self._write_file('scripts/deploy-agent.sh', '''
        #!/bin/bash
        set -e
        
        AGENT_NAME=${1:-financial-analyst}
        echo "Deploying agent: $AGENT_NAME"
        
        kubectl apply -f agents/kubernetes/${AGENT_NAME}.yaml
        kubectl wait --for=condition=ready pod -l app=$AGENT_NAME -n agents --timeout=300s
        
        echo "Agent deployed!"
        kubectl get pods -n agents
        ''')
    
    def _create_utility_scripts(self):
        self._write_file('scripts/port-forward-services.sh', '''
        #!/bin/bash
        
        echo "Starting port forwarding..."
        pkill -f "kubectl port-forward" || true
        
        kubectl port-forward -n monitoring svc/grafana 3000:3000 &
        kubectl port-forward -n monitoring svc/prometheus 9090:9090 &
        kubectl port-forward -n infrastructure svc/qdrant 6333:6333 &
        kubectl port-forward -n agents svc/financial-analyst 50051:50051 &
        
        sleep 2
        echo ""
        echo "Services available:"
        echo "  Grafana: http://localhost:3000 (admin/admin)"
        echo "  Prometheus: http://localhost:9090"
        echo "  Qdrant: http://localhost:6333/dashboard"
        echo "  Agent gRPC: localhost:50051"
        echo ""
        echo "Press Ctrl+C to stop"
        wait
        ''')
        
        self._write_file('scripts/quick-test.sh', '''
        #!/bin/bash
        
        echo "Quick System Test"
        echo "================="
        
        echo "1. Cluster status:"
        kubectl get nodes
        
        echo ""
        echo "2. GPU availability:"
        kubectl get nodes -o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia\\.com/gpu
        
        echo ""
        echo "3. All pods:"
        kubectl get pods --all-namespaces
        
        echo ""
        echo "4. Agent health:"
        kubectl exec -n agents deployment/financial-analyst -c agent -- \\
          python3 -c "print('Agent healthy')" 2>/dev/null || echo "Agent not ready"
        
        echo ""
        echo "Test complete!"
        ''')
    
    def _create_storage_class(self):
        self._write_file('infrastructure/kubernetes/storage-class.yaml', '''
        apiVersion: v1
        kind: PersistentVolume
        metadata:
          name: local-pv-postgres
        spec:
          storageClassName: local-storage
          capacity:
            storage: 20Gi
          accessModes:
            - ReadWriteOnce
          persistentVolumeReclaimPolicy: Retain
          hostPath:
            path: "/data/postgres"
            type: DirectoryOrCreate
        ---
        apiVersion: v1
        kind: PersistentVolume
        metadata:
          name: local-pv-qdrant
        spec:
          storageClassName: local-storage
          capacity:
            storage: 30Gi
          accessModes:
            - ReadWriteOnce
          persistentVolumeReclaimPolicy: Retain
          hostPath:
            path: "/data/qdrant"
            type: DirectoryOrCreate
        ---
        apiVersion: v1
        kind: PersistentVolume
        metadata:
          name: local-pv-redis
        spec:
          storageClassName: local-storage
          capacity:
            storage: 10Gi
          accessModes:
            - ReadWriteOnce
          persistentVolumeReclaimPolicy: Retain
          hostPath:
            path: "/data/redis"
            type: DirectoryOrCreate
        ---
        apiVersion: storage.k8s.io/v1
        kind: StorageClass
        metadata:
          name: local-storage
        provisioner: kubernetes.io/no-provisioner
        volumeBindingMode: WaitForFirstConsumer
        ''')
    
    def _create_postgresql(self):
        self._write_file('infrastructure/kubernetes/postgresql.yaml', '''
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
          name: postgres-pvc
          namespace: infrastructure
        spec:
          storageClassName: local-storage
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 20Gi
        ---
        apiVersion: v1
        kind: Secret
        metadata:
          name: postgres-secret
          namespace: infrastructure
        type: Opaque
        stringData:
          POSTGRES_USER: agentuser
          POSTGRES_PASSWORD: agentpass123
          POSTGRES_DB: agent_state
        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: postgres
          namespace: infrastructure
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: postgres
          template:
            metadata:
              labels:
                app: postgres
            spec:
              containers:
              - name: postgres
                image: postgres:16
                ports:
                - containerPort: 5432
                envFrom:
                - secretRef:
                    name: postgres-secret
                volumeMounts:
                - name: postgres-storage
                  mountPath: /var/lib/postgresql/data
                resources:
                  requests:
                    memory: "2Gi"
                    cpu: "500m"
                  limits:
                    memory: "4Gi"
                    cpu: "1000m"
              volumes:
              - name: postgres-storage
                persistentVolumeClaim:
                  claimName: postgres-pvc
        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: postgres
          namespace: infrastructure
        spec:
          selector:
            app: postgres
          ports:
          - port: 5432
            targetPort: 5432
          type: ClusterIP
        ''')
    
    def _create_qdrant(self):
        self._write_file('infrastructure/kubernetes/qdrant.yaml', '''
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
          name: qdrant-pvc
          namespace: infrastructure
        spec:
          storageClassName: local-storage
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 30Gi
        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: qdrant
          namespace: infrastructure
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: qdrant
          template:
            metadata:
              labels:
                app: qdrant
            spec:
              containers:
              - name: qdrant
                image: qdrant/qdrant:v1.7.4
                ports:
                - containerPort: 6333
                - containerPort: 6334
                volumeMounts:
                - name: qdrant-storage
                  mountPath: /qdrant/storage
                resources:
                  requests:
                    memory: "2Gi"
                    cpu: "500m"
                  limits:
                    memory: "4Gi"
                    cpu: "1000m"
              volumes:
              - name: qdrant-storage
                persistentVolumeClaim:
                  claimName: qdrant-pvc
        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: qdrant
          namespace: infrastructure
        spec:
          selector:
            app: qdrant
          ports:
          - port: 6333
            targetPort: 6333
            name: http
          - port: 6334
            targetPort: 6334
            name: grpc
          type: ClusterIP
        ''')
    
    def _create_redis(self):
        self._write_file('infrastructure/kubernetes/redis.yaml', '''
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
          name: redis-pvc
          namespace: infrastructure
        spec:
          storageClassName: local-storage
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 10Gi
        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: redis
          namespace: infrastructure
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: redis
          template:
            metadata:
              labels:
                app: redis
            spec:
              containers:
              - name: redis
                image: redis:7.2-alpine
                ports:
                - containerPort: 6379
                volumeMounts:
                - name: redis-storage
                  mountPath: /data
                resources:
                  requests:
                    memory: "1Gi"
                    cpu: "500m"
                  limits:
                    memory: "2Gi"
                    cpu: "1000m"
              volumes:
              - name: redis-storage
                persistentVolumeClaim:
                  claimName: redis-pvc
        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: redis
          namespace: infrastructure
        spec:
          selector:
            app: redis
          ports:
          - port: 6379
            targetPort: 6379
          type: ClusterIP
        ''')
    
    def _create_prometheus(self):
        self._write_file('infrastructure/kubernetes/prometheus.yaml', '''
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: prometheus-config
          namespace: monitoring
        data:
          prometheus.yml: |
            global:
              scrape_interval: 15s
            scrape_configs:
              - job_name: 'kubernetes-pods'
                kubernetes_sd_configs:
                - role: pod
                relabel_configs:
                - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
                  action: keep
                  regex: true
        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: prometheus
          namespace: monitoring
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: prometheus
          template:
            metadata:
              labels:
                app: prometheus
            spec:
              containers:
              - name: prometheus
                image: prom/prometheus:v2.48.0
                ports:
                - containerPort: 9090
                volumeMounts:
                - name: config
                  mountPath: /etc/prometheus
                resources:
                  requests:
                    memory: "1Gi"
                    cpu: "500m"
              volumes:
              - name: config
                configMap:
                  name: prometheus-config
        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: prometheus
          namespace: monitoring
        spec:
          selector:
            app: prometheus
          ports:
          - port: 9090
            targetPort: 9090
          type: ClusterIP
        ''')
    
    def _create_grafana(self):
        self._write_file('infrastructure/kubernetes/grafana.yaml', '''
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: grafana
          namespace: monitoring
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: grafana
          template:
            metadata:
              labels:
                app: grafana
            spec:
              containers:
              - name: grafana
                image: grafana/grafana:10.2.2
                ports:
                - containerPort: 3000
                env:
                - name: GF_SECURITY_ADMIN_PASSWORD
                  value: admin
                resources:
                  requests:
                    memory: "512Mi"
                    cpu: "250m"
        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: grafana
          namespace: monitoring
        spec:
          selector:
            app: grafana
          ports:
          - port: 3000
            targetPort: 3000
            nodePort: 30300
          type: NodePort
        ''')
    
    def _create_nvidia_dcgm(self):
        self._write_file('infrastructure/kubernetes/nvidia-dcgm-exporter.yaml', '''
        apiVersion: apps/v1
        kind: DaemonSet
        metadata:
          name: nvidia-dcgm-exporter
          namespace: monitoring
        spec:
          selector:
            matchLabels:
              app: nvidia-dcgm-exporter
          template:
            metadata:
              labels:
                app: nvidia-dcgm-exporter
              annotations:
                prometheus.io/scrape: "true"
                prometheus.io/port: "9400"
            spec:
              hostNetwork: true
              containers:
              - name: exporter
                image: nvidia/dcgm-exporter:3.3.0-3.2.0-ubuntu22.04
                ports:
                - containerPort: 9400
                securityContext:
                  privileged: true
                resources:
                  requests:
                    nvidia.com/gpu: 4
                  limits:
                    nvidia.com/gpu: 4
        ''')
    
    def _create_proto_file(self):
        self._write_file('agents/protos/agent_service.proto', '''
        syntax = "proto3";
        
        package agent;
        
        service AgentCommunication {
          rpc ExecuteTask(TaskRequest) returns (TaskResponse);
          rpc GetStatus(StatusRequest) returns (StatusResponse);
          rpc HealthCheck(HealthRequest) returns (HealthResponse);
        }
        
        message TaskRequest {
          string task_id = 1;
          string task_description = 2;
          map<string, string> context = 3;
          string priority = 4;
        }
        
        message TaskResponse {
          string task_id = 1;
          string status = 2;
          string result = 3;
          repeated string tools_used = 4;
          int64 duration_ms = 5;
          string error_message = 6;
        }
        
        message StatusRequest {
          string agent_id = 1;
        }
        
        message StatusResponse {
          string agent_id = 1;
          string agent_name = 2;
          string status = 3;
          string current_task = 4;
          int64 tasks_completed = 5;
          map<string, string> metadata = 6;
        }
        
        message HealthRequest {}
        
        message HealthResponse {
          bool healthy = 1;
          string message = 2;
        }
        ''')
    
    def _create_agent_config(self):
        self._write_file('agents/configs/financial_analyst.json', '''
        {
          "agent": {
            "id": "financial-analyst-001",
            "name": "Financial Analyst Agent",
            "type": "financial_analysis",
            "version": "1.0.0"
          },
          "system_prompt": "You are a Senior Financial Analyst.",
          "model": {
            "provider": "openai",
            "model_name": "gpt-4-turbo-preview",
            "temperature": 0.7,
            "max_tokens": 4096
          },
          "tools": [
            {"name": "calculator", "enabled": true}
          ],
          "monitoring": {
            "prometheus_port": 8000,
            "log_level": "INFO"
          }
        }
        ''')
    
    def _create_agent_code(self):
        self._write_file('agents/src/common/simple_agent.py', '''
        """Simple LangGraph agent implementation"""
        import os
        import json
        from langchain_openai import ChatOpenAI
        from langgraph.graph import StateGraph, END
        from typing import TypedDict, List
        
        class AgentState(TypedDict):
            messages: List[str]
            result: str
        
        class SimpleAgent:
            def __init__(self, config_path: str):
                with open(config_path) as f:
                    self.config = json.load(f)
                
                self.llm = ChatOpenAI(
                    model=self.config['model']['model_name'],
                    api_key=os.getenv('OPENAI_API_KEY')
                )
                
                self.workflow = self._build_workflow()
            
            def _build_workflow(self):
                workflow = StateGraph(AgentState)
                
                def process(state):
                    messages = state['messages']
                    response = self.llm.invoke(messages[-1])
                    return {'result': response.content}
                
                workflow.add_node("process", process)
                workflow.set_entry_point("process")
                workflow.add_edge("process", END)
                
                return workflow.compile()
            
            def execute(self, task: str):
                result = self.workflow.invoke({
                    'messages': [task],
                    'result': ''
                })
                return result['result']
        ''')
    
    def _create_financial_tools(self):
        self._write_file('tools/financial/stock_tools.py', '''
        """Financial analysis tools"""
        import yfinance as yf
        from langchain.tools import Tool
        
        def stock_price_lookup(ticker: str) -> str:
            """Get stock price"""
            try:
                stock = yf.Ticker(ticker)
                info = stock.info
                return f"${info.get('currentPrice', 'N/A')}"
            except:
                return f"Error: Could not fetch {ticker}"
        
        def get_stock_tool():
            return Tool(
                name="StockPrice",
                func=stock_price_lookup,
                description="Get current stock price. Input: ticker symbol"
            )
        ''')
    
    def _create_dockerfile(self):
        self._write_file('agents/Dockerfile', '''
        FROM nvidia/cuda:12.3.0-runtime-ubuntu22.04
        
        ENV PYTHONUNBUFFERED=1
        
        RUN apt-get update && apt-get install -y python3.11 python3-pip
        
        WORKDIR /app
        COPY requirements.txt .
        RUN pip3 install --no-cache-dir -r requirements.txt
        
        COPY agents/src /app/src
        COPY agents/configs /app/configs
        COPY tools /app/tools
        
        ENV PYTHONPATH=/app/src/common:/app/tools:$PYTHONPATH
        
        EXPOSE 50051 8000
        
        CMD ["python3", "src/common/simple_agent.py"]
        ''')
    
    def _create_agent_manifest(self):
        self._write_file('agents/kubernetes/financial-analyst.yaml', '''
        apiVersion: v1
        kind: Secret
        metadata:
          name: agent-secrets
          namespace: agents
        type: Opaque
        stringData:
          OPENAI_API_KEY: "your_key_here"
        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: financial-analyst
          namespace: agents
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: financial-analyst
          template:
            metadata:
              labels:
                app: financial-analyst
              annotations:
                prometheus.io/scrape: "true"
                prometheus.io/port: "8000"
            spec:
              containers:
              - name: agent
                image: financial-analyst:latest
                imagePullPolicy: Never
                ports:
                - containerPort: 50051
                - containerPort: 8000
                envFrom:
                - secretRef:
                    name: agent-secrets
                resources:
                  requests:
                    nvidia.com/gpu: 1
                    memory: "4Gi"
                    cpu: "2000m"
                  limits:
                    nvidia.com/gpu: 1
                    memory: "8Gi"
                    cpu: "4000m"
        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: financial-analyst
          namespace: agents
        spec:
          selector:
            app: financial-analyst
          ports:
          - port: 50051
            name: grpc
          - port: 8000
            name: metrics
        ''')
    
    def _create_grafana_dashboard(self):
        self._write_file('monitoring/grafana/dashboards/agent-dashboard.json', '''
        {
          "dashboard": {
            "title": "Agent Monitoring",
            "panels": [
              {
                "title": "Agent Status",
                "type": "stat"
              }
            ]
          }
        }
        ''')
    
    def _create_docs(self):
        self._write_file('docs/INSTALLATION.md', '''
        # Installation Guide
        
        ## Quick Install
        
        ```bash
        sudo ./scripts/setup-phase1.sh
        ```
        
        ## Manual Steps
        
        1. Install prerequisites
        2. Reboot
        3. Install K3s
        4. Deploy infrastructure
        5. Deploy agents
        ''')
        
        self._write_file('docs/OPERATIONS.md', '''
        # Operations Guide
        
        ## Start Services
        
        ```bash
        sudo systemctl start k3s
        make port-forward
        ```
        
        ## Monitor
        
        - Grafana: http://localhost:3000
        - Prometheus: http://localhost:9090
        ''')
        
        self._write_file('docs/TROUBLESHOOTING.md', '''
        # Troubleshooting
        
        ## GPU Not Available
        
        ```bash
        nvidia-smi
        kubectl get nodes -o yaml
        ```
        
        ## Pods Not Starting
        
        ```bash
        kubectl describe pod <pod-name> -n <namespace>
        kubectl logs <pod-name> -n <namespace>
        ```
        ''')
    
    def _create_tests(self):
        self._write_file('tests/test_agent_basic.py', '''
        """Basic agent tests"""
        import subprocess
        
        def test_cluster_running():
            """Test K3s cluster is running"""
            result = subprocess.run(['kubectl', 'get', 'nodes'], 
                                  capture_output=True, text=True)
            assert 'Ready' in result.stdout
        
        def test_gpu_available():
            """Test GPU is available"""
            result = subprocess.run(['nvidia-smi'], 
                                  capture_output=True, text=True)
            assert 'NVIDIA' in result.stdout
        
        if __name__ == '__main__':
            print("Running basic tests...")
            test_cluster_running()
            print("✓ Cluster running")
            test_gpu_available()
            print("✓ GPU available")
            print("All tests passed!")
        ''')
    
    def _print_summary(self):
        print(f"\n{'='*70}")
        print("✅ Project Created Successfully!")
        print(f"{'='*70}\n")
        print(f"📁 Location: {self.base_path.absolute()}\n")
        print(f"📊 Created:")
        print(f"   - {len(self.dirs_created)} directories")
        print(f"   - {len(self.files_created)} files\n")
        print("🚀 Next Steps:")
        print(f"   1. cd {self.project_name}")
        print("   2. cp .env.example .env")
        print("   3. Edit .env with your API keys")
        print("   4. sudo ./scripts/setup-phase1.sh\n")
        print("📚 Key Files:")
        print("   - README.md - Project overview")
        print("   - Makefile - Quick commands")
        print("   - scripts/setup-phase1.sh - Complete setup\n")


def main():
    parser = argparse.ArgumentParser(description='Create multi-agent project')
    parser.add_argument('project_name', nargs='?', default='multi-agent-system')
    parser.add_argument('--path', default='.')
    args = parser.parse_args()
    
    creator = ProjectCreator(args.project_name, args.path)
    creator.create()


if __name__ == '__main__':
    main()