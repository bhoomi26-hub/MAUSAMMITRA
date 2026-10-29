"""
===================================================================
 MAUSAM MITRA (मौसम मित्र) - Main Application Entry Point
 Serves the complete frontend and REST API backend server.
===================================================================
"""

import os
import sys

# Ensure backend directory is in python path
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend'))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from backend.app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'development') == 'development'

    print("\n" + "="*65)
    print(" MAUSAM MITRA - Server Ready")
    print(f" Frontend & API URL: http://127.0.0.1:{port}/")
    print(f" Health Endpoint:   http://127.0.0.1:{port}/api/health")
    print("="*65 + "\n")

    app.run(host='0.0.0.0', port=port, debug=debug)

