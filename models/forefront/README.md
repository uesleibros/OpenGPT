# ForeFront.ai

![ForeFront.ai Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0F7PGn9gAVFcnlfQK-Vc4KTMbj7DXcRGhuA&usqp=CAU)

This model has access to GPT-3.5 Turbo and GPT-4. Honestly, I consider it the best for use, it is very accurate in the answers and easy to access, apart from that it is unlimited and without problems with the application.

[How to Use](https://github.com/uesleibros/OpenGPT/tree/main/models/forefront/DOC.md)


## JWT

This is a big problem, as you know, JSON Web Token is an internet standard for creating optionally signed and/or encrypted data whose payload contains JSON that asserts some number of claims. Tokens are signed using a private secret or public/private key. Which means that whenever we make a request to the API to get the AI response, the token is changed.

![JWT Illustrator](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcdAvlunISGsCpy8F8WAeTGkvwUdCOuT3y3A&usqp=CAU)

When we get the response from the `/chat` API it asks us for this JWT token. It is constantly updated for platform security and robot attack prevention.

### Solution

As you know, the only solution so far is to create a new account for each question, which is quite time consuming. The solution is to make a request on the API that generates the JWT token and then use it, but for that, you need to have the `session_id`.

![JWT Solution](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdrx_ajRwFhXT158XH19u1B0S_Gr48mexWYw&usqp=CAU)

#### Session ID

To solve this problem, you send the request to the route that generates this new `refresh_token` or JWT if you prefer. For that, you need to use the `session_id` that is generated after creating your account, with the initials `sess_....`. Passed by the URL of the route `/tokens` the response obtained: 

```json
{
  "object": "token",
  "jwt": "jwt_token" 
}
``` 

With that you can proceed making the requests without problems, keeping this structure:

```makefile 
Step 1: Check JWT Token is Valid
Step 2: Generate new JWT Token 
Step 3: Get completion response using JWT Token 
```

### Algorithm

The algorithm that ForeFront.ai uses is `RS256`. Used a lot for these systems. They are encrypted and use a private key to perform encryption. Each JWT Token is good for something, for example. In cookies, the `__client` is what defines that you are logged into your account, containing some information, usually this format comes like this:

```js
{
  "azp": "https://chat.forefront.ai",                       //  Authorized party
  "exp": 1682912078,                                       //   Expiration time
  "iat": 1682912018,                                      //    Issued at
  "iss": "https://clerk.forefront.ai",                   //     Issuer
  "nbf": 1682912008,                                    //      Not valid before
  "sid": "sess_XXXXXXXXXXXXXXXXXXXXXXXXXXX",           //       Session ID
  "sub": "user_XXXXXXXXXXXXXXXXXXXXXXXXXXX"           //        Subject
}
```

It's tricky to be able to access and manipulate these values ​​with a well-architected system, so I owe congratulations to ForeFront.ai
