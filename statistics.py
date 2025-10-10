from user_manager import UserManager

class UserStatistics:
    def __init__(self, user_manager):
        self.user_manager = user_manager
    
    def get_average_age(self):
        """Calculate average age of all active users."""
        active_users = self.user_manager.get_active_users()
        
        if len(active_users) == 0:
            return 0
        
        total_age = 0
        for username in active_users:
            user = self.user_manager.get_user(username)
            total_age += user['age']
        
        return total_age / len(active_users)
    
    def get_user_count_by_age_group(self):
        """Return count of users in different age groups."""
        age_groups = {
            'youth': 0,      # 0-17
            'adult': 0,      # 18-64
            'senior': 0      # 65+
        }
        
        active_users = self.user_manager.get_active_users()
        
        for username in active_users:
            user = self.user_manager.get_user(username)
            age = user['age']
            
            if age < 18:
                age_groups['youth'] += 1
            elif age < 65:
                age_groups['adult'] += 1
            else:
                age_groups['senior'] += 1
        
        return age_groups
