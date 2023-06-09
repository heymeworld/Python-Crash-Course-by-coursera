#!/usr/bin/env python
# coding: utf-8

# # Practice Notebook - Putting It All Together

# Hello, coders! Below we have code similar to what we wrote in the last video.  Go ahead and run the following cell that defines our `get_event_date`, `current_users` and `generate_report` methods.

# In[5]:


def get_event_date(event):
  return event.date

def current_users(events):
  # 이벤트 객체 리스트를 파라미터로 받아서
  # 날짜.시간 순으로 재정렬해
  events.sort(key=get_event_date)

  # 머신 목록을 딕셔너리 타입으로 만들어
  machines = {}

  # 이벤트 객체 리스트의 객체마다 반복해
  for event in events:
    
    # 위에 머신 목록에 이벤트 객체의 머신이 이미 있는지, 없는지
    # 없으면 추가해. key는 머신 이름, val은 비어있는 집합으로
    # 빈 집합: set() / 빈 딕셔너리: {}
    # 채워진 집합: 집합 이름 = {1, 2, 3} / 채워진 딕셔너리: {key: val, key2: val2, ...}
    if event.machine not in machines:
      machines[event.machine] = set()
    
    # 위에 머신 목록에 이벤트 객체의 머신이 있다면
    # 해당 머신의 집합에 로그인한 유저는 추가하고, 로그아웃 유저는 제거해
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
        if event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))


# No output should be generated from running the custom function definitions above.  To check that our code is doing everything it's supposed to do, we need an `Event` class.  The code in the next cell below initializes our `Event` class.  Go ahead and run this cell next.

# In[6]:


class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user


# Ok, we have an `Event` class that has a constructor and sets the necessary attributes.  Next let's create some events and add them to a list by running the following cell.

# In[7]:


# 이벤트 변수에 각 요소가 클래스 Event의 객체로 구성된 리스트를 대입했음
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]


# Now we've got a bunch of events.  Let's feed these events into our `custom_users` function and see what happens.

# In[8]:


users = current_users(events)
print(users)


# Uh oh.  The code in the previous cell produces an error message.  This is because we have a user in our `events` list that was logged out of a machine he was not logged into. Do you see which user this is? Make edits to the first cell containing our custom function definitions to see if you can fix this error message. There may be more than one way to do so. 
# <br><br>
# Remember when you have finished making your edits, rerun that cell as well as the cell that feeds the `events` list into our `custom_users` function to see whether the error message has been fixed. Once the error message has been cleared and you have correctly outputted a dictionary with machine names as keys, your custom functions are properly finished.  Great!

# Now try generating the report by running the next cell.

# In[9]:


generate_report(users)


# Whoop whoop! Success! The error message has been cleared and the desired output is produced. You are all done with this practice notebook. Way to go!
