pipeline {
    agent any

    stages {
        stage('Préparation') {
            steps {
                dir('backend') {
                    bat 'python -m venv venv'
                    bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Tests') {
            steps {
                dir('backend') {
                    bat 'venv\\Scripts\\activate && pytest'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminé.'
        }
    }
}
