#!/usr/bin/env python3
"""
Ground Station Contact Scheduler Example

This script demonstrates automated contact scheduling for AWS Ground Station
using best practices for conflict resolution and optimization.

Usage:
    python contact-scheduler.py --satellite-id arn:aws:groundstation:us-east-2:123456789012:satellite:12345678-1234-1234-1234-123456789012 --start-time 2025-01-27T10:00:00Z --duration 600

Requirements:
    - boto3
    - python-dateutil
"""

import boto3
import json
import argparse
import logging
from datetime import datetime, timedelta
from dateutil import parser
from botocore.exceptions import ClientError, BotoCoreError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class GroundStationScheduler:
    """
    Ground Station contact scheduler with conflict resolution and optimization
    """
    
    def __init__(self, region='us-east-1'):
        """
        Initialize the scheduler
        
        Args:
            region (str): AWS region for Ground Station operations
        """
        self.region = region
        self.gs_client = boto3.client('groundstation', region_name=region)
        self.cloudwatch = boto3.client('cloudwatch', region_name=region)
        
    def list_available_antennas(self, start_time, end_time):
        """
        List available antennas for the specified time window
        
        Args:
            start_time (datetime): Start of the time window
            end_time (datetime): End of the time window
            
        Returns:
            list: Available ground stations
        """
        try:
            response = self.gs_client.list_ground_stations()
            available_stations = []
            
            for station in response.get('groundStationList', []):
                # Check if station is available during the time window
                # This is a simplified check - in practice, you'd query actual availability
                available_stations.append({
                    'groundStationId': station['groundStationId'],
                    'groundStationName': station['groundStationName'],
                    'region': station['region']
                })
                
            logger.info(f"Found {len(available_stations)} available ground stations")
            return available_stations
            
        except ClientError as e:
            logger.error(f"Error listing ground stations: {e}")
            return []
    
    def check_contact_conflicts(self, start_time, end_time, ground_station_id):
        """
        Check for existing contact conflicts
        
        Args:
            start_time (datetime): Proposed contact start time
            end_time (datetime): Proposed contact end time
            ground_station_id (str): Ground station ID to check
            
        Returns:
            bool: True if conflicts exist, False otherwise
        """
        try:
            # List existing contacts in the time window
            response = self.gs_client.list_contacts(
                startTime=start_time - timedelta(hours=1),
                endTime=end_time + timedelta(hours=1),
                groundStation=ground_station_id,
                statusList=['SCHEDULED', 'EXECUTING']
            )
            
            existing_contacts = response.get('contactList', [])
            
            for contact in existing_contacts:
                contact_start = contact['startTime']
                contact_end = contact['endTime']
                
                # Check for time overlap
                if (start_time < contact_end and end_time > contact_start):
                    logger.warning(f"Conflict detected with contact {contact['contactId']}")
                    return True
                    
            return False
            
        except ClientError as e:
            logger.error(f"Error checking conflicts: {e}")
            return True  # Assume conflict if we can't check
    
    def calculate_optimal_contact_window(self, satellite_id, preferred_start, duration_seconds):
        """
        Calculate optimal contact window considering satellite passes and conflicts
        
        Args:
            satellite_id (str): Satellite identifier
            preferred_start (datetime): Preferred start time
            duration_seconds (int): Contact duration in seconds
            
        Returns:
            dict: Optimal contact parameters or None if no suitable window found
        """
        # This is a simplified implementation
        # In practice, you'd use satellite orbital data and prediction algorithms
        
        search_window_hours = 24
        search_start = preferred_start
        search_end = preferred_start + timedelta(hours=search_window_hours)
        
        # Get available ground stations
        available_stations = self.list_available_antennas(search_start, search_end)
        
        if not available_stations:
            logger.error("No available ground stations found")
            return None
        
        # Try each ground station
        for station in available_stations:
            # Try different time slots within the search window
            current_time = search_start
            while current_time < search_end:
                contact_end = current_time + timedelta(seconds=duration_seconds)
                
                # Check if this time slot has conflicts
                if not self.check_contact_conflicts(
                    current_time, 
                    contact_end, 
                    station['groundStationId']
                ):
                    logger.info(f"Found optimal window: {current_time} to {contact_end}")
                    return {
                        'startTime': current_time,
                        'endTime': contact_end,
                        'groundStationId': station['groundStationId'],
                        'groundStationName': station['groundStationName']
                    }
                
                # Move to next time slot (15-minute intervals)
                current_time += timedelta(minutes=15)
        
        logger.error("No suitable contact window found")
        return None
    
    def schedule_contact(self, satellite_id, mission_profile_arn, contact_params):
        """
        Schedule a Ground Station contact
        
        Args:
            satellite_id (str): Satellite identifier
            mission_profile_arn (str): ARN of the mission profile
            contact_params (dict): Contact parameters from optimization
            
        Returns:
            str: Contact ID if successful, None otherwise
        """
        try:
            # Note: satellite_id should be a UUID format satellite ARN
            # Format: arn:aws:groundstation:region:account:satellite:uuid
            response = self.gs_client.reserve_contact(
                missionProfileArn=mission_profile_arn,
                satelliteArn=satellite_id,  # Expecting full satellite ARN
                startTime=contact_params['startTime'],
                endTime=contact_params['endTime'],
                groundStation=contact_params['groundStationId'],
                tags={
                    'ScheduledBy': 'AutomatedScheduler',
                    'SatelliteId': satellite_id,
                    'GroundStation': contact_params['groundStationName']
                }
            )
            
            contact_id = response['contactId']
            logger.info(f"Successfully scheduled contact {contact_id}")
            
            # Send custom metric to CloudWatch
            self.send_scheduling_metric('ContactScheduled', 1)
            
            return contact_id
            
        except ClientError as e:
            logger.error(f"Error scheduling contact: {e}")
            self.send_scheduling_metric('ContactSchedulingFailed', 1)
            return None
    
    def send_scheduling_metric(self, metric_name, value):
        """
        Send custom metrics to CloudWatch
        
        Args:
            metric_name (str): Name of the metric
            value (float): Metric value
        """
        try:
            self.cloudwatch.put_metric_data(
                Namespace='GroundStation/Scheduler',
                MetricData=[
                    {
                        'MetricName': metric_name,
                        'Value': value,
                        'Unit': 'Count',
                        'Timestamp': datetime.utcnow()
                    }
                ]
            )
        except ClientError as e:
            logger.warning(f"Failed to send metric {metric_name}: {e}")
    
    def get_contact_status(self, contact_id):
        """
        Get the status of a scheduled contact
        
        Args:
            contact_id (str): Contact ID to check
            
        Returns:
            dict: Contact status information
        """
        try:
            response = self.gs_client.describe_contact(contactId=contact_id)
            return {
                'contactId': contact_id,
                'status': response['contactStatus'],
                'startTime': response['startTime'],
                'endTime': response['endTime'],
                'groundStation': response['groundStation']
            }
        except ClientError as e:
            logger.error(f"Error getting contact status: {e}")
            return None

