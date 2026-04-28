pipeline {
    agent any

    stages {
        stage('Checking the code') {
            steps {
                git branch: "main", url: "https://github.com/Priyanka22577/python-demo-projects.git"
            }
        }
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
