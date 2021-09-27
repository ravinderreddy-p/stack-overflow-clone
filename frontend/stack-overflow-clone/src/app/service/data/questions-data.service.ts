import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

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
export class QuestionsDataService {
  public title: string;
  public body: string;
  public tags: string;

  constructor(
    private http: HttpClient
  ) { }

  httpHeader = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  } 

  callToGetAllQuestions(){
    return this.http.get<Questions[]>("http://127.0.0.1:5000/api/questions/all")
  }

  callToPostAQuestion(data){
    return this.http.post("http://127.0.0.1:5000/api/questions/add/", data)
  }
}
