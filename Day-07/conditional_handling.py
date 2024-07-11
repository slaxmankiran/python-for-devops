import sys

ec2_instance_type = sys.argv[1]

if ec2_instance_type == "t2.micro":
    print("This instance will cost you $2 a day")

elif ec2_instance_type == "t2.medium":
    print("This instance will cost you $4 a day")

elif ec2_instance_type == "t2.large":
    print("This instance will cost you $8 a day")

elif ec2_instance_type == "t2.xlarge":
    print("This instance will cost you $10 a day")

elif ec2_instance_type == "t2.xxlarge":
    print("This instance will cost you $12 a day")

else:
    print("Please provide a valid instance type")