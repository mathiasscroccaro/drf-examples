podTemplate(containers: [
    containerTemplate(
        name: 'python', 
        image: 'python3.9:alpine'
        )
  ]) {

    node(POD_LABEL) {
        stage('Get a Python project') {
            container('python') {
                stage('Shell Execution') {
                    sh '''
                    echo "Hello! I am executing shell"
                    '''
                }
            }
        }

    }
}