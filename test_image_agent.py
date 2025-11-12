#!/usr/bin/env python3
"""
Interactive test script for the image_agent_pause_approval
"""

import asyncio
from image_agent_pause_approval import image_app


async def test_interactive():
    """Test the image agent with a conversation"""
    
    print("=" * 60)
    print("Testing Image Generation Agent")
    print("=" * 60)
    
    # Test 1: Single image (auto-approved)
    print("\n[TEST 1] Requesting 1 image (should auto-approve)...")
    response1 = await image_app.run("Generate 1 image of a sunset")
    print(f"Response: {response1}")
    
    # Test 2: Multiple images (requires approval)
    print("\n[TEST 2] Requesting 3 images (should require approval)...")
    response2 = await image_app.run("Generate 3 images of cute cats")
    print(f"Response: {response2}")
    
    # Test 3: Simulate approval
    print("\n[TEST 3] Testing approval flow...")
    from image_agent_pause_approval import place_image_order, approve_image_order
    
    # Place a bulk order
    order = await place_image_order(prompt="abstract art", num_images=5)
    print(f"Order placed: {order}")
    
    if order.get("status") == "pending":
        token = order["approval_token"]
        print(f"\nApproval token: {token}")
        
        # Approve it
        print("Approving the order...")
        approved = await approve_image_order(token, approve=True)
        print(f"Approval result: {approved}")
        
        # Try to reject another order
        print("\n[TEST 4] Testing rejection...")
        order2 = await place_image_order(prompt="landscape", num_images=2)
        if order2.get("status") == "pending":
            token2 = order2["approval_token"]
            rejected = await approve_image_order(token2, approve=False)
            print(f"Rejection result: {rejected}")


async def test_agent_conversation():
    """Test natural conversation with the agent"""
    print("\n" + "=" * 60)
    print("Testing Agent Conversation Flow")
    print("=" * 60)
    
    session_id = "test_session_1"
    
    # Start a conversation
    print("\n[User]: I need 5 images of mountain landscapes")
    response = await image_app.run(
        "I need 5 images of mountain landscapes",
        session_id=session_id
    )
    print(f"[Agent]: {response}")


if __name__ == "__main__":
    asyncio.run(test_interactive())
    # Uncomment to test conversation:
    # asyncio.run(test_agent_conversation())

