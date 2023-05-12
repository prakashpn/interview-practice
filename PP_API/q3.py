import asyncio


async def string_manipulation(para):
    vowels = ["a", "e", "i", "o", "u"]
    split_para = para.split(".")
    print("act ->", split_para)
    after_remove_list = []
    for x in split_para:
        after_remove = [i for i in x if i not in vowels]
        after_remove = "".join(after_remove)
        print("before reverse", after_remove)
        after_remove = after_remove[::-1]
        after_remove_list.append(after_remove)

    print("remov-->", after_remove_list)
    return after_remove_list


async def main(para):
    output = await string_manipulation(para)
    joined_output = ".".join(output)
    return joined_output


if __name__ == '__main__':
    paragr = """Gardening is my favourite hobby. I own a small plot of land next to our house. I cultivate gardening there. Every day, I spend half an hour gardening. After returning from my morning walk, I go to my garden with a spade and a bucket of water. I prepare the soil, prune the plants, and water them. """
    output = asyncio.run(main(paragr))
    print(output)
