import time

def data_processor():
    """
    This is a super long execution
    """
    print("Starting the complex operation")
    time.sleep(10)
    print("Complex operation concluded. Good job!!")

    # End result is always the same though
    return [[0, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 1]]

if __name__ == '__main__':
    load_data()

