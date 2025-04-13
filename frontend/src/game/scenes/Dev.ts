import { Scene } from 'phaser';

export class DevScene extends Scene {
    constructor() {
        super('Dev');
    }
    
    drawGrid(cellWidth: number, cellHeight: number) {
        const graphics = this.add.graphics();
        graphics.lineStyle(1, 0x333333, 1); // Light gray lines

        const width = this.cameras.main.width;
        const height = this.cameras.main.height;

        // Draw vertical lines
        for (let x = 0; x <= width; x += cellWidth) {
            graphics.moveTo(x, 0);
            graphics.lineTo(x, height);
        }

        // Draw horizontal lines
        for (let y = 0; y <= height; y += cellHeight) {
            graphics.moveTo(0, y);
            graphics.lineTo(width, y);
        }

        graphics.strokePath();
    }

    create() {
        this.drawGrid(32, 32);
        // Fetch agents data
        fetch('http://localhost:8000/agents/')
        .then(response => response.json())
        .then(data => {
            const agentsText = JSON.stringify(data, null, 2);
            const text = this.add.text(50, 20, "Agents:\n" + agentsText, {
                font: '15px monospace',
                color: '#ffffff',
                stroke: '#000000',
                strokeThickness: 5,
            });

            // Create a transparent black background
            const background = this.add.graphics();
            background.fillStyle(0x000000, 0.5); // Black with 50% alpha
            background.fillRect(text.x - 5, text.y - 5, text.width + 10, text.height + 10);

            // Set the background behind the text
            background.setDepth(text.depth - 1);
        })
        .catch(error => {
            console.error("Error fetching agents:", error);
        });

        // Fetch all thoughts data
        fetch('http://localhost:8000/all_thoughts/')
            .then(response => response.json())
            .then(data => {
                const thoughtsText = JSON.stringify(data, null, 2);
                const text = this.add.text(50, 500, "Thoughts:\n" + thoughtsText, {
                    font: '12px monospace',
                    color: '#ffffff',
                    stroke: '#000000',
                    strokeThickness: 5,
                });

                // Create a transparent black background
                const background = this.add.graphics();
                background.fillStyle(0x000000, 0.5); // Black with 50% alpha
                background.fillRect(text.x - 5, text.y - 5, text.width + 10, text.height + 10);

                // Set the background behind the text
                background.setDepth(text.depth - 1);
            })
            .catch(error => {
                console.error("Error fetching thoughts:", error);
            });
            
        /*
        const gameButton = this.add.dom(this.cameras.main.width - 100, 50).createFromHTML('<button>Game Scene</button>');
            gameButton.addListener('click');
            gameButton.on('click', () => {
                this.scene.start('Game');
            });
        
        // Add a button to step the simulation
        const stepButton = this.add.dom(100, 10).createFromHTML('<button>Step Simulation</button>');
        stepButton.addListener('click');
        stepButton.on('click', () => {
            fetch('http://localhost:8000/step_simulation/', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    console.log("Simulation Step Response:", data);
                })
                .catch(error => {
                    console.error("Error stepping simulation:", error);
                });
        });
        */
    }
}