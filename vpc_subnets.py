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


