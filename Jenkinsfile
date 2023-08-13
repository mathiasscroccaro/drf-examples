podTemplate(containers: [
    containerTemplate(
        name: 'python', 
        image: 'python:3.10-slim',
        command: 'sleep',
        args: '30d'
        )
  ]) {

    node(POD_LABEL) {
        stage('Get a Python project') {
            git url: 'https://github.com/mathiasscroccaro/drf-examples.git', branch: 'main'
            container('python') {
                stage('Install dependencies') {
                    sh 'pip install -r requirements-dev.txt'
                }
                stage('Run unittests') {
                    sh 'python manage.py test'
                }
            }
        }

    }
}