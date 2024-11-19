from fake_useragent import UserAgent
useragent = UserAgent()


def get_random_useragent():
    return useragent.random
