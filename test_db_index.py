#!/usr/bin/env python
from db_index import *

if __name__ == "__main__":
    client = DBIndexClient('client.db')
    server = DBIndexServer('server.db', client.get_iv())
    tokens = client.gen_insert_equal_tokens('add', 'people', b'12345', 'age', (49).to_bytes(1, 'big'))
    server.insert_equal(tokens)
    tokens = client.gen_insert_equal_tokens('add', 'people', b'56432', 'age', (49).to_bytes(1, 'big'))
    server.insert_equal(tokens)

    tokens = client.gen_search_equal_tokens('people', 'age', (49).to_bytes(1, 'big'))
    print(server.search_equal(tokens))

    tokens = client.gen_insert_range_tokens('add', 'people', b'56432', 'age', 49, 8)
    server.insert_range(tokens)
    tokens = client.gen_insert_range_tokens('add', 'people', b'999100', 'age', 60, 8)
    server.insert_range(tokens)

    tokens = client.gen_search_range_tokens('people', 'age', 66, 77, 8)
    print(server.search_range(tokens))
