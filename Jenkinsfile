pipeline {
  agent any
  stages {
    stage('Clone Git') {
      steps {
        git(url: 'https://github.com/RichardsRobinR/Waitlist', branch: 'master')
      }
    }

    // stage('SonarQube Analysis') {
    //   steps {
    //     script {
    //       scannerHome = tool 'sonarqube'
    //     }
    //     withSonarQubeEnv('sonarcube-server') {
    //       sh "${scannerHome}/bin/sonar-scanner"
    //     } 
    //   }
    // }

    stage('Testing') {
      steps {
        // sh 'cd gcontacts'
        sh 'cd gcontacts && pip install --user virtualenv &&  ~/.local/bin/virtualenv env '


         // Print workspace directory for debugging
        sh 'cd gcontacts &&  pwd'
        sh  'cd gcontacts && ls -l'
        
        // Activate the virtual environment
        // sh 'cd gcontacts && . ./env/bin/activate'

        // sh '. env/bin/activate'
        sh 'cd gcontacts && . ./env/bin/activate && pip install -r requirements.txt'
        sh 'cd gcontacts && . ./env/bin/activate && ./env/bin/python ./manage.py migrate'
        sh 'cd gcontacts && . ./env/bin/activate && ./env/bin/pytest'
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
        withCredentials([usernamePassword(credentialsId: 'b718f5e5-e2ec-45c8-9524-794e94dc7d64', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
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

  }
}
