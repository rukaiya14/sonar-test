pipeline {
    agent any

    tools {
        sonarQubeScanner 'SonarScanner'
    }

    environment {
        SONARQUBE = 'sonarqube'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rukaiya14/sonar-test.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    bat "sonar-scanner -Dsonar.projectKey=sonar-demo -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.token=squ_cbd3ad7e63e69ad61a1c953b1b0b3451811e0407"
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
