# SNET Archives Structure 

> [Comments]
> Context - Archive
> * Vanessa Cardui: Archives
>
> Context - Archive
> * Vanessa Cardui: Archives
>
> Context - Archive
> * Vanessa Cardui: I wish it was called "Archives" throughout (it's an archives thing, just a convention, it's plural) Would anyone object to it being changed?
>   - André Diamond: I'm okay with any changes. Changing the repo names will affect some code and Netlify settings, but will be able to update it no problem. Maybe early on a Monday when no one is doing meeting summaries XD
>   - Vanessa Cardui: Only if it's not fiddly to do, cos it's not that important really - it just, idk, it grates on me hahaha - and if it's changed it makes us look more "archivey" to any archives people who happen to look :-)
>   - André Diamond: I can do this, but it can take up to 2 hours to identify and fix all breaking code changes in the summary tool, doc manager, GitHub actions, Netlify and GitBook settings. It will also affect Stephen and Ubios work. They would have to update folder names in their projects I think. This feels almost like it should be a paid task on the project board if we want to do it.
>

https://github.com/SingularityNET-Archive

### The Organisation Structure



SingularityNET-Archive // Organisation

SingularityNET-Archive // Archive Repo

SingularityNET-Ambassadors // GitBook Repo

Supervisory-Council-Decentralisation-Blueprint // GitBook Repo

SingularityNET-Governance-Workgroup // GitBook Repo 

> [Comments]
> Context - -Governance-Workgroup
> * Vanessa Cardui: this should be "Governance -Gitbook" - we changed it during the meeting yesterday, is the change still not showing?
>   - André Diamond: It looks like only the about has been updated and not the repo name. Is it okay if I change the repo name to SingularityNET-Governance-GitBook
>   - Vanessa Cardui: yeh fab - thanks
>   - André Diamond: Done, I also synced the GitBook with the new repo name 👍
>

SingularityNET-Archive-GitBook // GitBook Repo

meeting-summary-tool // Code Repo

snet-doc-manager // Code Repo

LLM-Development // Code Repo

archive-oracle // Code Repo  

> [Comments]
> Context - archive
> * Vanessa Cardui: archives
>

.gitHub // Org Profile Repo



### Drilling down the Archive Repo



SingularityNET-Archive

.github // Parent folder for issue templates and GitHub actions

ISSUE_TEMPLATE // Issue Templates

Workflows // GitHub Actions

Budget // Our monthly milestone tsv files

Data // Parent folder for all automated archival data  

> [Comments]
> Context - Data
> * Vanessa Cardui: so this structure is how it *will be*, innit? not now it is now?
>   - André Diamond: Yup, How it will be 👌
>   - Vanessa Cardui: cool - looks perfect
>

Snet-Ambassador-Program // Entity

Content

Onboarding-Workgroup // Sub-entity

Docs // Documents  

> [Comments]
> Context - Docs
> * Vanessa Cardui: and this is where the Blueprint doc would sit, right?
Just wondering - if we in the end did fork it, like we were discussing, so there was a "community owned" version, would that live here, or under (say) Ambassador Program/Docs? 
or would that be "TBD"?
>   - André Diamond: We could make 2 folders inside the Docs folder. Community-owned and SC-owned maybe
>   - Vanessa Cardui: yeh maybe... I mean, part of this depends on Daniel's proposal for a vote on whether there even is a new SC and whether they continue with ownershoip of the doc... and it also depends on the whole "who even is The Community".... I feel like that question is going to be an unintended side-effect of this work lol
>   - André Diamond: Yup, Can I make a community-owned folder so long to start testing, we can add the other folders when everything is clear.
>

Google-Docs // Type of document

Google-Spreadsheets

Articles

Medium

Hack-md

Videos

Youtube

Vimeo

Archives-Workgroup

Docs

Articles

Videos

Meeting-Summaries // Meeting Summaries  

> [Comments]
> Context - Meeting-Summaries
> * André Diamond: Who knows, maybe we can convince someone there to use our new summary-tool in the future
>

2023 // Year

2024

2025

Snet-Supervisory-Council // Entity

Content

Community-Owned // Sub-entity

Docs

Articles

SC-Owned

Docs

Meeting-Summaries

2024

2025

Snet-Foundation // Entity

Content

Mindplex // Example Entity

Content

Meeting-Summaries

Standards

Licence

Readme.md





### Some thoughts on current structure



Should we have entity folders in Budget (Maybe we have budgets for other entities) 

> [Comments]
> Context - entity folders in Budget (Maybe we have budgets for other entities)
> * Vanessa Cardui: hmmm I dunno. I guess this depends on the answer to Esther's query that u just posted. I mean - it is more transparent that way I guess, but is it more fiddly? And is that kind of transparency what we need?
>   - André Diamond: I was thinking we could remove the Budgets folder, because we already have milestones in our project board that shows all the costs. Keeping this budgets folder up to date will require some automation, but the info is already available else where. We could create a project board for this SC work that also has a milestone system with costs
>   - Vanessa Cardui: we could yeh - I mean atm the SC work is on the QA-DAO board, but that isn't public, right?
>   - André Diamond: Yup, we should create a public QADAO project board specifically for this work and start tracking it there. Can also be a way to make people aware of QADAO
>

Should we rename the Docs folder to something else, because we can have all different kind of things in there. ( Working things or links😅 ) or we keep it “Docs” and create another folder for all the other weird things like miroboard or youtube links. Still not exactly sure how to handle them, but suppose we do need a folder for them as well. 

> [Comments]
> Context - rename the Docs folder to something else, because we can have all different kind of things in there
> * Vanessa Cardui: hi André; to me, that'd be totally your call, depending on practicality - what's easiest to work with for what you're doing. If it's a faff to have Working Thingies :-) that aee not actual docs going in to that folder, then absolutely, separate it out.
>   - André Diamond: Yup, makes sense. Will separate them
>   - Vanessa Cardui: 👍
>

Here’s an example of modified structure - SingularityNET-Archive/Data/Snet-Ambassador-Program/Content/Archives-Workgroup/Docs/GoogleDocs/1MIItGDkPIBMA6x-_rvIaWvpRE_sKkkz9TdEhao_MVwM.md

