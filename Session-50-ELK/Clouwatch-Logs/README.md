# Add Logs to cloudwatch using Agent

1. Create EC2 Instance
    - aws linux instance
2. Wants to write logs from EC2 to CLoudwatch using agent. Without giving permission if you trying write that. It will not write logs.
3. Create Role: EC2-cloudwatch-role
    - IAM -> Role -> select AWS Service
    - EC2 -> next
    - Policy: CloudWatchAgentServerPolicy
    - name: ec2-cloudwatch-role
    - create
4. attach this Role to EC2 Instance.
    - go to EC2 -> select instance
    - actions -> security -> modify the Role
    - select just now created role
    - save

5. Connect With EC2
    - use SSH or browser to connect

```bash
#  Install agent
sudo yum install amazon-cloudwatch-agent -y

sudo nano /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
# edit with the code provided in config.json file save

# Start Agent
sudo  /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
-a start \
-c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json \
-m ec2

# Check Status
amazon-cloudwatch-agent-ctl -a status

# Let's Generate Logs
sudo mkdir /var/log/myapp
sudo touch /var/log/myapp/app.log

echo "Test Log" | sudo tee -a /var/log/myapp/app.log
echo "Final Success Test $(date)" | sudo tee -a /var/log/myapp/app.log
echo "Authentication Success $(date)" | sudo tee -a /var/log/myapp/app.log

#  in case config file was not saved and if you are changing later make sure
# to stop and start agent again
# Stop Agent
amazon-cloudwatch-agent-ctl -a stop
amazon-cloudwatch-agent-ctl -a status
# Start Agent
sudo  /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
-a start \
-c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json \
-m ec2

```
- Check Logs in AWS CloudWatch
- Log Management > Log Groups > folder for your logs