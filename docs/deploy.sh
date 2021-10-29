timestamp=$(date "+%Y-%m-%d-%H:%M:%S")
git add *
git commit -am "deploy at timestamp: ${timestamp}"
git push origin source
