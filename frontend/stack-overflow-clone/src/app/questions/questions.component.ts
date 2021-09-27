import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.css']
})
export class QuestionsComponent implements OnInit {

  questions = [
  {
    id : 1,
    title: 'Python issue',
    body: 'Python code is not running',
    tags: 'python'
  },
  {
    id : 2,
    title: 'Java issue',
    body: 'Java code is not running',
    tags: 'Java'
  },
  {
    id : 3,
    title: 'NodeJS issue',
    body: 'NodeJS code is not running',
    tags: 'Javascript'
  }
]

  constructor() { }

  ngOnInit(): void {
  }

}
