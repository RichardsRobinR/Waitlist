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
            sh 'cd gcontacts && docker build -t waitlist-django-app:latest .'
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
        withCredentials([usernamePassword(credentialsId: 'credentials-docker', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
          sh 'echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin'          
        }
        
      }
    }

    stage('Push to Dockerhub') {
      steps {
        sh 'docker tag waitlist-django-app richardsrobinr/waitlist-django-app:latest'
        sh 'docker push richardsrobinr/waitlist-django-app:latest'       
      }
    }

    stage('SonarQube Analysis') {
      def scannerHome = tool 'sonarqube';
      withSonarQubeEnv() {
        sh "${scannerHome}/bin/sonar-scanner"
      }
    }

  }
}