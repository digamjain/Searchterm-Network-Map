from pyvis.network import Network
import pandas as pd
from networkmap import dbfetch

def ret1(searchterm):
    ss=searchterm
    got_net = Network(height="750px", width="100%", bgcolor="#0E1117", font_color="white",heading = "</h1><h1 style='color:white;font-family:sans-serif'>Search Term:" + str(dbfetch.get_csv(ss)))
    got_data = pd.read_csv('networkmap/depth1.csv',encoding='latin-1')
    if len(got_data) == 0:
        # print("Term not in database!")
        return(-1)

    got_data.sort_values("weight", inplace = True,ascending = False)
    got_data.drop_duplicates(subset = ["NAME","TAG","CEO","OWNER","FOUNDER","HEADQUARTER"],keep = "first", inplace = True)

    tags = got_data['TAG']
    name = got_data['NAME']
    ceo = got_data['CEO']
    owner = got_data['OWNER']
    founder = got_data['FOUNDER']
    hq = got_data['HEADQUARTER']
    weight = got_data['weight']

    tags = list(tags)
    lstlen = len(list(tags))
    for i in range(lstlen):
        a = str(tags.pop(0)).split(",")
        for j in range(len(a)):
            tags.append(a[j])

    edge_data1 = zip(set(tags), name, weight)
    edge_data2 = zip(name, ceo, weight)
    edge_data3 = zip(tags, founder, weight-1)
    edge_data4 = zip(founder, name, weight)
    edge_data5 = zip(owner, name, weight-1)
    edge_data6 = zip(name,hq,weight)
    edge_data7 = zip(founder,hq,weight-1)
    edge_data8 = zip(ceo,hq,weight-2)


    for i in [edge_data1,edge_data2,edge_data3,edge_data4,edge_data5,edge_data6,edge_data7,edge_data8]:
        for e in i:

            src = e[0]
            dst = e[1]
            w   = e[2]
            got_net.add_node(src, src, title=src)
            got_net.add_node(dst, dst, title=dst)
            got_net.add_edge(src, dst, value=w)

        neighbor_map = got_net.get_adj_list()

    for node in got_net.nodes:
       node["title"] += " <br>Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
       node["value"] = len(neighbor_map[node["id"]])
    got_net.save_graph("networkmap/output.html")
