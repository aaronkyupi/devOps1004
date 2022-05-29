properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/aaronkyupi/devOps1004.git"
    }
    stage("show files"){
        bat "dir"
    }
}
