timestamp=$(date "+%Y-%m-%d-%H:%M:%S")
mv _site docs
git add *
git commit -am "deploy at timestamp: ${timestamp}"
git push origin source
mv docs _site
