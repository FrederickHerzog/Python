#Frederick Herzog
import folium

#Create map object centered at Houston, TX
m = folium.Map(location=[29.7632800, -95.3632700], zoom_start=10)
tooltip = 'Click for more info'

police = {'Santa Fe':[29.390659, -95.093003], 
			'Dickinson':[29.462807, -95.052177]}

#Create markers
for i in police:
	x,y = police[i]
	folium.Marker([x,y],
					popup='<strong>'+str(i)+ ' Police</strong>',
					tooltip=tooltip,
					icon=folium.Icon(icon='star')).add_to(m)

if __name__ == '__main__':
	#Generate html
	m.save('map.html')
