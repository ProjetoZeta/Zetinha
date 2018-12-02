class Tag {

	constructor({name, inner, attrs={}}={}){
		this.name = name
		this.inner = inner 
		this.attrs = attrs
	}

	stringifyAttrs() {
		var str_attrs = []
		this.attrs.forEach(function(attr){
			str_attrs.push(attr.content)
		})
		return str_attrs.join(' ')
	}

	get content(){
		return `<${this.name}${this.attrs.length ? ' '+this.stringifyAttrs() : ''}>${this.inner}</${this.name}>`
	}

};

Tag.Attribute = class {

	constructor({name, values}={}){
		this.name = name
		this.values = values
	}

	get content(){
		return `${this.name}="${this.values.join(' ')}"`
	}
}


class Schedule {

	constructor({tasks, config={'resolution': 5}}={}){
		this.config = config
		this.tasks = tasks
		this.timeBorderMax = this.getTimeBorders().max
		this.timeBorderMin = this.getTimeBorders().min
	}

	getTimeBorders() {
		var min = Number.MAX_SAFE_INTEGER
		var max = 0
		this.tasks.forEach(function(task){
			if(task.initial_date.getTime() < min)
				min = task.initial_date.getTime()
			if(task.end_date.getTime() > max)
				max = task.end_date.getTime()
		})
		return {
			'min': min,
			'max': max,
		}
	}

 	get HTMLTable() {
		return Schedule.HTMLTable({schedule: this, config: this.config})
	}

}

Schedule.Task = class {

	constructor({title, initial_date, end_date}={}) {
		this.title = title
		this.initial_date = new Date(initial_date); 
		this.end_date = new Date(end_date);
	}
}

Schedule.HTMLTable = class {

	constructor({schedule, config}={}){
		this.schedule = schedule
		this.config
	}

	htmlTimeCells(task){
		
	}

	get html(){
		
	}

}


data = [

	{
		'title': 'task0', 
		'initial_date': '2011-10-10', 
		'end_date': '2011-10-11'
	},

	{
		'title': 'task1', 
		'initial_date': '2011-10-10', 
		'end_date': '2018-10-11'
	},

	{
		'title': 'task2', 
		'initial_date': '2011-10-10', 
		'end_date': '2011-10-11'
	},

	{
		'title': 'task3', 
		'initial_date': '2011-10-10', 
		'end_date': '2011-10-11'
	},

	{
		'title': 'task4', 
		'initial_date': '2011-10-10', 
		'end_date': '2011-10-11'
	},

]

var tasks = []

data.forEach(function(elem){
	tasks.push(new Schedule.Task({title: elem.title, initial_date: elem.initial_date, end_date: elem.end_date}))
})

schedule = new Schedule({tasks: tasks})

c = new Tag.Attribute({name: 'class', values: ['hello', 'motherfucker']})
d = new Tag.Attribute({name: 'for', values: ['mean', 'ok']})

tag = new Tag({name: 'div', inner: 'hello', attrs: [c, d]})

console.log(schedule)









