import streamlit as st
import pandas as pd

view1, view2 = st.tabs(["Insurer Terms", "Test📈"])

with view1:


    st.markdown("We thank you for giving us the opportunity to obtain the most competitive terms with respect to your Motor Insurance Policy.")
   
    tab1, tab2, tab3 = st.tabs(["Fidelity Insurance", "APA Insurance",  "Metropolitan Cannon"])
    
    with tab1:
        fidelity = [['Basic Premium', '3.5%'], ['Minimum Premium', 30000], ['Excess Protector', 'Inclusive'], ['Political Violence and Terrorism Risks', 'Inclusive'], ['Loss Of Use/Courtsey Car', 'Inclusive']]

        df = pd.DataFrame(fidelity, columns = ['Fidelity', 'Value'])  

        # Reset the index to remove the original one
        newdf = df.reset_index(drop=True)

        # Add custom CSS to align headers to the left
        table_html = newdf.to_html(index=False)
        
        # Display the table without the index and apply the custom CSS
        st.write(table_html, unsafe_allow_html=True)

        st.markdown( 'Windscreen and Entertainment Unit limit of 50K')

    with tab2:
        apa = [['Basic Premium', '3.5%'], ['Minimum Premium', 25000], ['Excess Protector', 'Inclusive'], ['Political Violence and Terrorism Risks', 'Inclusive'], ['Loss Of Use/Courtsey Car', 3000]]

        df2 = pd.DataFrame(apa, columns = ['APA', 'Value'])

        # Select the first row (index 0)
        newdf2 = df2.reset_index(drop=True)        

        # Display the table without the index in Streamlit
        st.write(newdf2.to_html(index=False), unsafe_allow_html=True)

        st.markdown( 'Windscreen and Entertainment Unit limit of 100K')

    with tab3:
        cannon = [['Basic Premium', 'Banded'], ['Minimum Premium', 30000], ['Excess Protector', 'Inclusive'], ['Political Violence and Terrorism Risks', 'Inclusive'], ['Loss Of Use/Courtsey Car', 3000]]

        df3 = pd.DataFrame(cannon, columns = ['CANNON', 'Value'])  

        # Reset the index to remove the original one
        newdf3 = df3.reset_index(drop=True)

        # Add custom CSS to align headers to the left
        table_html_3 = newdf3.to_html(index=False)
        
        # Display the table without the index and apply the custom CSS
        st.write(table_html_3, unsafe_allow_html=True)

        st.markdown( 'For vehicle below 2.5M a rate of 4% will apply')
        st.markdown( 'For vehicle above 2.5M a rate of 3.5% will apply')
        
        