def main():
    """
    Main function for command-line usage
    """
    parser = argparse.ArgumentParser(description='Ground Station Contact Scheduler')
    parser.add_argument('--satellite-id', required=True, help='Satellite ARN (e.g., arn:aws:groundstation:region:account:satellite:uuid)')
    parser.add_argument('--start-time', required=True, help='Preferred start time (ISO format)')
    parser.add_argument('--duration', type=int, required=True, help='Contact duration in seconds')
    parser.add_argument('--mission-profile-arn', required=True, help='Mission profile ARN')
    parser.add_argument('--region', default='us-east-1', help='AWS region')
    parser.add_argument('--dry-run', action='store_true', help='Calculate optimal window without scheduling')
    
    args = parser.parse_args()
    
    # Parse start time
    try:
        preferred_start = parser.parse(args.start_time)
    except ValueError as e:
        logger.error(f"Invalid start time format: {e}")
        return 1
    
    # Initialize scheduler
    scheduler = GroundStationScheduler(region=args.region)
    
    # Calculate optimal contact window
    logger.info(f"Calculating optimal contact window for satellite {args.satellite_id}")
    optimal_params = scheduler.calculate_optimal_contact_window(
        args.satellite_id,
        preferred_start,
        args.duration
    )
    
    if not optimal_params:
        logger.error("Could not find suitable contact window")
        return 1
    
    logger.info(f"Optimal contact window: {optimal_params}")
    
    if args.dry_run:
        logger.info("Dry run mode - contact not scheduled")
        return 0
    
    # Schedule the contact
    contact_id = scheduler.schedule_contact(
        args.satellite_id,
        args.mission_profile_arn,
        optimal_params
    )
    
    if contact_id:
        logger.info(f"Contact scheduled successfully: {contact_id}")
        return 0
    else:
        logger.error("Failed to schedule contact")
        return 1

if __name__ == '__main__':
    exit(main())
