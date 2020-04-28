import itchat, time
import matplotlib.pyplot as plot


def chatProportion():
    itchat.auto_login(True)
    male = female = other = 0
    rName = "山东7群"
    roomSum = 0
    chatRooms = itchat.search_chatrooms(name=rName)
    if chatRooms is None:
        print("no this:" + rName)
    else:
        chatRoom = itchat.update_chatroom(chatRooms[0]['UserName'], detailedMember=True)
        index = 0
        mem_list = chatRoom['MemberList']
        roomSum = len(mem_list)
        for friend in mem_list:
            dis = friend['DisplayName']
            nick = friend['NickName']
            sex = friend['Sex']
            if sex == 1:
                male += 1
            elif sex == 2:
                female += 1
            else:
                other += 1
            index += 1
            print(index, dis, nick, sex)
    labels = ['男:' + str(male), '女' + str(female), '其他' + str(other)]
    sizes = [male, female, other]
    colors = ['green', 'red', 'gray']
    # 几个分量向外偏移
    explode = (0.1, 0.1, 0)
    plot.pie(sizes, explode, labels, colors, '%2.0f%%')
    plot.axis('equal')
    plot.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
    plot.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plot.rcParams['axes.unicode_minus'] = False
    plot.title("群名：" + str(rName) + "[总人数：" + str(roomSum) + "]\n" + str("(男女比例分析)"))
    plot.grid()
    plot.show()



if __name__ == "__main__":
  chatProportion()