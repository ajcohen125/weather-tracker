pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh "echo 'Running Test automation'"
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    app = docker.build("weather-tracker")
                }
            }
        }
        stage('Run Docker Image') {
            steps {
                script {
                    echo "Hello from Run Docker Image"
                }
            }

        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('http://192.168.1.220:5000/docker-private', 'nexus_login') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
        stage('Create archive') {
            steps {
                    sh 'tar cvzf weather-tracker.tar.gz *.py testing/ Dockerfile'
                    archiveArtifacts artifacts: 'weather-tracker.tar.gz', followSymlinks: false
                }
            }
        stage('Push Archive to Nexus') {
            steps {
                nexusArtifactUploader artifacts: [[artifactId: 'weather-tracker', classifier: '', file: 'weather-tracker.tar.gz', type: 'tar.gz']], credentialsId: 'nexus_login', groupId: 'weather-tracker', nexusUrl: '192.168.1.220:8081', nexusVersion: 'nexus3', protocol: 'http', repository: 'Artifacts', version: "${env.BUILD_NUMBER}"
            }
        }
        stage('Clean workspace after run') {
            steps {
                cleanWs notFailBuild: true
            }
        }
    }
}
