import boto3
import vpc_subnets
import internet_nat_gateway
import route_tables

ec2 = boto3.client('ec2')

# Create the VPC
response_vpc = vpc_subnets.create_custom_vpc('10.0.0.0/16','Name', '3Tier-VPC')
print("Create VPC Response")
print(response_vpc, "\n")


#Get VPC id
vpc_id = response_vpc["Vpc"]["VpcId"] 
print("VPC ID")
print(vpc_id, "\n")


# Create public subnet 1
response_pub_sub1 = vpc_subnets.create_custom_subnet("us-east-1a", "10.0.0.0/20", vpc_id, "Name", "3Tier-Pub-Sub1")
print("Create Public Subnet 1 Response")
print(response_pub_sub1, "\n")

# Get public subnet 1 ID
pub_sub_1_id = response_pub_sub1["Subnet"]["SubnetId"]




# Create public subnet 2
response_pub_sub2 = vpc_subnets.create_custom_subnet("us-east-1b", "10.0.16.0/20", vpc_id, "Name", "3Tier-Pub-Sub2")
print("Create Public Subnet 2 Response")
print(response_pub_sub2, "\n")

# Get public subnet 2 ID
pub_sub_2_id = response_pub_sub2["Subnet"]["SubnetId"]




# Create private subnet 1
response_priv_sub1 = vpc_subnets.create_custom_subnet("us-east-1a", "10.0.128.0/20", vpc_id, "Name", "3Tier-Priv-Sub1")
print("Create Private Subnet 1 Response")
print(response_priv_sub1, "\n")

# Get private subnet 1 ID
priv_sub_1_id = response_priv_sub1["Subnet"]["SubnetId"]




# Create private subnet 2
response_priv_sub2 = vpc_subnets.create_custom_subnet("us-east-1b", "10.0.144.0/20", vpc_id, "Name", "3Tier-Priv-Sub2")
print("Create Private Subnet 2 Response")
print(response_priv_sub2, "\n")

# Get private subnet 2 ID
priv_sub_2_id = response_priv_sub2["Subnet"]["SubnetId"]




# Create private subnet 3
response_priv_sub3 = vpc_subnets.create_custom_subnet("us-east-1a", "10.0.160.0/20", vpc_id, "Name", "3Tier-Priv-Sub3")
print("Create Private Subnet 3 Response")
print(response_priv_sub1, "\n")

# Get private subnet 3 ID
priv_sub_3_id = response_priv_sub3["Subnet"]["SubnetId"]



#Create private subnet 4
response_priv_sub4 = vpc_subnets.create_custom_subnet("us-east-1b", "10.0.178.0/20", vpc_id, "Name", "3Tier-Priv-Sub4")
print("Create Private Subnet 4 Response")
print(response_priv_sub4, "\n")

# Get private subnet 4 ID
priv_sub_4_id = response_priv_sub4["Subnet"]["SubnetId"]



#Create and attach Internet Gateway
response_create_attach_ig = internet_nat_gateway.create_attach_internet_gateway(vpc_id, "Name", "3Tier-Int-GW")
print("Create and attach Iternet Gateway Response")
print(response_create_attach_ig, "\n")


#Get subnet ID for NAT Gateway
subnet_id_ng = response_pub_sub2["Subnet"]["SubnetId"]
print("Get Subnet ID for NAT Gateway")
print(subnet_id_ng, "\n")

#Create NAT Gateway
response_create_ng = internet_nat_gateway.create_nat_gateway(subnet_id_ng, "Name", "3Tier-EIP", "Name", "3Tier-Nat-GW")
print("Create NAT Gateway Response")
print(response_create_ng, "\n")

#Get Internet Gateway ID
int_gw_id = response_create_attach_ig["InternetGateway"]["InternetGatewayId"]
print("Get Internet Gateway ID")
print(int_gw_id, "\n")

#Create Route table and Route to Internet Gateway
response_public_rt = route_tables.create_pub_rt(vpc_id, "0.0.0.0/0", int_gw_id, "Name", "3Tier-Pub-RT")
print("Create Route Table for Internet Gateway Response")
print(response_create_ng, "\n")

#Get NAT Gateway ID
nat_gw_id = response_create_ng["NatGateway"]["NatGatewayId"]
print("Get NAT Gateway ID")
print(nat_gw_id, "\n")

print("Waiting for NAT Gateway To be Available..." "\n")


ng_available = False

#Check if Nat Gateway is Active then create route
while ng_available == False:
    #Get NAT Gateway State
    get_nat_gw= ec2.describe_nat_gateways(
        Filter=[
            {
                'Name': 'nat-gateway-id',
                'Values': [
                    nat_gw_id,
                ],
            },
        ],
    )

    nat_gatway_info = get_nat_gw['NatGateways'][0]
    ng_state = nat_gatway_info['State']

    if ng_state == "available":
        print("NAT Gateway is now Available..." "\n")

        #Create Private Route Table and Route to NAT Gateway
        response_private_rt = route_tables.create_priv_rt(vpc_id, "0.0.0.0/0", nat_gw_id, "Name", "3Tier-Priv-RT")
        print("Create Route Table for NAT Gateway Response")
        print(response_create_ng, "\n")

        ng_available = True


#Get Public Route Table ID
pub_rt_id = response_public_rt["RouteTable"]["RouteTableId"]
print("Get Public Route Table ID")
print(pub_rt_id, "\n")

#Associate Public Subnet 1 to Public Route table
response_ass_rt_pub_sub1 = route_tables.assoc_rt_subnet(pub_rt_id, pub_sub_1_id)
print("Associate Public Subnet 1 to Public Route table Response")
print(response_ass_rt_pub_sub1, "\n")

#Associate Public Subnet 2 to Public Route table
response_ass_rt_pub_sub2 = route_tables.assoc_rt_subnet(pub_rt_id, pub_sub_2_id)
print("Associate Public Subnet 2 to Public Route table Response")
print(response_ass_rt_pub_sub2, "\n")


#Get Private Route Table ID
priv_rt_id = response_private_rt["RouteTable"]["RouteTableId"]
print("Get Public Route Table ID")
print(pub_rt_id, "\n")

#Associate Private Subnet 1 to Private Route table
response_ass_rt_priv_sub1 = route_tables.assoc_rt_subnet(priv_rt_id, priv_sub_1_id)
print("Associate Private Subnet 1 to Private Route table Response")
print(response_ass_rt_priv_sub1, "\n")

#Associate Private Subnet 2 to Private Route table
response_ass_rt_priv_sub2 = route_tables.assoc_rt_subnet(priv_rt_id, priv_sub_2_id)
print("Associate Private Subnet 2 to Private Route table Response")
print(response_ass_rt_priv_sub2, "\n")

#Associate Private Subnet 3 to Private Route table
response_ass_rt_priv_sub3 = route_tables.assoc_rt_subnet(priv_rt_id, priv_sub_3_id)
print("Associate Private Subnet 3 to Private Route table Response")
print(response_ass_rt_priv_sub3, "\n")

#Associate Private Subnet 4 to Private Route table
response_ass_rt_priv_sub4 = route_tables.assoc_rt_subnet(priv_rt_id, priv_sub_4_id)
print("Associate Private Subnet 4 to Private Route table Response")
print(response_ass_rt_priv_sub4, "\n")
