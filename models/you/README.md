# You.com

![You.com](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/You.com_Logo.svg/2560px-You.com_Logo.svg.png)

This is a more recommended template for getting answers, I don't recommend using it for dialogues, discussions or jokes. Uses GPT-3.5 Turbo with Internet but designed for search engine.

[How to Use](https://github.com/uesleibros/OpenGPT/tree/main/models/you/DOC.md)

## Unauthorized

As you know, it works best on `localhost`, that is, running the code on your local machine. When hosted on a client (server), Cloudflare detects that we are a robot because of the Headers and the way the request is made. One way to resolve this is by using a Proxy.

![Proxy](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/CPT-Proxy.svg/400px-CPT-Proxy.svg.png)

## Solution

On a client, when we send the request to the server, a series of Headers are sent that indicate that we are a server and clearly this indicates that we are a robot. However, when we use a Proxy, the request is sent to it and after that it is sent to the server. In this case, the server understands that we are a `localhost` and not a client, making it easy to deceive and access the API.

![Proxy Solution](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBfLbxTOH-XwASr44j-9x7j-u7LiXYKOVcfw&usqp=CAU)

### Replit

In the case of Replit, we know that it has a serious policy with Proxies, when using it on the platform we have the project suspended for about 10 minutes. However, you can use **Vercel**, which has Back-End support and runs Python applications.
You can learn how to make your python application in Vercel at the following link: https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python

### Structure

You can use this site to get proxies and use them in your requests: https://proxy2.webshare.io

The format you will use to work is as follows: `http://username:password/@ip:port`

And JSON:

```json
{
  "http": "proxy",
  "https": "proxy"
}
```
