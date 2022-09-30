echo 'Deploy application'

rm -f ./package

pip install --target ./package -r requirements.txt

cd ./package
zip -r ../deploy-package.zip .

cd ..
zip -g deploy-package.zip lambda_function.py
zip -g deploy-package.zip -r lib/