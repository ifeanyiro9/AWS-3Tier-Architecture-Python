import boto3
import vpc_subnets
import internet_nat_gateway
import route_tables

# Create the VPC
response_vpc = vpc_subnets.create_custom_vpc('10.0.0.0/16','Name', '3Tier-VPC')
print("Create VPC Response")
print(response_vpc)
print("")

#Get VPC id
vpc_id = response_vpc["Vpc"]["VpcId"] 
print("VPC ID")
print(vpc_id)
print("")

# Create public subnet 1
response_pub_sub1 = vpc_subnets.create_custom_subnet("us-east-1a", "10.0.0.0/20", vpc_id, "Name", "3Tier-Pub-Sub1")
print("Create Public Subnet 1 Response")
print(response_pub_sub1)
print("")

# Create public subnet 2
response_pub_sub2 = vpc_subnets.create_custom_subnet("us-east-1b", "10.0.16.0/20", vpc_id, "Name", "3Tier-Pub-Sub2")
print("Create Public Subnet 2 Response")
print(response_pub_sub2)
print("")

# Create private subnet 1
response_priv_sub1 = vpc_subnets.create_custom_subnet("us-east-1a", "10.0.128.0/20", vpc_id, "Name", "3Tier-Priv-Sub1")
print("Create Private Subnet 1 Response")
print(response_priv_sub1)
print("")

# Create private subnet 2
response_priv_sub2 = vpc_subnets.create_custom_subnet("us-east-1b", "10.0.144.0/20", vpc_id, "Name", "3Tier-Priv-Sub2")
print("Create Private Subnet 2 Response")
print(response_priv_sub2)
print("")

# Create private subnet 3
response_priv_sub3 = vpc_subnets.create_custom_subnet("us-east-1a", "10.0.160.0/20", vpc_id, "Name", "3Tier-Priv-Sub3")
print("Create Private Subnet 3 Response")
print(response_priv_sub1)
print("")

#Create private subnet 4
response_priv_sub4 = vpc_subnets.create_custom_subnet("us-east-1b", "10.0.178.0/20", vpc_id, "Name", "3Tier-Priv-Sub4")
print("Create Private Subnet 4 Response")
print(response_priv_sub4)
print("")

#Create and attach Internet Gateway
response_create_attach_ig = internet_nat_gateway.create_attach_internet_gateway(vpc_id, "Name", "3Tier-Int-GW")
print("Create and attach Iternet Gateway Response")
print(response_create_attach_ig)
print("")

#Get subnet ID for NAT Gateway
subnet_id_ng = response_pub_sub2["Subnet"]["SubnetId"]
print("Get Subnet ID for NAT Gateway")
print(subnet_id_ng)
print("")

#Create NAT Gateway
response_create_ng = internet_nat_gateway.create_nat_gateway(subnet_id_ng, "Name", "3Tier-EIP", "Name", "3Tier-Nat-GW")
print("Create NAT Gateway Response")
print(response_create_ng)
print("")

#Get Internet Gateway ID
int_gw_id = response_create_attach_ig["InternetGateway"]["InternetGatewayId"]
print("Get Internet Gateway ID")
print(int_gw_id)
print("")

#Create Route table and Route to Internet Gateway
response_public_rt = route_tables.create_pub_rt(vpc_id, "0.0.0.0/0", int_gw_id, "Name", "3Tier-Pub-RT")
print("Create Route Table for Internet Gateway Response")
print(response_create_ng)
print("")

#Get NAT Gateway ID
nat_gw_id = response_create_attach_ig["NatGateway"]["NatGatewatId"]
print("Get NAT Gateway ID")
print(nat_gw_id)
print("")

#Create Route table and Route to NAT Gateway
response_private_rt = route_tables.create_priv_rt(vpc_id, "0.0.0.0/0", nat_gw_id, "Name", "3Tier-Priv-RT")
print("Create Route Table for NAT Gateway Response")
print(response_create_ng)
print("")




