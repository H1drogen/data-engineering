import boto3

client = boto3.client("secretsmanager")


def make_secret(identifier, id, password):
    try:
        client.create_secret(
            Name=identifier, SecretString=f'{{"username":"{id}","password":"{password}"}}'
        )
        return "Secret saved."
    except Exception as e:
        return f"{e.args[0]}"


def list_secrets():
    secrets = []
    list = client.list_secrets(IncludePlannedDeletion=False)["SecretList"]
    for entry in list:
        secrets.append(entry["Name"])
    return secrets


def get_secret(identifier, filename = "./secrets.txt"):
    try:
        result = client.get_secret_value(SecretId=identifier)["SecretString"]
        with open(filename, "a+") as file:
            file.write(result)
        return "Secrets stored in local file secrets.txt."
    except:
        return f"Secret {identifier} is not a valid secret."


def delete_secret(identifer):
    try:
        client.delete_secret(SecretId=identifer, ForceDeleteWithoutRecovery=True)
        return "Deleted"
    except:
        return f"Secret {identifer} is not a valid secret."
