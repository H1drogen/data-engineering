import asyncio

import src.utils.server as server



async def fetch_banner_content():
    # TODO: implement your function here
    task = await server.get_banner_content()
    # output = await asyncio.gather(task)
    return task

async def get_lower_owners():
    task = server.get_owners()
    # output = asyncio.run(task)
    output = await asyncio.gather(task)
    output = output[0]
    for index in range(len(output)):
        output[index] = output[index].lower()
    return output

async def get_pets_by_owner(owner):
    try:
        task = server.get_cats_by_owner(owner)
        output = await asyncio.gather(task)
        dictionary = {}
        dictionary['pets'] = output[0]
        return dictionary
    except:
        dictionary = {}
        dictionary['pets'] = []
        dictionary['message'] = 'missing not found'
        return dictionary


async def get_all_cats():
    list_of_owners = await get_lower_owners()
    owner_and_pets = []

    async def make_dictionary(owner):
        dictionary = {}
        dictionary['owner'] = owner
        dictionary['cats'] = await server.get_cats_by_owner(owner)
        return dictionary

    task = []
    for owner in list_of_owners:
        task.append(make_dictionary(owner))

    item = await asyncio.gather(*task)
    return item


async def get_cat_pics(list_of_strings):

    tasks = []
    async def something(string):
        try:
            return await server.get_pic(string)
        except Exception:
            return "placeholder_cat.png"

    for string in list_of_strings:
        tasks.append(something(string))

    output = await asyncio.gather(*tasks)
    return output

async def retry_legacy_server():
    server_response = 500
    while server_response == 500:
        variable = await server.get_legacy_status()
        # {"status": 200, "message": "Internal Server Error"}
        if variable['status'] == 200:
            return variable['message']
