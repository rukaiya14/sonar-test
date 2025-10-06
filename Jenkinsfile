pipeline {
    agent any

    environment {
        // Replace this with your actual SonarQube token
        SONAR_TOKEN = "squ_cbd3ad7e63e69ad61a1c953b1b0b3451811e0407"
        SONAR_HOST = "http://localhost:9000"
        PROJECT_KEY = "sonar-demo"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code from GitHub..."
                git branch: 'main', url: 'https://github.com/rukaiya14/sonar-test.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo "Starting SonarQube Analysis..."
                // Run SonarScanner CLI
                bat """
                sonar-scanner ^
                -Dsonar.projectKey=%PROJECT_KEY% ^
                -Dsonar.sources=. ^
                -Dsonar.host.url=%SONAR_HOST% ^
                -Dsonar.login=%SONAR_TOKEN%
                """
            }
        }
    }

    post {
        success {
            echo "SonarQube analysis completed successfully!"
        }
        failure {
            echo "Build failed. Check the console output for details."
        }
    }
}
