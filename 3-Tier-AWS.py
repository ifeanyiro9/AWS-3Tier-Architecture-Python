import boto3

ec2 = boto3.client('ec2')

def create_custom_vpc(cidr_block, tags_key, tags_value):
    """
    Function to create a custom VPC.

    Args:
        cidr_block (str): The CIDR block for the VPC.
        tags_key (str): The key for the VPC tag.
        tags_value (str): The value for the VPC tag.

    Returns:
        dict: The response from the create_vpc API call.
    """

    response = ec2.create_vpc(
        CidrBlock=cidr_block,
        TagSpecifications=[
            {
                'ResourceType': 'vpc',
                'Tags': [
                    {
                        'Key': tags_key,
                        'Value': tags_value
                    },
                ]
            },
        ]
    )
    return response


def create_custom_subnet(az, cidr_block, vpc_id, tags_key, tags_value):
    """
    Function to create a custom subnet.

    Args:
        az (str): The availability zone for the subnet.
        cidr_block (str): The CIDR block for the subnet.
        vpc_id (str): The ID of the VPC in which the subnet will be created.
        tags_key (str): The key for the subnet tag.
        tags_value (str): The value for the subnet tag.

    Returns:
        dict: The response from the create_subnet API call.
    """
    
    response = ec2.create_subnet(
        TagSpecifications=[
            {
                'ResourceType': 'subnet',
                'Tags': [
                    {
                        'Key': tags_key,
                        'Value': tags_value
                    },
                ]
            },
        ],
        AvailabilityZone=az,
        CidrBlock=cidr_block,
        VpcId=vpc_id,
    )
    return response


# Create the VPC
response_vpc = create_custom_vpc('10.0.0.0/16','Name', '3Tier-VPC')
print(response_vpc)
print("")

#Get VPC id
vpc_id = response_vpc["Vpc"]["VpcId"] 
print(vpc_id)
print("")

# Create public subnet 1
response_pub_sub1 = create_custom_subnet("us-east-1a", "10.0.0.0/20", vpc_id, "Name", "3Tier-Pub-Sub1")
print(response_pub_sub1)
print("")

# Create public subnet 2
response_pub_sub2 = create_custom_subnet("us-east-1b", "10.0.16.0/20", vpc_id, "Name", "3Tier-Pub-Sub2")
print(response_pub_sub2)

# Create private subnet 1
response_priv_sub1 = create_custom_subnet("us-east-1a", "10.0.128.0/20", vpc_id, "Name", "3Tier-Priv-Sub1")
print(response_priv_sub1)
print("")

# Create private subnet 2
response_priv_sub2 = create_custom_subnet("us-east-1b", "10.0.144.0/20", vpc_id, "Name", "3Tier-Priv-Sub2")
print(response_priv_sub2)

print("")

# Create private subnet 3
response_priv_sub3 = create_custom_subnet("us-east-1a", "10.0.160.0/20", vpc_id, "Name", "3Tier-Priv-Sub3")
print(response_priv_sub1)
print("")

# Create private subnet 4
response_priv_sub4 = create_custom_subnet("us-east-1b", "10.0.178.0/20", vpc_id, "Name", "3Tier-Priv-Sub4")
print(response_priv_sub4)
