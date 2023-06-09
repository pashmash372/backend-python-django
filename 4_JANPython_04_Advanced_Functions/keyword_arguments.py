# advanced functions

def my_new_function(input_one, input_two):
    print(input_one, input_two)
    return True


# somehow - gets tweets from particular user on twitter
# Scrapping or API integration
# what is scrapping? - https://en.wikipedia.org/wiki/Web_scraping

# def get_tweets(username, includes_retweets, not_older_than, max_tweets_count):
#     pass
#
#
# get_tweets('elonmusk', True, '2020-01-01', 100)
# get_tweets('championswimmer', False, '2020-01-01', 100)
# get_tweets('bill gates', False, '2020-01-01', 100)


def get_tweets(username, includes_retweets, not_older_than,
               max_tweets_count=100):  # default value for max_tweets_count is 100 if not provided  by user in
    # function call , name of syntax is keyword argument
    includes_retweets = 'yes' if includes_retweets else 'no'
    print(
        f"Getting tweets for {username} which are not older than  {not_older_than} and includes retweets {includes_retweets} and max tweets count {max_tweets_count}")

    return True


get_tweets('elonmusk', True, '2020-01-01', 1000)    # positional arguments - order matters  # 1000 is overriding
# default value    # 1000 is overriding default value   # 1000 is overriding default value

# any default value should be at the end of the function definition not in between or at the start




#  usecases of default values in functions - 1. to provide default value to an argument
# 2. to provide default value to an argument which is optional
# 3. to provide default value to an argument which is optional and is at the end of the function definition
# 4. to provide default value to an argument which is optional and is at the end of the function definition and
# is not provided by user in function call
# 5. to provide default value to an argument which is optional and is at the end of the function definition and
# used in pandas library



