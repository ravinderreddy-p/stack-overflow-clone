import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { QuestionsDataService } from '../service/data/questions-data.service';

@Component({
  selector: 'app-questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.css']
})
export class QuestionsComponent implements OnInit {
  public title: string;
  public body: string;
  public tags: string;

  public data = {}

  responseStatus = ''

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private questionsDataService: QuestionsDataService
  ) { }

  ngOnInit(): void {
  }


  submitQuestion(){
    this.data = {
      'title': this.title,
      'body': this.body,
      'tags': this.tags,
      'user_id': sessionStorage.getItem('id')
    }
    this.questionsDataService.callToPostAQuestion(this.data).subscribe(
      response => this.handleSuccessfulResponse(response),
      error => this.handleErrorResponse(error)
    );
  }

  handleSuccessfulResponse(response){
    this.responseStatus = response.success;
    this.router.navigate(['dashboard']);
  }

  handleErrorResponse(error){
    this.responseStatus = error.error.message;
  }

}
