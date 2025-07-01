pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t my-cicd-app .'
            }
        }

        stage('Run') {
            steps {
                echo 'Running Docker container...'
                sh 'docker run my-cicd-app'
            }
        }
    }
}

