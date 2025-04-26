def my_callback(str):
    print(f"コールバックが呼ばれました: {str}")

def my_function(callback, message):
    print("関数が実行されました")

    callback(message)

if __name__ == "__main__":
    my_function(my_callback, "Hello")
