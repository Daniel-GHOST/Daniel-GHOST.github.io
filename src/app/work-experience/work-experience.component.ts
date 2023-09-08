import { Component } from '@angular/core';

@Component({
  selector: 'app-work-experience',
  templateUrl: './work-experience.component.html',
  styleUrls: ['./work-experience.component.css']
})
export class WorkExperienceComponent {
  workExperience: Array<any> =[];

  constructor() { }

  ngOnInit() : void{
  let work1 = {
    fecha:"2018-2023",
    ubicacion:"Orizaba, Ver",
    puesto:"CEO",
    empresa:"Casa de la Cultura y el Arte (CCAA)",
    logros: [
      { descripcion: "Dron autonomo"},
      { descripcion: "Cluster GPU"},
    ]
  };
  let work2 = {
    fecha:"2018-2023",
    ubicacion:"Orizawa, Ver",
    puesto:"CEO",
    empresa: "Asti consultora",
    logros:[
      { descripcion: "Red Neuronal GAN"},
      { descripcion: "Cluster GPU"},
    ]
  };
  this.workExperience.push(work1);
  this.workExperience.push(work2);
  }
}

