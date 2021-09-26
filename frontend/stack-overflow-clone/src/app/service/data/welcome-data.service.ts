import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export class HelloWorldBean {
  constructor(
    public message: string,
  ){}
}


@Injectable({
  providedIn: 'root'
})
export class WelcomeDataService {

  constructor(
    private http: HttpClient
  ) { }

  executeHelloWorldService() {
    return this.http.get<HelloWorldBean>("http://127.0.0.1:5000/api")
    // console.log("Execute Helloworld service")
  }
}
