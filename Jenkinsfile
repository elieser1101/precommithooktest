#!groovy
node {
    git url: 'https://github.com/elieser1101/precommithooktest', poll: false
    sh "pwd & ls"
    sh "env && echo changejenkinsfile2"
    sh "echo $ref"
    sh "echo $changed_files"
}
