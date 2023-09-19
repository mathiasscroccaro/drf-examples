def gitUrl = 'https://github.com/mathiasscroccaro/drf-examples.git'
def gitBranch = '6-create-k8s-manifest'

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
        // stage('Test') {
        //     git url: gitUrl, branch: gitBranch
        //     container('python') {
        //         stage('Install dependencies') {
        //             sh 'pip install -r requirements-dev.txt'
        //         }
        //         stage('Run unittests') {
        //             sh 'python manage.py test'
        //         }
        //     }
        // }
        stage('Build') {
            git url: gitUrl, branch: gitBranch
            container('kaniko') {
                stage('Build image and push to registry') {
                    sh 'ls -la'
                    sh 'pwd'
                    sh '''
                    /kaniko/executor --insecure --dockerfile `pwd`/Dockerfile --context `pwd` \
                    --destination "registry.container-registry:5000/drf-example:latest"
                    '''
                }
            }
        }

    }
}