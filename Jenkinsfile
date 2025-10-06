pipeline {
    agent any

    tools {
        // ✅ Correct tool name
        sonarScanner 'SonarScanner'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/rukaiya14/sonar-test.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My SonarQube Server') {
                    bat "sonar-scanner -Dsonar.projectKey=sonar-demo -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.token=squ_cbd3ad7e63e69ad61a1c953b1b0b3451811e0407"
                }
            }
        }
    }
}
