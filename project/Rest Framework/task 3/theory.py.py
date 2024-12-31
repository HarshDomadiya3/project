# 1) What is Serialization?

#     Serialization is the process of converting complex data types (like Django models or QuerySets) into a format that can be easily rendered into JSON, XML, or other content types. 
# This is essential for APIs because APIs typically communicate using formats like JSON, 
# which can be transferred over the network and understood by web browsers or mobile applications.

# 2) Why Convert QuerySets to JSON? 

#     - APIs: JSON is the standard format for RESTful APIs and web communication.
#     - Frontend Communication: JavaScript or frontend frameworks (React, Angular, etc.) expect JSON data for rendering.
#     - Data Portability: JSON allows easy sharing of data across different platforms.

# 3) Using Serializers in Django REST Framework (DRF)

#     In Django REST Framework (DRF), serializers are used to convert complex Python objects such as Django models or QuerySets into JSON, which can be easily rendered into HTTP responses.
# They also perform the reverse operation: validating and converting input data into Python objects.