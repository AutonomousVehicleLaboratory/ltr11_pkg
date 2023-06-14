#!/usr/bin/env python3

import numpy as np
from bgt60ltr11aip_ros.msg import Complex64Array
from ifxDopplerLTR11 import DopplerLTR11
import time

import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Create Device
    device = DopplerLTR11.DopplerLTR11()

    # Create and Set Config
    config_defaults = device.get_config_defaults()
    print("Configuration limits", device.get_limits())

    # print("Default Configs: ", config_defaults)

    # mode: 1                           // SPI Continuous Wave Mode or SPI Pulse Mode
    # rf_frequency_Hz: 61044000000      // Operational RF Center Frequency
    # num_of_samples: 256               // Number of samples per chirp
    # detector_threshold: 80            // 
    # prt: 1                            // Pulse repetition time expressed as index / enum   
    # pulse_width: 0                    // Pulse width expressed as index / enum
    # tx_power_level: 7                 // 
    # rx_if_gain: 8
    # aprt_factor: 4                    // Adaptive prt factor
    # hold_time: 8
    # disable_internal_detector: False

    # Customize config
    #config_defaults.num_of_samples = 1024



    device.set_config(config_defaults)
    print("Device Configured with: ", config_defaults)
    device.start_acquisition()

    #plt.ion()


    # ---- Ex1
    # fig, ax = plt.subplots()
    # line, = ax.plot([], [])
    # ax.set_xlabel('Range Bins')
    # ax.set_ylabel('Magnitude (dB)')
    # ax.set_title('Range Profile')
    # ax.grid(True)
    # ----

    # ----
    # Set the size of the range-Doppler map
    # num_range_bins = 256
    # num_doppler_bins = 256

    # # # Create the figure and axis
    # fig, ax = plt.subplots()
    # im = ax.imshow(np.zeros((num_range_bins, num_doppler_bins)), aspect='auto', cmap='hot', origin='lower')
    # ax.set_xlabel('Doppler Bins')
    # ax.set_ylabel('Range Bins')
    # ax.set_title('Range-Doppler Map')
    # fig.colorbar(im)




    # Single Code
    # plt.figure()
    # frame, metadata = device.get_next_frame()
    # avg = np.mean(frame)
    # frame = frame - avg

    # time.sleep(0.01)

    # plt.plot(frame)
    # plt.show()




    # x = [1, 2, 3]
    # y = np.array([[1, 2], [3, 4], [5, 6]])
    # plt.plot(x, y)
    # plt.show()
    # Enable interactive mode
    #plt.ion()

    # fig, ax = plt.subplots()
    # line, = ax.plot([], [])
    # ax.set_xlabel('test1')
    # ax.set_ylabel('test2')
    # ax.grid(True)

    plt.ion()
    # here we are creating sub plots
    figure, ax = plt.subplots(figsize=(10, 8))
    x = np.arange(0, 256, 1)
    y = np.zeros(256)
    ax.set_xlim(0, 256)
    ax.set_ylim(-10, 10)
    line1, = ax.plot(x, y)

    total_iterations = 0
    #while total_iterations <= 1000:
    while True:
        print("Getting data")
        frame, metadata = device.get_next_frame()
        frame = frame - np.mean(frame)
        frame = np.fft.fft(frame)
        total_iterations += 1

        # updating data values
        line1.set_xdata(x)
        line1.set_ydata(frame)
    
        # drawing updated values
        figure.canvas.draw()
    
        # This will run the GUI event
        # loop until all UI events
        # currently waiting have been processed
        figure.canvas.flush_events()
    
        time.sleep(0.1)



        # line.set_data(np.arange(0,256), frame)
        # fig.canvas.draw()
        # count = 0
        # data_stack = np.zeros((0, 256))
        # num_frames = 0
        # while num_frames < 7:
            
        #     frame, metadata = device.get_next_frame() # Frame is a numpy array of shape (num_of_samples, )
        #     print(frame.shape)
        #     print("Frame: ", frame)
        #     # metadata_dict = metadata.to_dict()
        #     # print("Chip power mode: ", "active mode " if metadata_dict['active'] else "low power mode")
        #     # print("Target Detected" if (metadata_dict['motion'] == 0) else "No Target Detected")
        #     # if metadata_dict['motion'] == 0:
        #     #     print("Approaching " if metadata_dict['direction'] else " Departing")
        #     # print("Average Power Consumption is equal to: ", metadata_dict['avg_power'])

        #     # ------------------- Ex1
        #     # raw_data = frame  # Replace with your function to obtain the latest raw data

        #     # # Perform range processing to obtain range data
        #     # range_data = np.fft.fft(raw_data)   # Range FFT

        #     # # Convert the data to dB scale for visualization
        #     # range_dB = 20 * np.log10(np.abs(range_data))

        #     # # Update the plot data
        #     # line.set_data(np.arange(0,256), range_dB)

        #     # # Adjust the plot limits if needed
        #     # # ax.set_xlim(0, len(range_dB))
        #     # # ax.set_ylim(np.min(range_dB), np.max(range_dB))

        #     # ax.set_xlim(0, 256)
        #     # ax.set_ylim(-100, 100)

        #     # # Redraw the plot
        #     # fig.canvas.draw()
        #     # -------------------- Ex1


        #     data_stack = np.vstack((data_stack, frame.reshape(1,-1)))

        #     #if num_frames < 1:
        #         #print("Frame before: ", frame)
        #         #print(frame.reshape(1,256).shape)
        #         #print("Frame after: ", frame.reshape(1,256))

        #         #print("frame: ", (num_frames, data_stack.shape))
        #         #print(data_stack)
        #     #print(data_stack.shape)

        #     # if data_stack.shape[0] >= 70:
        #     #     print("In : ", data_stack.shape)
        #     #     # Perform range processing
        #     # range_data = np.fft.fft(data_stack, axis=0)
        #     # #print(range_data)
        #     # #data_stack = np.zeros((0,256))

        #     # # Perform Doppler processing
        #     # doppler_data = np.fft.fft(range_data, axis=1)
        #     # #print(doppler_data)
        #     # # Update the range-Doppler map data
        #     # im.set_array(np.abs(doppler_data))



            # time.sleep(0.001)
            # num_frames += 1

        # total_iterations += 1

        # print("Processing data to get range information: ", (data_stack.shape))
        # range_data = np.fft.fft(data_stack, axis=0)
        # print(range_data.shape)
        # #data_stack = np.zeros((0,256))

        # # Perform Doppler processing
        # doppler_data = np.fft.fft(range_data, axis=1)
        # print(doppler_data.shape)

        # # Update the range-Doppler map data
        # im.set_array(np.abs(doppler_data))
        # # Redraw the plot
        # fig.canvas.draw()



    # Stop device and end process
    device.stop_acquisition()
    print("acquisition stopped")
    print("Sensor information: ", device.get_sensor_information())    



    
