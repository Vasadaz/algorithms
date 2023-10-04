from collections import deque


def get_seller(sellers: dict[str:list[tuple[str, str]]], fruit: str) -> str:
    search_queue = deque(sellers['I'])
    checked_sellers = []

    while search_queue:
        seller, product = search_queue.popleft()

        if not seller in checked_sellers:
            if product == fruit:
                return f'{fruit} seller - {seller}!'

            else:
                search_queue += sellers[seller]
                checked_sellers.append(seller)

    return f'The {fruit} seller was not found...'



if __name__ == '__main__':
    my_sellers = {
        'I': [('Bob', 'Apple'), ('Alice', 'Banana'), ('Claire', 'Lime')],
        'Bob': [('Anuj', 'Raspberry'), ('Peggy', 'Pear')],
        'Alice': [('Peggy', 'Pear')],
        'Claire': [('Thom', 'Orange'), ('Jonny', 'Mango')],
        'Anuj': [],
        'Peggy': [],
        'Thom': [],
        'Jonny': [],
    }

    print(get_seller(my_sellers, 'Mango'))
    print(get_seller(my_sellers, 'Pear'))
    print(get_seller(my_sellers, 'Strawberry'))
