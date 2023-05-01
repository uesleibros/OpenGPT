# ForeFront.ai

![ForeFront.ai Logo](https://cdn.storifyme.com/accounts/cashify-in-0561312/assets/f-628193922a4d18f47da82090_webclip-51371682183445132.png?t=1682184113000)

This model has access to GPT-3.5 Turbo and GPT-4. Honestly, I consider it the best for use, it is very accurate in the answers and easy to access, apart from that it is unlimited and without problems with the application.

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
  "jwt": "token" 
}
``` 

With that you can proceed making the requests without problems, keeping this structure:

```makefile 
Step 1: Check JWT Token is Valid
Step 2: Generate new JWT Token 
Step 3: Get completion response using JWT Token 
```