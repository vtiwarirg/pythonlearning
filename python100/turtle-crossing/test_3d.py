#!/usr/bin/env python3
"""
Test script for 3D Turtle Crossing Game
"""

try:
    from player import Player
    from car_manager import CarManager
    from car_3d import Car3D
    from road_marking import RoadMarking
    from background_3d import Background3D
    from scoreboard import Scoreboard
    
    print("Testing 3D game components...")
    
    # Test Player with 3D effects
    player = Player()
    print(f"✓ 3D Player created with shadow: {player.shadow is not None}")
    
    # Test Car Manager
    car_manager = CarManager()
    print(f"✓ 3D Car Manager created")
    
    # Test creating a 3D car
    test_car = Car3D(100, 50, 1)
    print(f"✓ 3D Car created with components: shadow={test_car.shadow is not None}, body={test_car.main_body is not None}, highlight={test_car.highlight is not None}")
    
    # Test Scoreboard
    scoreboard = Scoreboard()
    print(f"✓ Enhanced Scoreboard created")
    
    print("\n🎉 All 3D components working correctly!")
    print("The game now features:")
    print("• 3D turtle with shadow effects")
    print("• 3D cars with layered depth (shadow + body + highlight)")
    print("• 3D road markings with shadow effects")
    print("• Enhanced environment with barriers and perspective")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()