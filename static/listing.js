document.addEventListener('DOMContentLoaded', function() {
    fetchJobListings();
});

async function fetchJobListings() {
    const listingsContainer = document.getElementById('job-listings');
    
    try {
        listingsContainer.innerHTML = '<div class="loading">Loading jobs...</div>';
        
        const response = await fetch('/api/job-listings');
        console.log('Response status:', response.status);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Response data:', data);
        
        if (data.error) {
            listingsContainer.innerHTML = `<div class="error">${data.error}</div>`;
            return;
        }
        
        if (!data || data.length === 0) {
            listingsContainer.innerHTML = '<div class="no-jobs">No matching jobs found. Try uploading a different CV.</div>';
            return;
        }
        
        listingsContainer.innerHTML = '';
        data.forEach((job, index) => {
            const jobCard = createJobCard(job);
            listingsContainer.appendChild(jobCard);
            
            if (index === 0) {
                jobCard.click();
            }
        });
    } catch (error) {
        console.error('Error:', error);
        listingsContainer.innerHTML = `<div class="error">Error loading jobs: ${error.message}</div>`;
    }
}

function createJobCard(job) {
    const div = document.createElement('div');
    div.className = 'job-card';
    div.innerHTML = `
        <h3 class="job-title">${job.title || 'Unknown Title'}</h3>
        <p class="company-name">${job.company_name || 'Unknown Company'}</p>
    `;
    
    div.addEventListener('click', () => {
        document.querySelectorAll('.job-card').forEach(card => {
            card.classList.remove('active');
        });
        
        div.classList.add('active');
        displayJobDetails(job);
    });
    
    return div;
}

function displayJobDetails(job) {
    const detailsContainer = document.getElementById('job-details');
    detailsContainer.innerHTML = `
        <div class="job-details-header">
            <h2>${job.title || 'Unknown Title'}</h2>
            <p class="company-name">${job.company_name || 'Unknown Company'}</p>
        </div>
        
        <div class="job-info">
            ${job.location ? `<p><strong>Location:</strong> ${job.location}</p>` : ''}
            ${job.employment_type ? `<p><strong>Employment Type:</strong> ${job.employment_type}</p>` : ''}
            ${job.industry ? `<p><strong>Industry:</strong> ${job.industry}</p>` : ''}
            ${job.external_url ? `<p><strong>Application Link:</strong> <a href="${job.external_url}" target="_blank" class="job-link">Apply Here →</a></p>` : ''}
        </div>

        <div class="job-description">
            ${job.description || 'No description available'}
        </div>
    `;
}