class EventEmitter:
    def __init__(self):
        self.events = {}

    def on(self, event, callback):
        "コールバックを登録する"
        if event not in self.events:
            self.events[event] = []
        self.events[event].append(callback)

    def emit(self, event, *args, **kwargs):
        "イベントを発火する"
        callbacks = self.events.get(event, [])
        for callback in callbacks:
            try:
                callback(*args, **kwargs)
            except Exception as e:
                print(f"Error in callback '{event}': {e}")

emitter = EventEmitter()

# コールバック関数を登録
def on_hello(name):
    print(f"Hello, {name}!")

def on_goodbye(name):
    print(f"Goodbye, {name}!")

emitter.on('greet', on_hello)
emitter.on('farewell', on_goodbye)

# イベントを発火
emitter.emit('greet', 'Taro')    # → Hello, Taro!
emitter.emit('farewell', 'Hanako')  # → Goodbye, Hanako!
