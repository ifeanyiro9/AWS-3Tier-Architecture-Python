import boto3

ec2 = boto3.client('ec2')

def create_pub_rt(vpc_id, dest_cidr, int_gw_id, tags_key, tags_value):
    #create public routetable
    response_rt = ec2.create_route_table(
        VpcId=vpc_id,
        TagSpecifications=[
            {
                'ResourceType': 'route-table',
                'Tags': [
                    {
                        'Key': tags_key,
                        'Value': tags_value
                    },
                ]
            },
        ]
    )
    
    rt_id = response_rt["RouteTable"]["RouteTableId"]

    #Create route for routetable to internet gateway
    response_route = ec2.create_route(
        DestinationCidrBlock=dest_cidr,
        GatewayId=int_gw_id,
        RouteTableId=rt_id,
    )

    print("Create Private Route to Natgateway Responce")
    print(response_route)
    print("")

    return response_rt




def create_priv_rt(vpc_id, dest_cidr, nat_gw_id, tags_key, tags_value):
    #create private routetable
    response_rt = ec2.create_route_table(
        VpcId=vpc_id,
        TagSpecifications=[
            {
                'ResourceType': 'route-table',
                'Tags': [
                    {
                        'Key': tags_key,
                        'Value': tags_value
                    },
                ]
            },
        ]
    )

    rt_id = response_rt["RouteTable"]["RouteTableId"]
   
    #Create route for routetable to natgateway
    response_route = ec2.create_route(
        DestinationCidrBlock=dest_cidr,
        NatGatewayId=nat_gw_id,
        RouteTableId=rt_id,
    )

    print("Create Private Route to Natgateway Responce")
    print(response_route)
    print("")

    return response_rt
