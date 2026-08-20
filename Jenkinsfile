pipeline {
    agent any

    environment {
        FILE_TO_TEST = 'app.txt'
    }

    stages {
        stage('Build') {
            steps {
                echo '======= Build stage ======='
                sh 'echo "Hello from V3.5" > app.txt'
            }
        }

        stage('Test') {
            steps {
                echo '======= Test stage ======='
                sh 'python3 search_word.py Hello'
            }
        }

        stage('Deploy') {
            steps {
                echo '======= Deploy stage ======='
                sh 'mkdir -p deploy'
                sh 'cp app.txt deploy/'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}