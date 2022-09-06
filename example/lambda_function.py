import os
import gnupg
import boto3
from botocore.exceptions import (
    ClientError
)

session = boto3.Session( aws_access_key_id='AKIAQJZNGEWMR2XSRKWS', aws_secret_access_key='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')
s3 = session.resource('s3')

def handler(event, context):
    print("algo")
    my_bucket = s3.Bucket('merchantkey')

    items = []
    
    for my_bucket_object in my_bucket.objects.all():
        file = my_bucket_object.key
        items.append(file)
        my_bucket.download_file(f"{file}", f"/tmp/{file}") 
    
    for file in items:
        result = encrypt_file(f"/tmp/{file}") 
        print(result)
    
    return f'Gpg encrypt ok'       


def encrypt_file(file_name):
    gpg_homeshort = "/tmp"
    gpg = gnupg.GPG(gnupghome=gpg_homeshort, verbose=True)
    key = open("XX_AP_UPL_MERCHANT_DOCS_NPRD_.key", "rb").read()
    gpg.import_keys(key)
    gpg.list_keys() 
    with open(file_name, "rb") as f:
        status = gpg.encrypt_file(
            f,
            recipients=["Luis.Salazar@Millicom.com"],
            output=f"/tmp/{file_name}.gpg",
            always_trust=True,
            extra_args=["--yes"],
        )
        print(status) 
    lst = os.listdir("/tmp")
    
    return lst


 
