pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '======= Build stage ======='
                sh 'echo "Hello from V2" > app.txt'
            }
        }

        stage('Test') {
            steps {
                echo '======= Test stage ======='
                sh 'test -f app.txt'
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