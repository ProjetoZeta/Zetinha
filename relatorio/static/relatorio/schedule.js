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
			var attr = new Tag.Attribute({'name': 'bgcolor', 'values': ['#FF0000']})
			var level = this.schedule.timeBorderMin + i * this.section_time			
			if ((level > initial_date) &&
				(level <= end_date))
				var attr = new Tag.Attribute({'name': 'bgcolor', 'values': ['#00FF00']})
			td_tags.push((new Tag({'name': 'td', 'inner': '&nbsp;', 'attrs':[attr]})).content)
		}
		return td_tags
	}

	get html(){
		var a = this
		var trs = []
		this.schedule.tasks.forEach(function(task){
			var tag = new Tag({'name': 'td', 'inner': task.title})
			var tags = a.htmlTimeCells(task)
			tags.unshift(tag.content)
			trs.push((new Tag({'name': 'tr', 'inner': tags.join('')})).content)
		})

		var c = new Tag.Attribute({'name': 'cellspacing', 'values': ['0']})
		var d = new Tag.Attribute({'name': 'cellpadding', 'values': ['0']})

		return (new Tag({'name': 'table', 'inner': trs.join('\n'), 'attrs':[c,d]})).content
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
		'end_date': '2011-10-11'
	},

	{
		'title': 'task2', 
		'initial_date': '2011-10-10', 
		'end_date': '2011-10-12'
	},

	{
		'title': 'task2', 
		'initial_date': '2011-10-10', 
		'end_date': '2011-11-12'
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
	tasks.push(new Schedule.Task({'title': elem.title, 'initial_date': elem.initial_date, 'end_date': elem.end_date}))
})

schedule = new Schedule({'tasks': tasks, 'config': {'resolution': 200}})

c = new Tag.Attribute({'name': 'class', 'values': ['hello', 'motherfucker']})
d = new Tag.Attribute({'name': 'for', 'values': ['mean', 'ok']})

tag = new Tag({'name': 'div', 'inner': 'hello', 'attrs': [c, d]})

document.getElementById('table-container').innerHTML = schedule.HTMLTable.html









