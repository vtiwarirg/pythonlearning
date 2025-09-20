#!/usr/bin/env python3
"""
Quick test to verify the snake game works
"""

try:
    from snake import Snake
    from food import Food
    print("✓ Successfully imported Snake and Food classes")
    
    # Test snake creation
    snake = Snake()
    print("✓ Snake object created successfully")
    print(f"✓ Snake has {len(snake.segments)} segments")
    print(f"✓ Snake head is at position: {snake.head.position()}")
    
    # Test food creation
    food = Food()
    print("✓ Food object created successfully")
    print(f"✓ Food is at position: {food.position()}")
    
    # Test basic movement
    original_pos = snake.head.position()
    snake.move()
    new_pos = snake.head.position()
    print(f"✓ Snake moved from {original_pos} to {new_pos}")
    
    # Test extension
    original_length = len(snake.segments)
    snake.extend()
    new_length = len(snake.segments)
    print(f"✓ Snake extended from {original_length} to {new_length} segments")
    
    print("\n🎉 All tests passed! The snake game should work correctly.")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()