def gitUrl = 'https://github.com/mathiasscroccaro/drf-examples.git'
def gitBranch = '4-create-jenkinsfile'

podTemplate(containers: [
    containerTemplate(
        name: 'python', 
        image: 'python:3.10-slim',
        command: 'sleep',
        args: '30d'
    ),
    containerTemplate(
        name: 'kaniko', 
        image: 'gcr.io/kaniko-project/executor:v1.9.0-debug',
        command: 'sleep',
        args: '30d'
    )
  ]) {

    node(POD_LABEL) {
        stage('Test') {
            git url: gitUrl, branch: gitBranch
            container('python') {
                stage('Install dependencies') {
                    sh 'pip install -r requirements-dev.txt'
                }
                stage('Run unittests') {
                    sh 'python manage.py test'
                }
            }
        }
        stage('Build') {
            git url: gitUrl, branch: gitBranch
            container('kaniko') {
                stage('Build image and push to registry') {
                    sh '/kaniko/executor --insecure --dockerfile "Dockerfile" --destination "localhost:30000/drf-example"'
                }
            }
        }

    }
}