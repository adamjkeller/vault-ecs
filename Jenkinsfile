// Job == vault-unseal_pipeline
node() {
    withCredentials([
        [$class: 'StringBinding', credentialsId: 'vaultToken', variable: 'TOKEN'],
        [$class: 'StringBinding', credentialsId: 'vaultUnsealKey1', variable: 'KEY1'],
        [$class: 'StringBinding', credentialsId: 'vaultUnsealKey2', variable: 'KEY2'],
        [$class: 'StringBinding', credentialsId: 'vaultUnsealKey3', variable: 'KEY3']
    ]) 
    {
    stage 'Checkout'
        checkout(
           [$class: 'GitSCM',
               branches: [
                    [
                        name: 'master'
                    ]
               ],
               userRemoteConfigs: [
                   [
                       url: 'https://github.com/adamjkeller/vault-ecs.git'
                   ]
               ],
               extensions: [
                   [$class: 'CleanBeforeCheckout']
               ]
           ]
       )
    stage 'Check/Unseal Vaults'
        sh "apk --update add python py-pip"
        sh "pip install -r requirements.txt"
        sh "python unseal.py -t ${env.TOKEN} -k1 ${env.KEY1} -k2 ${env.KEY2} -k3 ${env.KEY3}"
    }
}
