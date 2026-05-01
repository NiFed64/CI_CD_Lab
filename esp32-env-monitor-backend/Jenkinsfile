// Jenkinsfile
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'esp32-env-monitor:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'python -m pytest tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Container (CD Demo)') {
            steps {
                script {
                    // Остановить старый контейнер, если есть
                    sh 'docker stop env-monitor-app || true'
                    sh 'docker rm env-monitor-app || true'
                    
                    // Запустить новый
                    sh "docker run -d --name env-monitor-app -p 5000:5000 ${env.DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
