import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export class Questions {
  constructor(
    public id: number,
    public tags: string,
    public title: string,
    public body: string
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
    return this.http.get<Questions[]>("http://127.0.0.1:5000/api/questions/all")
    // console.log("Execute Helloworld service")
  }
}
