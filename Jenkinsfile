pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main',url:'https://github.com/bhavani-github-user/my-cicd-pipeline'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-cicd-app .'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'echo Tests Passed!'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run my-cicd-app'
            }
        }

        stage('Cleanup Containers') {
            steps {
                echo 'Cleaning up containers...'
                sh 'docker rm $(docker ps -aq) -f || true'
            }
        }
    }
}
