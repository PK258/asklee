

read_data= """select start_date, start_location_latitude, start_location_longitude, 
                        end_location_latitude, end_location_longitude, start_location, end_location 
                        from smarte_app.trip where start_location_latitude is not null and 
                        start_date >= %s and start_date < %s;"""


mapbox_token = "pk.eyJ1IjoidWJlcmRhdGEiLCJhIjoiY2pudzRtaWloMDAzcTN2bzN1aXdxZHB5bSJ9.2bkj3IiRC8wj3jLThvDGdA"