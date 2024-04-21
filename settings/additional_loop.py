"""
Creating additional loop for executing ascync functions syncronously
"""
import asyncio

loop = asyncio.get_event_loop()
print('[service] Additional async loop started')
