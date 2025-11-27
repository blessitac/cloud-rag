#!/usr/bin/env python3
"""
Seed script for creating demo tenant and user data.

Usage:
    source .venv/bin/activate
    cd backend
    python -m scripts.seed_demo_data

This script is idempotent - safe to run multiple times.
"""

import sys
import os
from uuid import uuid4
# Add the parent directory to the path so we can import app modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.database import SessionLocal
from app.models.domain import Tenant, User
import app.models.domain  # noqa: F401  # ensures ALL models are imported (side effect)


def seed_demo_data():
    """Create demo tenant and user if they don't exist."""
    db = SessionLocal()
    
    try:
        # Check if demo tenant exists
        demo_tenant = db.query(Tenant).filter(Tenant.slug == "demo").first()
        
        if not demo_tenant:
            print("Creating demo tenant...")
            demo_tenant = Tenant(
                id=uuid4(),
                name="Demo Tenant",
                slug="demo"
            )
            db.add(demo_tenant)
            db.commit()
            db.refresh(demo_tenant)
            print(f"✓ Created demo tenant with ID: {demo_tenant.id}")
        else:
            print(f"✓ Demo tenant already exists with ID: {demo_tenant.id}")
        
        # Check if demo user exists
        demo_user = db.query(User).filter(
            User.tenant_id == demo_tenant.id,
            User.email == "demo@example.com"
        ).first()
        
        if not demo_user:
            print("Creating demo user...")
            demo_user = User(
                id=uuid4(),
                tenant_id=demo_tenant.id,
                email="demo@example.com",
                display_name="Demo User",
                role="admin"
            )
            db.add(demo_user)
            db.commit()
            db.refresh(demo_user)
            print(f"✓ Created demo user with ID: {demo_user.id}")
        else:
            print(f"✓ Demo user already exists with ID: {demo_user.id}")
        
        print("\n" + "="*50)
        print("DEMO DATA READY")
        print("="*50)
        print(f"Tenant ID: {demo_tenant.id}")
        print(f"User ID: {demo_user.id}")
        print(f"User Email: {demo_user.email}")
        print(f"User Role: {demo_user.role}")
        print("\nTo test the /auth/me endpoint, use this header:")
        print(f"X-Demo-User-Id: {demo_user.id}")
        print("="*50)
        
    except Exception as e:
        print(f"Error seeding demo data: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed_demo_data()