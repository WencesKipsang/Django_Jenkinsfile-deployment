pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                script {
                    dir('/root/frs_cicd/CICD') {
                        git branch: 'main', url: 'https://github.com/WencesKipsang/Django_Jenkinsfile-deployment.git'                        
                    } 
                }              

            }
        }
        
        stage('deploy') {
            steps {
                echo "Deploying"
                script {
                    dir('/root/frs_cicd') {
                        source  CiEnv/bin/activate
                        echo "Virtual environment activated"                      
                        dir('/root/frs_cicd/CICD') {
                            echo 'hey'                       
                        }
                    } 
                }


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