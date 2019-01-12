# check config

write-host -fore Yellow "---------------------------"
write-host -fore Yellow " Setting up build branch"
write-host -fore Yellow "---------------------------"
git checkout -b __build
cp travis\* .
mv travis_secrets.yaml secrets.yaml

write-host -fore Yellow "---------------------------"
write-host -fore Yellow " Running hass check_config "
write-host -fore Yellow "---------------------------"
hass --script check_config

if ($LASTEXITCODE -eq 0) {
    write-host -fore Green "SUCCESS"
} else {
    write-host -fore Red "Failed"
}

write-host -fore Yellow "---------------------------"
write-host -fore Yellow " Cleaning up"
write-host -fore Yellow "---------------------------"
rm secrets.yaml
rm fake_ssl_*.pem

git checkout master
git branch -d __build