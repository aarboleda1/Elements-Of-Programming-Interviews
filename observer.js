// Subject
var Subject = function() {
    this.observers = [];
    this.count = 0
}

Subject.prototype = {
    subscribe: function(callback) {
        this.observers.push(callback);
    },
    unsubscribe: function(callback) {
        // Iterate through the array and if the callback is
        // found, remove it.
        for (let i = 0; i < this.observers.length; i++) {
            if (this.observers[i] === callback) {
                this.observers.splice(i, 1);
                // Once we've found it, we don't need to
                // continue, so just return.
                return;
            }
        }
    },
    publishCountChange: function() {
        // This function notifies the observers of the event
        for (let i = 0; i < this.observers.length; i++) {
            this.observers[i](this.count);
        }
    },
    incrementCount: function() {
      this.count += 1
    }
};

// Observers
var Observer1 = function (data) {
    console.log('Observer1: The count has been incremented: ' + data);
}

var Observer2 = function (data) {
    console.log('Observer2: The count has been incremented: ' + data);
}

// Notify the observers of
subject = new Subject();
subject.subscribe(Observer1);
subject.subscribe(Observer2);

// Change the state of the Subject
subject.incrementCount();

// Publish event to observers
subject.publishCountChange();
