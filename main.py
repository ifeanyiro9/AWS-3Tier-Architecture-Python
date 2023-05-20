import boto3
import vpc_subnets

# Create the VPC
response_vpc = vpc_subnets.create_custom_vpc('10.0.0.0/16','Name', '3Tier-VPC')
print(response_vpc)
print("")

#Get VPC id
vpc_id = response_vpc["Vpc"]["VpcId"] 
print(vpc_id)
print("")

# Create public subnet 1
response_pub_sub1 = vpc_subnets.create_custom_subnet("us-east-1a", "10.0.0.0/20", vpc_id, "Name", "3Tier-Pub-Sub1")
print(response_pub_sub1)
print("")

# Create public subnet 2
response_pub_sub2 = vpc_subnets.create_custom_subnet("us-east-1b", "10.0.16.0/20", vpc_id, "Name", "3Tier-Pub-Sub2")
print(response_pub_sub2)

# Create private subnet 1
response_priv_sub1 = vpc_subnets.create_custom_subnet("us-east-1a", "10.0.128.0/20", vpc_id, "Name", "3Tier-Priv-Sub1")
print(response_priv_sub1)
print("")

# Create private subnet 2
response_priv_sub2 = vpc_subnets.create_custom_subnet("us-east-1b", "10.0.144.0/20", vpc_id, "Name", "3Tier-Priv-Sub2")
print(response_priv_sub2)

print("")

# Create private subnet 3
response_priv_sub3 = vpc_subnets.create_custom_subnet("us-east-1a", "10.0.160.0/20", vpc_id, "Name", "3Tier-Priv-Sub3")
print(response_priv_sub1)
print("")
print("")

# Create private subnet 4
response_priv_sub4 = vpc_subnets.create_custom_subnet("us-east-1b", "10.0.178.0/20", vpc_id, "Name", "3Tier-Priv-Sub4")
print(response_priv_sub4)