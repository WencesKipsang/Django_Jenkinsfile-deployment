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

                sh 'cd  /frs_cicd'
                sh 'source CiEnv/bin/activate'
                sh 'pip3 install -r requirements.txt'
                sh 'cd  /frs_cicd/Django_Jenkinsfile-deployment'
                sh 'python3 manage.py makemigrations'
                sh 'python3 manage.py migrate'



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