pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/WencesKipsang/Django_Jenkinsfile-deployment.git']])
                sh 'cd  /root/frs_cicd'
                sh 'git clone https://github.com/WencesKipsang/Django_Jenkinsfile-deployment.git'               
            }
        }
        
        stage('deploy') {
            steps {
                echo "Deploying"


            }
        }
        
        stage('Test') {
            steps {
                echo "Testing"
            }
        }
        
        stage('Release') {
            steps {
                echo "Releasing"
            }
        }
    }
}