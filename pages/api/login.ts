import Cookies from "cookies";
import { clientPromise, queryPromise } from "../../lib/mysql";
import Link from "next/link";
const { createHash } = require("node:crypto");

export default async function handler(req, res) {
  if (req.method == "POST") {
    const username = req.body["username"];
    const password = req.body["password"];

    
     await fetch('http://localhost:8000/api/user/login', {
      method: 'post',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: new URLSearchParams({
        'username': username,
        'password': password,
        'grant_type': 'password'
      })
    }).then((response) => {
      if(response.status == 200){
        res.redirect("/"); // ppt maker 주소
      }
      else{
        res.redirect("/login?msg=Incorrect username or password");
      }
    })

  } else {
    res.redirect("/");
  }
}