with view2:
    reg = st.text_input('Enter Registration')            
    value = int(st.number_input('Sum Insured')) 
    loss_of_use = st.selectbox("Choose Loss Of Use Amount charged", ["Inclusive", "Excluded"])
    windscreen = int(st.number_input('Windscreen Amount Above Free Limit'))
    span = st.selectbox("Choose Length of cover", ["Annual Cover", "Pro-Rated Cover"])
    if span == "Pro-Rated Cover":                
        days = st.number_input('Number of days on cover')   
    else:
        days = 365           
    
    if value < 2500000:
        cannon_rate = 4
        cannon_premium = max(value * (cannon_rate/100) * (days/365),(30000 * (days/365)))
    elif value > 2500000:
        cannon_rate = 3.5
        cannon_premium = (value * (cannon_rate/100) * (days/365))

    if value < 2000000:
        apa_rate = 3.5
        cannon_premium = max(value * (apa_rate/100) * (days/365),(25000 * (days/365)))
    elif value > 2000000:
        cannon_rate = 3.25
        apa_rate= (value * (apa_rate/100) * (days/365))
    
    
    # if value > 0:
    #     apa_rate = 3.5
    #     apa_premium = max(value * (apa_rate/100) * (days/365), (25000 * (days/365)))
   
    if value > 0:
        fidelity_rate = 3.5               
        fidelity_one = (value * (fidelity_rate/100) * (days/365))
        fidelity_premium = max(fidelity_one, 30000)                 
    
    car_hire = 0
    car_hire_nil = 0    
    car_hire_two = 0
    fee = 100
    ex_pr = 0
    pvt_value = 0

    if st.button("Calculate"):

        if loss_of_use == 'Exluded':
            car_hire += 0
            car_hire_two += 0
        elif loss_of_use == 'Inclusive':
            car_hire_nil += 0
            car_hire += 1500
            car_hire_two += 3000       
                        
        cannon_gross_premium = (cannon_premium + car_hire_two)
        fidelity_gross_premium = (fidelity_premium + car_hire_nil)        
        apa_gross_premium = ( apa_premium + car_hire_two)
        
        cannon_levies = cannon_gross_premium * 0.0045
        fidelity_levies = fidelity_gross_premium * 0.0045
        apa_levies = apa_gross_premium * 0.0045
               

        cannon_total = ( cannon_gross_premium + fee + cannon_levies )
        fidelity_total = ( fidelity_gross_premium + fee + fidelity_levies )        
        apa_total = ( apa_gross_premium + fee + apa_levies )
        

        # Format numbers with commas for thousands
        def format_with_commas(number):
            rounded_number = round(number, 2)
            return "{:,.2f}".format(rounded_number)
            
        
        formatted_value = format_with_commas(value)

        

        formatted_cannon_premium = format_with_commas(cannon_premium)        
        formatted_fidelity_premium = format_with_commas(fidelity_premium)
        formatted_apa_premium = format_with_commas(apa_premium)
        
        
        formatted_car_hire = format_with_commas(car_hire)
        formatted_car_hire_nil = format_with_commas(car_hire_nil)
        formatted_car_hire_two = format_with_commas(car_hire_two)

        
        
        formatted_fidelity_gross_premium = format_with_commas(fidelity_gross_premium)
        formatted_apa_gross_premium = format_with_commas(apa_gross_premium)
        formatted_cannon_gross_premium = format_with_commas(cannon_gross_premium)
       

        formatted_fidelity_levies = format_with_commas(fidelity_levies)
        formatted_apa_levies = format_with_commas(apa_levies)
        formatted_cannon_levies = format_with_commas(cannon_levies)

        
        formatted_fidelity_total = format_with_commas(fidelity_total)
        formatted_apa_total = format_with_commas(apa_total)              
        formatted_cannon_total = format_with_commas(cannon_total)
       
        # Create an HTML report
        html_report = f"""
        <html>
        <head>
        <style>                
            table {{
            border-collapse: collapse;
            width: 45%;
            margin: 0.5px auto; /* Center the table */
            table-layout: fixed;
            font-size: 8px;
            font-family: Candara;
        }}

        th, td {{
            border: 1px solid black;
            padding: 2.5px; /* Increased padding for better spacing */
            text-align: left;
        }}

        th {{
            background-color: #ffffff;
            color: black; /* Text color for table headers */
        }}

        .bold {{
            font-weight: bold;
        }}

        .gross_premium {{
            border-top: 2px solid black;
            border-bottom: 2px double black;        
        }}

        .footer-row th {{
            background-color: #073980;
        }}

        img {{
            width: 100%;
            height: 45px; 
            display: block;
            margin: 0 auto;
            object-fit: cover;
        }}     
        
        </style>
        </head>
        <body>
        <table>
            <tr>
                <th colspan="8" style="background-color: #966fd6; text-align: center; font-size: 12px;">INSURANCE BROKER: GRAS SAVOYE KENYA</th>
            </tr>

            <tr>
                <th colspan="2">MOTOR PRIVATE COMPREHENSIVE</th>
                <th colspan="2"><img src="https://th.bing.com/th/id/OIP.FKycthqs_eBeEyXkHC5blAHaHa?rs=1&pid=ImgDetMain" alt="Cannon Logo"></th>                       
                <th colspan="2"><img src="https://sokodirectory.com/wp-content/uploads/2015/04/APA-Insurance1.jpg" alt="APA Logo"></th>
                <th colspan="2"><img src="https://th.bing.com/th/id/OIP.ioiH7hKhGdj9RZPSqNX7CAHaC2?rs=1&pid=ImgDetMain" alt="Fidelity Logo"></th>
                
                </tr>
            
                <tr>
                <th style="background-color: #17B169">{reg}</th>
                <th style="background-color: #17B169">Value - KES</th>
                <th style="background-color: #17B169">Rate</th>
                <th style="background-color: #17B169">Premium</th>
                <th style="background-color: #17B169">Rate</th>
                <th style="background-color: #17B169">Premium</th>
                <th style="background-color: #17B169">Rate</th>
                <th style="background-color: #17B169">Premium</th>
               
                                                                
            <tr>
                <td>Basic Premium</td>
                <td>{value}</td> 
                <td style="color:red">{cannon_rate}%</td>
                <td>{formatted_cannon_premium}</td>
                <td style="color:red">{apa_rate}%</td>
                <td>{formatted_apa_premium}</td> 
                <td style="color:red">{fidelity_rate}%</td>
                <td>{formatted_fidelity_premium}</td> 
               
            </tr>                     

            <tr>
                <td>Excess Protector</td>
                <td></td>
                <td style="color:red">Inclusive</td>
                <td >0.00</td>                       
                <td style="color:red">Inclusive</td>  
                <td >0.00</td>
                <td style="color:red">Inclusive</td>
                <td >0.00</td>              
                
                                            
            </tr>           
                                        
            <tr>
                <td>Political/Terrorism</td>
                <td></td>
                <td style="color:red">Inclusive</td>
                <td >0.00</td>                       
                <td style="color:red">Inclusive</td>  
                <td >0.00</td>
                <td style="color:red">Inclusive</td>
                <td >0.00</td>            
                                                        
            </tr>              

            <tr>
                <td>Courtesy Car</td>                        
                <td></td>
                <td style="color:red" >{loss_of_use}</td>
                <td>{formatted_car_hire_two}</td>
                <td style="color:red" >{loss_of_use}</td>
                <td>{formatted_car_hire_two}</td>
                <td style="color:red" >{loss_of_use}</td>
                <td>{formatted_car_hire_nil}</td>
               
                
            </tr>      
                
            
            <tr>
                <td>Gross Premium</td>
                <td></td> 
                <td></td>
                <td class='gross_premium'>{formatted_cannon_gross_premium}</td> 
                <td></td>
                <td class='gross_premium'>{formatted_apa_gross_premium}</td> 
                <td></td>
                <td class='gross_premium'>{formatted_fidelity_gross_premium}</td> 
                              
            </tr>      
        
            <tr>
                <td>Levies</td>
                <td></td>
                <td style="color:red">0.45%</td>
                <td >{formatted_cannon_levies}</td> <!-- Updated formatting for better readability -->
                <td style="color:red">0.45%</td>
                <td >{formatted_apa_levies}</td> <!-- Updated formatting for better readability -->
                <td style="color:red">0.45%</td>
                <td >{formatted_fidelity_levies}</td> <!-- Updated formatting for better readability -->             
                
        
            <\tr>
            
            <tr>
                <td>Policy Fee</td>
                <td></td>
                <td></td>
                <td>{fee}</td>
                <td></td>
                <td>{fee}</td>
                <td></td>
                <td>{fee}</td>
                               
                                                    
            </tr>
            
            <tr style=" border-top: 2px double black;  border-bottom: 2px double black;">
                <td class= 'bold' style="color:#152637">Total Premium</td>
                <td></td>
                <td></td>
                <td class = 'bold' style="color:#152637">{formatted_cannon_total}</td>
                <td></td>
                <td class = 'bold' style="color:#152637">{formatted_apa_total}</td>
                <td></td>
                <td class = 'bold' style="color:#152637">{formatted_fidelity_total}</td>
                                                                
            </tr>                   
        </table>
        </body>                    
        </html>"""

        
    # Create a download button with customized file name

        st.download_button(
            label=f"Download {reg}'s_premium_quote(HTML)",
            data=html_report.encode('utf-8'),
            file_name=f"{reg}_quote.html",
            mime="text/html"
        )
