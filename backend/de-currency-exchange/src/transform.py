import json

def lambda_handler(event, context):
    """Transforms the data to give the required rates against USD.

    The output should include the reverse rate to 6 decimal places.

    Args:
        event: a dictionary in the form output by the extract function.
        context: supplied by AWS

    Returns:
        dictionary e.g. {
            "eur": {
                "rate": 1.08167213,
                "reverse_rate": 0.924495
            }
        }

    """
    # replace this code
    return {"eur": {"rate": event['eur']['usd'], "reverse_rate": 1 / event['eur']['usd']}}
