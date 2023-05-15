#!/bin/sh

# Version: 6.0.0 2019-07-18

. pcp-functions
. pcp-soundcard-functions


pcp_httpd_query_string

pcp_html_head "AUDIOPHONICS ES9038 DAC INPUT" "DAC"

pcp_picoreplayers_toolbar
pcp_banner
pcp_navigation

card_id=`aplay -l | grep "I-Sabre Q2M DAC" | sed 's/card \([0-9+]\).*$/\1/'`
if test -z "$card_id"
then
	echo '<p class="error">[ ERROR ] I-Sabre Q2M DAC not detected...</p>'
	exit 0
else 

current_input=`amixer sget -c $card_id 'I2S/SPDIF Select' | grep Item0: | sed "s/^.*\?'\(.*\)'/\1/g"`
current_filter=`amixer sget -c $card_id 'FIR Filter Type'  | grep Item0: | sed "s/^.*\?'\(.*\)'/\1/g"`

case "$SUBMIT" in
		"");;
        toggle)
	
			if [ "$current_input" = "I2S" ]
			then 
				amixer sset -c $card_id 'I2S/SPDIF Select' SPDIF > /dev/null
			else 
				amixer sset -c $card_id 'I2S/SPDIF Select' I2S > /dev/null
				
			fi
			current_input=`amixer sget -c $card_id 'I2S/SPDIF Select' | grep Item0: | sed "s/^.*\?'\(.*\)'/\1/g"` 
			echo "<p class='ok'>[ TOGGLE INPUT ] ${current_input} </p>"
        ;;
		next_filter)
			filters=`amixer sget -c $card_id 'FIR Filter Type' | grep Items | sed "s/^.*Items:[^']*'\(.*\)'/\1/; s/' '/\n/g"` 
			length=`echo "$filters" | wc -l`
			current_index=`echo "$filters" | grep -wxn "$current_filter" | sed 's/:.*$//'`
			next_index=`echo "($current_index) % ($length) +1" | bc`
			next_filter=`echo "$filters" | sed "$next_index""q;d"`
			amixer sset -c $card_id 'FIR Filter Type' "$next_filter"  > /dev/null
			urlsafenewfilter=`echo $next_filter | sed -e "s/ /%20/g"`
			current_filter=$next_filter
			echo "<p class='ok'>[ CYCLE FILTER ] ${current_filter} </p>"
		;;
        *)
                echo '<p class="error">[ ERROR ] Invalid case argument.</p>'
        ;;
esac


echo ''
echo '<table class="bggrey">'
echo '  <tbody>'
echo '    <tr>'
echo '      <td>'
echo '        <div class="row">'
echo '          <fieldset>'
echo '            <legend>Audiophonic ES9038 DAC Input Selection</legend>'
echo '            <table class="bggrey percent100">'
echo '              <tbody>'

echo '                <tr class="even">'
echo '                  <td class="column150 center">'
echo '                    <form name="Update" action="apessq2m.cgi" method="get">'
echo '                      <button type="submit" name="SUBMIT" value="toggle">Toggle</button>'
echo '                    </form>'
echo '                  </td>'
echo '                  <td>'
echo '                    <p>Current Input : '
echo "$current_input"
echo " 						<a id='input_morea' class='moreless' href='#' onclick=\"return more('input_more')\">more&gt;</a>"
echo '                    </p>'
echo '                    <div id="input_more" class="less">'
echo '                      <p>Toggles between I2S and SPDIF Inputs</p>'
echo '                    </div>'
echo '                  </td>'
echo '                </tr>'

echo '                <tr class="odd">'
echo '                  <td class="column150 center">'
echo '                    <form name="Update" action="apessq2m.cgi" method="get">'
echo '                      <button type="submit" name="SUBMIT" value="next_filter">Next filter</button>'
echo '                    </form>'
echo '                  </td>'
echo '                  <td>'
echo '                    <p>Current Filter : '
echo "$current_filter"
echo " 						<a id='filter_morea' class='moreless' href='#' onclick=\"return more('filter_more')\">more&gt;</a>"
echo '                    </p>'
echo '                    <div id="filter_more" class="less">'
echo '                      <p>Cycles between DAC filters</p>'
echo '                    </div>'
echo '                  </td>'
echo '                </tr>'

echo '			  </tbody>'
echo '            </table>'
echo '          </fieldset>'
echo '        </div>'
echo '      </td>'
echo '    </tr>'
echo '  </tbody>'
echo '</table>'
echo ''

fi



pcp_html_end