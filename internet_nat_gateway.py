import boto3
import main

ec2 = boto3.client('ec2')
vpc_id = main.vpc_id


def create_attach_internet_gateway(vpc_id, tags_key, tags_value):
    #Create a Internet Gateway
    response_create_ig = ec2.create_internet_gateway(
        TagSpecifications=[
            {
                'ResourceType': 'internet-gateway',
                'Tags': [
                    {
                        'Key': tags_key,
                        'Value': tags_value
                    },
                ]
            },
        ],
    )

    ig_id = response_create_ig["InternetGatway"]["InternetGatewayId"]

    #Attach Internet Gateway to VPC
    response_attach_ig = ec2.attach_internet_gateway(
        InternetGatewayId= ig_id,
        VpcId=vpc_id,
    )
    print(response_attach_ig)

    return response_create_ig


def create_nat_gateway(subnet_id, tags_key_ip, tags_value_ip, tags_key_nat, tags_value_nat):
    
    #Create Elastic IP
    response_eip = ec2.allocate_address(
        Domain='vpc',
        TagSpecifications=[
            {
                'ResourceType': 'elastic-ip',
                'Tags': [
                    {
                        'Key': tags_key_ip,
                        'Value': tags_value_ip
                    },
                ]
            },
        ]
    )

    eip_id = response_eip["AllocationId"]
    
    #Create a NAT Gateway
    response_nat = ec2.create_nat_gateway(
        AllocationId=eip_id,
        SubnetId= subnet_id,
        TagSpecifications=[
            {
                'ResourceType': 'natgateway',
                'Tags': [
                    {
                        'Key': tags_key_nat,
                        'Value': tags_value_nat
                    },
                ]
            },
        ],
    )
    return response_nat
