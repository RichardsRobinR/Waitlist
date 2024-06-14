pipeline {
  agent any
  stages {
    stage('Clone Git') {
      steps {
        git(url: 'https://github.com/RichardsRobinR/Waitlist', branch: 'master')
      }
    }

    stage('Build Docker') {
      parallel {
        stage('Build Docker') {
          steps {
            sh 'cd gcontacts && echo admin | sudo -S docker build -t waitlist-django-app:latest .'
          }
        }

        stage('ls Log') {
          steps {
            sh 'cd gcontacts && ls -l'
          }
        }

      }
    }

    stage('Login to docker') {
      steps {
        sh 'sudo docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
      }
    }

  }
}