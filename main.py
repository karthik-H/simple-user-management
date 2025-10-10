from user_manager import UserManager
from statistics import UserStatistics

def main():
    # Initialize the user manager
    manager = UserManager()
    stats = UserStatistics(manager)
    
    # Add some users
    manager.add_user("alice", "alice@example.com", 25)
    manager.add_user("bob", "bob@example.com", 35)
    manager.add_user("charlie", "charlie@example.com", 70)
    manager.add_user("diana", "diana@example.com", 16)
    
    # Display statistics
    print(f"Average age: {stats.get_average_age():.1f}")
    print(f"Age groups: {stats.get_user_count_by_age_group()}")
    
    # Deactivate a user
    manager.deactivate_user("bob")
    
    print("\nAfter deactivating Bob:")
    print(f"Active users: {manager.get_active_users()}")
    print(f"Average age: {stats.get_average_age():.1f}")
    print(f"Age groups: {stats.get_user_count_by_age_group()}")
    
    # Update user email
    manager.update_user_email("alice", "alice.new@example.com")
    user = manager.get_user("alice")
    print(f"\nAlice's new email: {user['email']}")

if __name__ == "__main__":
    main()
