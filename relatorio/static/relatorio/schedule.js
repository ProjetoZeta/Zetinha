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
		return new Schedule.HTMLTable({schedule: this})
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

	constructor({schedule}={}){
		this.schedule = schedule
		this.config
		this.section_time = (schedule.timeBorderMax - schedule.timeBorderMin) / schedule.config.resolution
	}

	htmlTimeCells(task){
		var td_tags = []
		var resolution = this.schedule.config.resolution
		var initial_date = task.initial_date.getTime()
		var end_date = task.end_date.getTime()
		for (var i = 1; i <= this.schedule.config.resolution; i++) {
			var attr = new Tag.Attribute({'name': 'class', 'values': ['schedule-outtime']})
			var level = this.schedule.timeBorderMin + i * this.section_time			
			if ((level > initial_date) &&
				(level <= end_date))
				attr = new Tag.Attribute({'name': 'class', 'values': ['schedule-intime']})
			td_tags.push((new Tag({'name': 'td', 'inner': '', 'attrs':[attr]})).content)
		}
		return td_tags
	}

	//see https://www.w3schools.com/js/js_date_methods.asp

	get html(){
		var a = this
		var trs = []
		this.schedule.tasks.forEach(function(task){
			var c = new Tag.Attribute({'name': 'class', 'values': ['schedule-label']})
			var tag = new Tag({'name': 'td', 'inner': task.title, 'attrs': [c]})
			var tags = a.htmlTimeCells(task)
			tags.unshift(tag.content)

			var tt1 = new Tag.Attribute({'name': 'data-toggle', 'values': ['tooltip']})
			var tt2 = new Tag.Attribute({'name': 'data-html', 'values': ['true']})
			var tt3 = new Tag.Attribute({'name': 'title', 'values': ['8 dias, de 12/12/2018 a 20/12/2018']})

			trs.push((new Tag({'name': 'tr', 'inner': tags.join(''), attrs:[tt1, tt2, tt3]})).content)
		})

		var c = new Tag.Attribute({'name': 'class', 'values': ['schedule']})
		return (new Tag({'name': 'table', 'inner': trs.join('\n'), 'attrs':[c]})).content
	}	

}


data = [

	{
		'title': 'task1', 
		'initial_date': '2011-10-12', 
		'end_date': '2011-10-15'
	},

	{
		'title': 'task2', 
		'initial_date': '2011-10-10', 
		'end_date': '2011-10-11'
	},

	{
		'title': 'task3', 
		'initial_date': '2011-10-10', 
		'end_date': '2011-10-12'
	},

	{
		'title': 'task4', 
		'initial_date': '2011-10-10', 
		'end_date': '2011-10-12'
	},

	{
		'title': 'task5', 
		'initial_date': '2011-10-10', 
		'end_date': '2011-11-12'
	},

	{
		'title': 'task6', 
		'initial_date': '2011-10-23', 
		'end_date': '2011-11-1'
	},

	{
		'title': 'task7', 
		'initial_date': '2011-10-10', 
		'end_date': '2011-10-11'
	},

]

var tasks = []

data.forEach(function(elem){
	tasks.push(new Schedule.Task({'title': elem.title, 'initial_date': elem.initial_date, 'end_date': elem.end_date}))
})

schedule = new Schedule({'tasks': tasks, 'config': {'resolution': 450}})

c = new Tag.Attribute({'name': 'class', 'values': ['hello', 'motherfucker']})
d = new Tag.Attribute({'name': 'for', 'values': ['mean', 'ok']})

tag = new Tag({'name': 'div', 'inner': 'hello', 'attrs': [c, d]})

document.getElementById('schedule-table-container').innerHTML = schedule.HTMLTable.html









