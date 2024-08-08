# The Gang 4 | NoobMaster

Description: Can you find more information about his flight? Time to close John Doe's case once and for all! Author: NoobMaster Note: Flag format is `n00bz{DateOfFlight(DD/MM/YYYY)_FlightNumber_IATAairportCodeofDeparture_IATAairportCodeofArrival_ACTUALtimeOfDeparture_ACTUALtimeOfArrival_GateofDeparture_AirplaneModel}`. Example: `n00bz{26/06/2024_AA1337_DFW_SFO_13:37_15:51_32A_AirbusA319-400}`. Please use the above format to format your flag

# Write-up

From the discord server (read gang 3 for more information), we can find out some details:

1) Flight is from DEL (Delhi) to BLR (Bengaluru)
2) Flight timings are around 9:40 - 13:00
3) Airline is Air India
4) Flight date is august 3

Using these, we can find the flight (on AirIndia website) to be `AI506`. Use the Air India flight tracking website to find the remaining info!

# Flag - n00bz{03/08/2024_AI506_DEL_BLR_10:03_12:44_30_AirbusA350-900}