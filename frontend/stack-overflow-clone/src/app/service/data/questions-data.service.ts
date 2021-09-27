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
export class QuestionsDataService {

  constructor(
    private http: HttpClient
  ) { }

  callToGetAllQuestions(){
    return this.http.get<Questions[]>("http://127.0.0.1:5000/api/questions/all")
  }
}
