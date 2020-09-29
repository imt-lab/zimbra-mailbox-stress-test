# zimbra mailbox(lmtp) stress test
A stress test tool for zimbra mailbox (lmtp)


### Install

##### Build image

```shell script
git clone https://github.com/imt-lab/zimbra-mailbox-stress-test.git
cd zimbra-mailbox-stress-test/app
docker build -t "zimbra-lmtp-stress-tests" .
```

##### Run app

Edit the `docker-compose.yml` file, then run it:

```shell script
cd zimbra-mailbox-stress-test/
docker-compose up --scale lmtp_stress_test=3
```

Check the logs mailbox:

```shell script
tail -100f /opt/zimbra/log/mailbox.log
```

That's it!