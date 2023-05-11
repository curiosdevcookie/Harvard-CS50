# Internet

## TCP

TCP is a connection-oriented protocol, which means a connection is established and maintained until the application programs at each end have finished exchanging messages. It determines how to break application data into packets that networks can deliver, sends packets to and accepts packets from the network layer, manages flow control, and—because it is meant to provide error-free data transmission—handles retransmission of dropped or garbled packets as well as acknowledgement of all packets that arrive. TCP is used by application protocols such as HTTP, FTP, SMTP, Telnet, and others.

### IP

IP is a connectionless protocol, which means that there is no continuing connection between the end points that are communicating. Each packet that travels through the Internet is treated as an independent unit of data without any relation to any other unit of data. (The reason the packets do get put in the right order is because of TCP.)

### TCP/IP

TCP/IP is a suite of protocols that two computers use to communicate with each other. TCP/IP works by breaking data into chunks of packets that are sent to a destination and reassembled in the correct order when they reach the target machine.

### TCP/IP Layers

TCP/IP is a hierarchical protocol made up of interactive modules, and each of them provides specific functionality. The functionality of each layer is quite independent of the other layers. Layers above each layer are unaware of what is happening at the lower layers. Each layer has a specific function, and each layer performs its own subset of the required communication functions. The layers are stacked this way:

- Application Layer
- Transport Layer
- Internet Layer
- Network Access Layer

## Http Protocol

Http is a protocol that allows the fetching of resources, such as HTML documents. It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser. A complete document is reconstructed from the different sub-documents fetched, for instance text, layout description, images, videos, scripts, and more.

### Http

Every resource on the Web - HTML document, image, video clip, program, etc. - is identified by a Uniform Resource Identifier (URI), which is used to retrieve the resource. The URI often identifies the server name, the application name, and the specific resource, following this type of syntax:

```code
protocol://servername/applicationname/resourcename
```

For example, to retrieve a Web page from the <www.w3.org> Web site, the URI would be:

```code
http://www.w3.org/index.html
```

### Http Request

An HTTP client sends an HTTP request to a server in the form of a request message which includes following format:

```code
Request line (GET, POST, ...)
Headers
Body
```

### Http Response

The server responds with an HTTP response message:

```code
Status line (200, 404, ...)
Headers
Body
```

### Http Methods

The HTTP protocol defines a number of methods that assign semantic meaning to a request. The common HTTP methods used by most RESTful web APIs are:

- GET - Retrieve a resource. The URL contains all the necessary information the server needs to locate and return the resource.
- POST - Create a resource. POST requests usually carry a payload that specifies the data for the new resource.
- PUT - Update a resource. The payload may contain the updated data for the resource.
- DELETE - Delete a resource.

### Http Status Codes

The status code is a 3-digit code returned by a server in response to a client's request made to the server. The first digit of the status code specifies one of five standard classes of responses. The message phrases shown are typical, but any human-readable alternative may be provided. Unless otherwise stated, the status code is part of the HTTP/1.1 standard.

- 1xx: Informational - Request received, continuing process
- 2xx: Success - The action was successfully received, understood, and accepted
- 3xx: Redirection - Further action must be taken in order to complete the request
- 4xx: Client Error - The request contains bad syntax or cannot be fulfilled
- 5xx: Server Error - The server failed to fulfill an apparently valid request

### Http Headers

Http headers allow the client and the server to pass additional information with the request or the response. An HTTP header consists of its case-insensitive name followed by a colon (:), then by its value. Whitespace before the value is ignored.

### Http Cookies

An HTTP cookie (web cookie, browser cookie) is a small piece of data that a server sends to the user's web browser. The browser may store it and send it back with the next request to the same server. Typically, it's used to tell if two requests came from the same browser — keeping a user logged-in, for example. It remembers stateful information for the stateless HTTP protocol.

### Http Caching

Http caching is a mechanism that allows to store and reuse http responses in order to reduce the number of requests sent on the network. It is based on the fact that a response to the same request will be sent by the server only once and then cached by the client.

### Http Security

Http security is a set of measures that allows to protect the data exchanged between the client and the server. It is based on the fact that the communication between the client and the server is encrypted and therefore protected from eavesdropping.
Https is a protocol that allows the fetching of resources, such as HTML documents, over an encrypted connection. It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser. A complete document is reconstructed from the different sub-documents fetched, for instance text, layout description, images, videos, scripts, and more.
