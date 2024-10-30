A Disposable in VS Code (and generally in programming) is an object that represents something that needs to be cleaned up or released when it's no longer needed. Think of it like a contract that says "I'll clean up after myself when I'm done."

Here's a practical explanation:

```typescript
// 1. Basic Disposable Example
const disposable = vscode.window.onDidChangeActiveTextEditor((editor) => {
    console.log('Editor changed!');
});

// Later when you don't need it anymore:
disposable.dispose(); // Cleans up the event listener


// 2. Creating your own Disposable
class MyService implements vscode.Disposable {
    private eventListener: vscode.Disposable;
    private timer: NodeJS.Timer;

    constructor() {
        // Set up some resources
        this.eventListener = vscode.workspace.onDidChangeTextDocument(() => {
            console.log('Document changed!');
        });
        this.timer = setInterval(() => {
            console.log('Tick');
        }, 1000);
    }

    dispose() {
        // Clean up all resources
        this.eventListener.dispose();
        clearInterval(this.timer);
    }
}
```

Common use cases for Disposables:
1. **Event Listeners**
   ```typescript
   const listener = vscode.workspace.onDidSaveTextDocument(() => {});
   // Later: listener.dispose();
   ```

2. **Resource Management**
   ```typescript
   const statusBar = vscode.window.createStatusBarItem();
   // Later: statusBar.dispose();
   ```

3. **Multiple Disposables**
   ```typescript
   // VS Code provides a DisposableStore
   const disposables = new vscode.DisposableStore();
   
   disposables.add(vscode.window.onDidChangeActiveTextEditor(() => {}));
   disposables.add(vscode.window.onDidChangeTextEditorSelection(() => {}));
   
   // Dispose all at once
   disposables.dispose();
   ```

4. **Extension Cleanup**
   ```typescript
   export function activate(context: vscode.ExtensionContext) {
       // Add to subscriptions to auto-dispose when extension deactivates
       context.subscriptions.push(
           vscode.commands.registerCommand('myExtension.someCommand', () => {})
       );
   }
   ```

Think of Disposables like:
- A subscription you can cancel
- A rental that needs to be returned
- A cleanup contract for resources
- A way to prevent memory leaks

When to use:
- When you create event listeners
- When you allocate resources that need cleanup
- When you create UI elements
- When you start background processes
