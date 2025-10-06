pipeline {
    agent any

    environment {
        // Name of the SonarQube server configured in Jenkins
        SONARQUBE_SERVER = 'My SonarQube Server'

        // Optional: You can store your token as a Jenkins Secret Text credential
        // and reference it here with credentials('sonar-token-id')
        SONAR_TOKEN = 'squ_cbd3ad7e63e69ad61a1c953b1b0b3451811e0407'
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone your GitHub repo
                git 'https://github.com/rukaiya14/sonar-test.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                // Wrap analysis in Jenkins SonarQube environment
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    // Run the scanner using your token
                    bat """
                    sonar-scanner ^
                    -Dsonar.projectKey=sonar-demo ^
                    -Dsonar.sources=. ^
                    -Dsonar.host.url=http://localhost:9000 ^
                    -Dsonar.token=${SONAR_TOKEN}
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'SonarQube analysis finished. Check your dashboard at http://localhost:9000/dashboard?id=sonar-demo'
        }
    }
}
