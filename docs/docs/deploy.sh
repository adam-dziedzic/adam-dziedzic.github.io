timestamp=`date "+%Y-%m-%d-%H:%M:%S"`
cd docs
rm -r *
cp -r ../_site/* .
git add *
cd ..
git commit -am "deploy at timestamp: ${timestamp}"
git push origin source