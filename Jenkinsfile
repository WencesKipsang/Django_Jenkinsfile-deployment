pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                script {
                    dir('/root/frs_cicd') {
                        git branch: 'main', url: 'https://github.com/WencesKipsang/Django_Jenkinsfile-deployment.git'                        
                    } 
                }              

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