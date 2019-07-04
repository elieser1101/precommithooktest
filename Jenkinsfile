#!groovy
node {
    git url: 'https://github.com/elieser1101/precommithooktest', poll: false
    sh "pwd & ls"
    sh "env && echo prueba2pullrequest2"
    properties([
      pipelineTriggers([
       [$class: 'GenericTrigger',
        genericVariables: [
         [key: 'ref', value: '$.ref'],
         [
          key: 'before',
          value: '$.before',
          expressionType: 'JSONPath', //Optional, defaults to JSONPath
          regexpFilter: '', //Optional, defaults to empty string
          defaultValue: '' //Optional, defaults to empty string
         ]
        ],
        genericRequestVariables: [
         [key: 'requestWithNumber', regexpFilter: '[^0-9]'],
         [key: 'requestWithString', regexpFilter: '']
        ],
        genericHeaderVariables: [
         [key: 'headerWithNumber', regexpFilter: '[^0-9]'],
         [key: 'headerWithString', regexpFilter: '']
        ],
         
        causeString: 'Triggered on $ref',
        
        token: 'pruebahook',
        
        printContributedVariables: true,
        printPostContent: true,
        
        silentResponse: false,
        
        regexpFilterText: '$ref',
        regexpFilterExpression: 'refs/heads/master' 
       ]
      ])
     ])
    sh "echo $payload"
    sh "echo $ref"
    sh "echo $changed_files"
}
