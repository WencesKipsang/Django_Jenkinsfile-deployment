pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                sh "cd  /root/frs_cicd  git branch: 'main', url: 'erthyjklhttps://github.com/WencesKipsang/Django_Jenkinsfile-deployment.git'"
                              
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