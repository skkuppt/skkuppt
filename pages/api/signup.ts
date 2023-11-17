import Cookies from "cookies";
import * as EmailValidator from 'email-validator';
import { clientPromise, queryPromise } from "../../lib/mysql";
const { createHash } = require("node:crypto");
import { useEffect, useState } from 'react';

export default async function handler(req, res) {
  if (req.method == "POST") {


    const username = req.body["username"];
    const password1 = req.body["password"];
    const password2 = req.body["passwordagain"];
    const email = req.body["email"];
//


//
    fetch('http://localhost:8000/api/user/create', {
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username,
        password1: password1,
        password2: password2,
        email: email
      })
    })
    
      
    res.redirect("/");
  } else {
    res.redirect("/");
  }
}
