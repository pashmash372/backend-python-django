from my_library import log_datetime, measure_performance  # import the decorator


@log_datetime  # apply the decorator to the function
def daily_backup():  # define the function
    print('Daily backup job has finished')


@log_datetime  # apply the decorator to the function
def daily_cleanup():  # define the function
    print('Daily cleanup job has finished')


# daily_backup()  # run the function
# daily_cleanup()  # run the function


@measure_performance
def iterate_numbers(max_count):
    print(f"Going to iterate {max_count} times")
    for i in range(max_count):
        i = i


iterate_numbers(1000000)
