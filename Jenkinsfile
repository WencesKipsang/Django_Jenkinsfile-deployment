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
                        sh '''
                        . CiEnv/bin/activate
                        echo "Virtual environment activated"
                        cd /root/frs_cicd/CICD
                        pip install -r requirements.txt
                        python manage.py makemigrations
                        python manage.py migrate
                        '''
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