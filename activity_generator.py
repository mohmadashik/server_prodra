import os
import random
from datetime import timedelta
from django.utils import timezone
from django.core.management import execute_from_command_line

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server_prodra.settings')
import django
django.setup()

# Import models after setting up Django environment
from activities.models import Activity
from django.contrib.auth.models import User

# Assuming you have some users in your database
user = User.objects.first()  # or create a user if none exists

# List of activities
activity_types = ['run', 'cycling']

# Sample names for activities
activity_names = ['Morning Run', 'Evening Run', 'Mountain Cycling', 'Road Cycling', 'Trail Run', 'Sprint Workout']

# Function to create random activity records
def create_sample_activities(num_records=100):
    for i in range(num_records):
        # Randomly select activity type
        activity_type = random.choice(activity_types)
        
        # Randomly select activity name
        name = random.choice(activity_names)
        
        # Random distance between 5 km and 50 km
        distance = round(random.uniform(5, 50), 2)
        
        # Random duration between 30 minutes and 2 hours
        duration = timedelta(minutes=random.randint(30, 120))
        
        # Random date within the past year
        date = timezone.now() - timedelta(days=random.randint(1, 365))
        
        # Random speed calculation (based on distance and duration)
        if activity_type == 'run':
            speed = round(distance / (duration.total_seconds() / 3600), 2)
        else:
            speed = round(distance / (duration.total_seconds() / 3600), 2)
        
        # Random notes
        notes = random.choice([None, "Great workout!", "Feeling strong!", "Need more practice.", "Amazing day for a run!", "Cycling was tough today."])
        
        # Random steps (for run activities, approx 100 steps per 1 km)
        steps = random.randint(3000, 10000) if activity_type == 'run' else None
        
        # Random photo path (simulating file storage)
        photos = f"/photos/{random.randint(1, 50)}.jpg" if random.choice([True, False]) else None
        
        # Create Activity record
        Activity.objects.create(
            name=name,
            distance=distance,
            duration=duration,
            date=date.strftime('%Y-%m-%d %H:%M:%S'),
            user=user,  # Ensure this user exists
            type=activity_type,
            photos=photos,
            speed=speed,
            notes=notes,
            steps=steps
        )

# Create 100 sample records
create_sample_activities(100)
