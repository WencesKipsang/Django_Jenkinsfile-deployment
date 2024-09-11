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
                script {
                    dir('/root/frs_cicd') {
                        sh 'source CiEnv/bin/activate'                       
                        dir('/root/frs_cicd/Django_Jenkinsfile-deployment') {
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