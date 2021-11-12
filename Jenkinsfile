pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo 'Running Test automation'
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


        }
        stage('Push Docker Image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry('http://192.168.1.220:8083/docker-private', 'nexus_login') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
        stage('Create archive') {
            steps {
                    script {
                        tar cvzf weather-tracker-${env.BUILD_NUBMER}.tar.gz *.py testing/ Dockerfile
                    }
                    archiveArtifacts artifacts: 'weather-tracker-${env.BUILD_NUMBER}.tar.gz', followSymlinks: false
                }
            }
        stage('Push Archive to Nexus') {
                nexusArtifactUploader artifacts: [[artifactId: 'weather-tracker', classifier: '', file: 'weather-tracker-${env.BUILD_NUMBER}.tar.gz', type: 'tar.gz']], credentialsId: 'nexus_login', groupId: 'weather-tracker', nexusUrl: '192.168.1.220:8081', nexusVersion: 'nexus3', protocol: 'http', repository: 'weather-tracker', version: '${env.BUILD_NUMBER}'
        }
    }
}
