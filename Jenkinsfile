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
            container('python') {
                stage('Shell Execution') {
                    sh '''
                    echo "Hello! I am executing shell"
                    '''
                    sh 'python --version'
                    sh 'ls -la'
                    containerLog 'python'
                }
            }
        }

    }
}