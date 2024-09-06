pipeline {
  agent {
    kubernetes {
            label 'jenkins-agent'  // This should match the label of your Pod Template
            defaultContainer 'kubectl'  // The name of the container defined in the Pod Template
    }
  } 
  stages {
    stage('Clone Git') {
      steps {
        git(url: 'https://github.com/RichardsRobinR/Waitlist', branch: 'master')
      }
    }

    stage('Deploy to Kubernetes') {
            steps {
                container('kubectl') {
                    sh 'kubectl get nodes'
                }
            }
    }
   
    // stage('Activationg Enviornment') {
    //   steps {
    //     // sh 'cd gcontacts'
    //     sh 'cd gcontacts && sudo apt install python3-virtualenv -y &&  /usr/bin/virtualenv env '


    //      // Print workspace directory for debugging
    //     sh 'cd gcontacts &&  pwd'
    //     sh  'cd gcontacts && ls -l'
        
    //     // Activate the virtual environment
    //     // sh 'cd gcontacts && . ./env/bin/activate'

    //     // sh '. env/bin/activate'
    //   }
    // }

    // stage('Installing Requirments and Migrating ') {
    //   steps {
        
    //     sh 'cd gcontacts && . ./env/bin/activate && pip install -r requirements.txt'
    //     sh 'cd gcontacts && . ./env/bin/activate && ./env/bin/python ./manage.py migrate'
    //   }
    // }

    //  stage('Testing and generating Coverage Report') {
    //   steps {
    //     sh 'cd gcontacts && . ./env/bin/activate && ./env/bin/pytest --cov=. --cov-report=xml'
    //   }
    // }

    //  stage('SonarQube Analysis') {
    //   steps {
    //     script {
    //       scannerHome = tool 'sonarqube'
    //     }
    //     withSonarQubeEnv('sonarcube-server') {
    //       sh "${scannerHome}/bin/sonar-scanner -Dsonar.python.coverage.reportPaths=gcontacts/coverage.xml"
    //     } 
    //   }
    // }


    // stage('Build Docker') {
    //   parallel {
    //     stage('Build Docker') {
    //       steps {
    //         sh 'cd gcontacts && docker build -t waitlist-django-app:latest .'
    //       }
    //     }

    //     stage('ls Log') {
    //       steps {
    //         sh 'cd gcontacts && ls -l'
    //       }
    //     }

    //   }
    // }

    // stage('Login to docker') {
    //   steps {
    //     withCredentials([usernamePassword(credentialsId: 'b718f5e5-e2ec-45c8-9524-794e94dc7d64', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
    //       sh 'echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin'          
    //     }
        
    //   }
    // }

    // stage('Push to Dockerhub') {
    //   steps {
    //     sh 'docker tag waitlist-django-app richardsrobinr/waitlist-django-app:latest'
    //     sh 'docker push richardsrobinr/waitlist-django-app:latest'       
    //   }
    // }

  }
}
