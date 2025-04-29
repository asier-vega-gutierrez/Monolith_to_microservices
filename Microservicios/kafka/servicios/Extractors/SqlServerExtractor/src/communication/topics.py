# Importing the required libraries  
from pydoc_data.topics import topics
from kafka.admin import KafkaAdminClient, NewTopic

def create_topic(topic_name):
    # Client for server with admin credentials
    admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:29092", 
        client_id='topic_test'
    )

    # We get the topics from the server
    topics_in_server = admin_client.list_topics()
    # We create the new topic and add it if it is not in the server
    new_topic = NewTopic(name=topic_name, num_partitions=1, replication_factor=1)

    # We only add the new topic, if there is no created in the server
    if(new_topic.name not in  topics_in_server):
        # We append the list of topics
        topic_list = []
        topic_list.append(new_topic)
        admin_client.create_topics(new_topics=topic_list, validate_only=False)

        # We list the topics in the server
        topics_in_server = admin_client.list_topics()
        print('Topics in server: ')
        print(topics_in_server)