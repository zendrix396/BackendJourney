import asyncio
import time
import httpx

# Simulating an API call with delay
def sync_get_user(user_id):
    print(f"Starting sync fetch for user {user_id}")
    time.sleep(1)  # Simulates API delay
    print(f"Finished sync fetch for user {user_id}")
    return f"User {user_id} data"

# Async version of the same function
async def async_get_user(user_id):
    print(f"Starting async fetch for user {user_id}")
    await asyncio.sleep(1)  # Simulates API delay
    print(f"Finished async fetch for user {user_id}")
    return f"User {user_id} data"

# Synchronous way to fetch multiple users
def get_users_sync():
    start_time = time.time()
    
    # Get 3 users one after another
    users = []
    for user_id in range(1, 4):
        users.append(sync_get_user(user_id))
    
    end_time = time.time()
    print(f"\nSync total time: {end_time - start_time:.2f} seconds")
    return users

# Asynchronous way to fetch multiple users
async def get_users_async():
    start_time = time.time()
    
    # Create tasks for all users at once
    tasks = []
    for user_id in range(1, 4):
        tasks.append(async_get_user(user_id))
    
    # Wait for all tasks to complete
    users = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"\nAsync total time: {end_time - start_time:.2f} seconds")
    return users

# Main function to run both examples
async def main():
    print("Running synchronous version:")
    sync_results = get_users_sync()
    
    print("\nRunning asynchronous version:")
    async_results = await get_users_async()

# Run the program
if __name__ == "__main__":
    asyncio.run(main())