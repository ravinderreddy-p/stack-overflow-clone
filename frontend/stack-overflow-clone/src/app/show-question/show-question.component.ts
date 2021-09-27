import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { QuestionsDataService, Questions, Answers } from '../service/data/questions-data.service';

@Component({
  selector: 'app-show-question',
  templateUrl: './show-question.component.html',
  styleUrls: ['./show-question.component.css']
})
export class ShowQuestionComponent implements OnInit {

  public question_id: number;
  public question_title: string;
  public question_body: string;
  public question_tags: string;
  public responseStatus: string;
  public answers: Answers[];
  public answers_length:  number;

  constructor(
    private route: ActivatedRoute,
    private service: QuestionsDataService,
  ) { }

  ngOnInit(): void {
    this.question_id = this.route.snapshot.params['id'];
    this.getQuestion()
  }

  getQuestion(){
    this.service.callToGetAQuestion(this.question_id).subscribe(
      response => this.handleSuccessfulResponse(response),
      error => this.handleErrorResponse(error)
    );
  }
  

  handleSuccessfulResponse(response){
    console.log(response.status)
    console.log(response.question)
    this.answers = response.question.answers;
    console.log('*********');
    console.log(this.answers);
    console.log(this.answers.length);
    this.answers_length = this.answers.length
    this.question_id = response.question.id;
    this.question_title = response.question.title;
    this.question_body = response.question.body;
    this.question_tags = response.question.tags;
  }

  handleErrorResponse(error){
    this.responseStatus = error.error.message;
    console.log(this.responseStatus);
  }
  
}
