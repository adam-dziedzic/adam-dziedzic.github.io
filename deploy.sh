timestamp=$(date "+%Y-%m-%d-%H:%M:%S")
bundle exec jekyll build --destination docs
git add *
git commit -am "deploy at timestamp: ${timestamp}"
git push origin source
