pipeline {
    agent any

    environment {
        APP_VERSION = '1.0'
        APP_NAME = 'my-app'
        DOCKER_REPO = 'my-docker-repo'
    }

    stages {
        stage('Build') {
            steps {
                echo '======= Build stage ======='
                echo "App Name: ${APP_NAME}, Version: ${APP_VERSION}, Docker Repo: ${DOCKER_REPO}"
            }
        }

        stage('Test') {
            steps {
                echo '======= Test stage ======='
                echo "Pipeline Name: ${JOB_NAME}"
                echo "Build Number: ${BUILD_NUMER}"
            }
        }

        stage('Deploy') {
            steps {
                echo '======= Deploy stage ======='
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}