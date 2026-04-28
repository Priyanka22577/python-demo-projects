pipeline {
    agent any

    stages {
    
        stage("Execute python program") {
            steps {
                    sh 'python3 python_demo/calculator.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp .'
    }
  }
       stage('run the container') {
           steps {
               sh 'docker run --rm -t myapp'
           }
       }
 }
}
