import Spectral_BLDC as Spectral
import time


Communication1 = Spectral.CanCommunication(bustype='slcan', channel='COM41', bitrate=1000000)
Motor = []

Motor.append(Spectral.SpectralCAN(node_id=0, communication=Communication1))
Motor.append(Spectral.SpectralCAN(node_id=1, communication=Communication1)) 
ž

timeout_setting = 0.00005
tick_cnt = 0

while True:

    # Send data to all motors
    #Motor[1].Send_data_pack_PD(-6000,0,0)
    #Motor[2].Send_data_pack_PD(6000,0,0)
    
    tick_cnt = tick_cnt  + 1

    Motor[0].Send_data_pack_1(None,4500,0)
    Motor[1].Send_data_pack_1(None,-4500,0)
  
    
    #Motor[3].Send_Respond_Encoder_data()
    #Motor[4].Send_Respond_Encoder_data()

    #Motor[1].Send_Limits(800000,2000)
    #Motor[2].Send_Limits(800000,2000)

    #Motor[1].Send_Respond_State_of_Errors()
    #Motor[2].Send_Respond_State_of_Errors()

    #Motor[1].Send_PD_Gains(0.012,0.001)
    #Motor[2].Send_PD_Gains(0.012,0.001)

    for i in range(1, 7):  # Loop 9-1=8 to check for received data
        message, UnpackedMessageID = Communication1.receive_can_messages(timeout=timeout_setting)
        print(f"unpack {i} is: {UnpackedMessageID}")

        # Check if UnpackedMessageID is not None 
        if UnpackedMessageID is not None:
            #print(Motor)
            # Update received id index; meaning that we received response from that CAN ID
            Motor[UnpackedMessageID[0]].UnpackData(message,UnpackedMessageID)
            print(f"Motor {UnpackedMessageID [0]}, speed is: {Motor[UnpackedMessageID[0]].speed}, current is {Motor[UnpackedMessageID[0]].current },pos is {Motor[UnpackedMessageID[0]].position}")
            """
            print(f"Motor {UnpackedMessageID[0]}, speed is: {Motor[UnpackedMessageID[0]].speed}")
            print(f"Error is: {Motor[UnpackedMessageID[0]].error}")
            print(f"Temperature rror is: {Motor[UnpackedMessageID[0]].temperature_error}")
            print(f"Encoder error is: {Motor[UnpackedMessageID[0]].encoder_error}")
            print(f"Vbus error is: {Motor[UnpackedMessageID[0]].vbus_error}")
            print(f"Driver error is: {Motor[UnpackedMessageID[0]].driver_error}")
            print(f"Velocity error is: {Motor[UnpackedMessageID[0]].velocity_error}")
            print(f"Current error is: {Motor[UnpackedMessageID[0]].current_error}")
            print(f"Estop error is: {Motor[UnpackedMessageID[0]].estop_error}")
            print(f"Watchdog error is: {Motor[UnpackedMessageID[0]].watchdog_error}")
            print(f"Calibrated is: {Motor[UnpackedMessageID[0]].calibrated}")
            print(f"Activated is: {Motor[UnpackedMessageID[0]].activated}")
            """


    time.sleep(1)