podTemplate(containers: [
    containerTemplate(
        name: 'python', 
        image: 'python:3.10-slim'
        )
  ]) {

    node(POD_LABEL) {
        stage('Get a Python project') {
            container('python') {
                stage('Shell Execution') {
                    sh '''
                    echo "Hello! I am executing shell"
                    '''
                    sh "python --version"
                    containerLog 'python'
                }
            }
        }

    }
}