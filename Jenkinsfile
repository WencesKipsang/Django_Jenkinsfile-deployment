pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    dir('/root/frs_cicd/CICD') {
                        git branch: 'main', url: 'https://github.com/WencesKipsang/Django_Jenkinsfile-deployment.git'                        
                    } 
                }              

            }
        }
        
        stage('Build') {
            steps {
                echo "Building"
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
        
        stage('Deploy') {
            steps {
                echo "Deploying"
                dir('/root/frs_cicd') {
                    sh '''
                    sudo systemctl start jenkins-deployment-gunicorn.socket
                    sudo systemctl enable jenkins-deployment-gunicorn.socket
                    sudo systemctl start jenkins-deployment-gunicorn.service
                    sudo systemctl enable jenkins-deployment-gunicorn.service
                    sudo systemctl status jenkins-deployment-gunicorn.service
                    sudo systemctl restart jenkins-deployment-gunicorn.service
                    '''
                    
                }
            }
        }
        
        stage('Release') {
            steps {
                echo "Releasing"
            }
        }
    }
}