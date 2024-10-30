import csv

def create_sec_jamboree_womens_meet_html(csv_file, output_file):
    print(f"Reading file: {csv_file}")
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            meetdata = list(reader)
        print(f"File read successfully. Generating HTML for {csv_file}...")

        
        meet_name = meetdata[0][0]
        meet_date = meetdata[1][0]
        meet_description = ''.join(meetdata[3][:])

       
        team_data_start = 7  
        team_data_end = 14  
        athlete_data_start = team_data_end + 2  
        meet_teams = meetdata[team_data_start:team_data_end]  
        meet_athletes = meetdata[athlete_data_start:]  

   
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8"> 
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{meet_name} - Women's Junior Varsity Results</title>
            <link rel="stylesheet" href="style.css">
            <style>
                img {{
                    max-width: 24%;
                    border: solid navy 5px;
                }}
                .photo {{
                    display: inline;
                }}
            </style>
        </head>
        <body>
            <header>
                <nav>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="#meetSummary">Meet Summary</a></li>
                        <li><a href="#meetPhotoBook">Meet Photo Book</a></li>
                        <li><a href="#meetTeamResults">Meet Team Results</a></li>
                        <li><a href="#meetIndividualResults">Meet Individual Results</a></li>
                    </ul>
                </nav>
                <h1>{meet_name} - Women's Junior Varsity Results</h1>
                <h2>{meet_date}</h2>
            </header>

            <!-- Section for Meet Summary -->
            <section id="meetSummary">
                <h2>Meet Summary</h2>
                <p>{meet_description}</p>
            </section>

            <!-- Section for Meet Photos -->
            <section id="meetPhotoBook">
                <h2>Meet Photo Book</h2>
                <div id="photoBook">
                    <div class="photo">
                        <img src="secjamboree/IMG_2001.jpg" alt="{meet_name} Photo 1">
                    </div>
                    <div class="photo">
                        <img src="secjamboree/IMG_2002.jpg" alt="{meet_name} Photo 2">
                    </div>
                    <div class="photo">
                        <img src="secjamboree/IMG_2003.jpg" alt="{meet_name} Photo 3">
                    </div>
                    <div class="photo">
                        <img src="secjamboree/IMG_2004.jpg" alt="{meet_name} Photo 4">
                    </div>
                </div>
            </section>

            <!-- Section for Meet Team Results -->
            <section id="meetTeamResults">
                <h2>Meet Team Results</h2>
                <table id="meet-team-results">
                    <thead>
                        <tr>
                            <th>Place</th>
                            <th>Team Name</th>
                            <th>Score</th>
                        </tr>
                    </thead>
                    <tbody>
        """


        for team in meet_teams:
            if len(team) == 3: 
                place, team_name, score = team
                html_content += f"""
                            <tr class="team-row">
                                <td class="team-placing">{place}</td>
                                <td class="team-name">{team_name}</td>
                                <td class="team-score">{score}</td>
                            </tr>
                """

        html_content += """
                    </tbody>
                </table>
            </section>

            <!-- Section for Individual Athlete Results -->
            <section id="meetIndividualResults">
                <h2>Meet Individual Results</h2>
                <table id="meet-individual-results">
                    <thead>
                        <tr>
                            <th>Place</th>
                            <th>Name</th>
                            <th>Time</th>
                            <th>Grade</th>
                            <th>Team</th>
                            <th>Athletic.Net Link</th>
                        </tr>
                    </thead>
                    <tbody>
        """

        
        for athlete in meet_athletes:
            if len(athlete) >= 6:  
                place, grade, name, link, time, team = athlete[:6]
                html_content += f"""
                            <tr class="athlete-row">
                                <td class="athlete-placing">{place}</td>
                                <td class="athlete-name">{name}</td>
                                <td class="athlete-time">{time}</td>
                                <td class="athlete-grade">{grade}</td>
                                <td class="athlete-team">{team}</td>
                                <td class="athlete-link"><a href="{link}">Link</a></td>
                            </tr>
                """

        html_content += """
                    </tbody>
                </table>
            </section>
        </body>
        </html>
        """

       
        print(f"Writing HTML to {output_file}")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"HTML file {output_file} created successfully.")
    except Exception as e:
        print(f"Error processing file {csv_file}: {e}")


create_sec_jamboree_womens_meet_html("client-project/meets/SEC_Jamboree_#1_Womens_5000_Meters_Junior_Varsity_24.csv", "newMeet_sec_jamboree_female.html")
