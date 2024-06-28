# Treasury Guild Operation Steps outline for treasury guild transaction building process



**Formating Taxonomy:**

Underscore or Underlined words are buttons: Button Name

Sometimes buttons are colored , the matching color button can be found in Treasury Manager

Excel Sheets are colored with its respective Sheet Color

Excel Columns are colored with its respective Column Name Color

Orange Columns are mandatory Columns

Yellow Columns are automated Support Columns

Grey Columns are Imported Support Columns

Commonly mistaken or important information is highlighted in strong yellow



Operation Session Recording, when going through all these steps: https://youtu.be/U-WAF4DFOTA

## Import Data to Treasury Manager

### CLEAR

Deletes  Insert Contributions Sheet Data Table

Closes all Extra Columns.

Resets all filters or provides filtering options for all columns

Resets all kinds of potential UI issues related to buttons.



### Open Dework Exporter

Visit https://public-dework-exporter.netlify.app



Export csv files of all the rows that have more than 0 Fund Request (column Fund Request)

**NB!** Do only one at the time ****

**NB!** Verify if the Export csv button downloaded the file! (Dework might be lagging)



**Unique Errors:**

Nigerian networks internet service provider allows the use of dework without VPN but the normal mobile network service providers don’t allow thus the use of vpns

Session Timeouts, If the page loads for more than 2 minutes, try a refresh



**if still doesn’t work**

then Check the Dework platform itself to Export files

https://app.dework.xyz/singularitynet-ambas/treasury-guild-87240/settings/general

You can find more guidelines about exporting on Dework PBL in the 2nd chapter: https://instance-dework-pbl.vercel.app/course/module/301/3015



### Manage Import Folder

**Set-Up and Configurations**

Import into Excel - Requires **Desktop** Drive Access ( treasuryguildoperations@gmail.com )

Excel might require a license (The Swarm can create credentials)



Your Date Format has to be the same as all other Treasury Operators

The Computer Date format has to be dd.MM.yyMiro Board guide for Windows OS: https://miro.com/app/board/uXjVOiDYnHs=/?moveToWidget=3458764531567467710&cot=14



Configure Manage Import Folder.

Include the Download Folder in the conf sheet to recognize importable files from Download Folder (List Folder Paths - Download Folder Locations)

****

**Import Manager**

Use the arrow buttons between lists to move files to Import Folder Files. (right side)

Use the Load All Files button to load all the Excel CSV reports into Excel.



**Potential Critical Errors**

Retry when date format errors comes up (they come from errors people do in task name)

Internal errors or compute errors. Press the End button on the error pop-up to stop scripts.



### DELETE Selected Rows

Deletes visible rows in Insert Contributions Sheet Data Table



Usually skipped if no critical contribution rows (fully red rows) are at present and filtered in



**Dework Operations**

Go to Dework and move all tasks to Done that were imported.

**NB!** Only the tasks that are in the Review stage and are audited or have a Fund Request Tag.

## Check Task Dates

Make Date related Extra Columns visible ( Suggested Date and Task Creation Date )

Above the column ribbon D, there is a + sign to do that. - sign would close the grouped column.



Check for date column errors (red color) and warnings (yellow color).



Update the Date Column if necessary using the Task Name or Proof Link for extra information.

You can use the Open Proof Link button to open selected Dework link (selected proof is highlighted)



## Check Task Associations

If there are new workgroups, guilds or changes requested from said groups.

Verify if the Group Name and Sub Group are correctly automated.

### FILTER

Closes all Extra Columns.

Resets all filters or provides filtering options for all columns

Resets all kinds of potential UI issues related to buttons.

## Check Label suggestions



**Configurations**

In the conf sheet, you can automate the suggestions for labels.

More info about suggested labels https://instance-dework-pbl.vercel.app/course/module/201/2018





### FILTER With Task Labels

Opens Extra Columns

Creates Yellow Buttons for adding tags from Label Suggestions to Task Labels

Filters Task Labels and in a way that leaves out all blanks

****

**Task Label Operations:**

Suggestion: Zoom Excel to see both Task Label and Task Name column at the same time for easier management



Check all Task Labels against the name and if see if they make sense

Here is a list of commonly used Tags and their meaning: https://instance-dework-pbl.vercel.app/course/module/201/2018



### FILTER Missing Task Labels

Opens Extra Columns

Creates Yellow Buttons for adding tags from Label Suggestions to Task Labels

Filters Task Labels and only leaves blanks



**Task Label Operations:**

Suggestion: Zoom Excel to see both Task Label and Task Name column at the same time for easier management



Select Label Suggestion values to populate insert values for Yellow Buttons .

You can use Yellow Buttons with the Label Suggestion to insert button value to Task Labels on the same selected Labels Suggestion row



Choose Task Labels for the given Task Name

Here is a list of commonly used Tags and their meaning: https://instance-dework-pbl.vercel.app/course/module/201/2018



### Add to Conf

This automates adding newly added Task Labels to Configurations for further automation.

takes you the Conf Sheet near the Table called **Defined Task Labels for Task Names**

Copies relevant info to Conf Sheet

Highlights newly added rows with yellow



**Configuration rules:**

For each of the matches that are found with the value from Matching String from Task Name that is present in the Task Names provided in import files there will be following checks

If the Group Name Req field is filled and Group Name matches the imported file Group Name

If the Sub Group field is filled and Sub Group Name match with the imported file Sub Group Name

If the above matches have been found then Task Label Keys will be used as Task Labels in Insert Contributions Sheet



**Operation Guidelines**

Change Matching String from Task Name to match with future potential task names that most likely would give similar task label results

Remove all unrecurring words and labels



Delete Matching String from Task Name where automation is not applicable or necessary.



Use the FILTER Below Table button to

Delete all rows in the table that have no values in Matching String from Task Name

Sort Column Matching String for Task Name by Z>A

Remove highlight colors



Move back to Insert Contributions Sheet to continue with the rest of the process

## Check Task Names

### Refresh Return Messages

Recheck all rows for errors and warnings

### FILTER Return Message

It filters in only the same errors, making tackling the same type of errors easier.

### CLEAR Return Messages

Delete visible error messages on the Return Message Column. Used if errors are fixed or checked and you no longer want it to show up when pressing the FILTER Return Message button



**Potential Errors**

Sometimes, the Task Name is already in use, or there are duplicates



If the task seems to be a one-time or unique contribution

You can use the Add Date to Task Name button to write the Date Column value into the Task Name to make it unique.



If the task seems to be a recurring contribution

You can use the  Add Task Name to Conf … button to allow similar task names to be rewarded again.



Task Name can not have non-ASCII characters

Sometimes they have weird characters in the Task Name

Delete those weird characters in the Task Name



Task Name can not have an upper commaRemove Upper commas from the Task Name



## Check Wallet Addresses



### Find Wallet Owners

Opens Extra Columns

This will check wallet addresses added to the Treasury Guild Wallet Address registration form or through the dApp connector

If there are any matches with Dework/Discord Names, they will be written in Treasury Manager and highlighted in yellow.

More info: https://instance-dework-pbl.vercel.app/course/module/101/1017



If there are no Wallet Owner Matches, then move to create new accounts with the Register Wallet Owner button



### Register Wallet Owner

Use the button to create Accounts that connect Dework Names and Cardano Wallet Addresses



Select Dework Name from the left list for which you want to create an account.

Use Dework Name button will help you copy paste the Dework Name as Wallet Name

The Wallet Name Field will filter similar names in the Select Wallet Name list.



If the Select Wallet Name list includes the same or similar name, check if those accounts have wallet addresses in different networks.

You can select Wallet Address by clicking on the Wallet Address in the owned by list.



Above the Register Account button , you will find the final 4 values that will be linked together to create a Wallet Name

Optional - Wallet Address

Dework Name

Group Name

Wallet Name



## Check Task Rewards

All the final yellow Columns are token tickers.



Check Task Names for reward currency formatting, e.g. $ or commas don't work, look for outliers



The orange-colored reward amounts show that the calculation came from the Roles Sheet



Check if MINS tokens are provided for each contribution where applicable



You can use the Task Point Calculator button to help with MINS time calculations



## Insert Contribution Data to Data Tables

### Update Contributions

Inserts Contribution Data to Data Tables



**Errors**

Potential warnings and errors documentation on Miro Board

https://miro.com/app/board/uXjVOiDYnHs=/?moveToWidget=3458764547936957860&cot=14



## Archive work

### Archive All Files

Creates a new copy of the Insert Contributions data table and archives it

Clears the Insert Contributions data table and Token Columns

Hides all the Extra Columns

Moves all the import files to archive and timestamps them



Press Archive All Files if you imported all files at the beginning of the process.

### Archive Contributions

Creates a new copy of the Insert Contributions data table and archives it

Clears the Insert Contributions data table and Token Columns

Hides all the Extra Columns



Press Archive Contributions if you manually inserted values to the Insert Contributions sheet



## Create the Transaction JSON

Move to the Bundle Transactions sheet .

### Refresh

Loads all unrewarded contributions inserted to Treasury Manager





**Verify and Update Token prices**

You can verify Token Exchange Rate values by selecting the cell value next to it.It will turn green, highlighting that the Token Exchange Rate is set and verified.



### Filter Group

Automatically filters the first Group Name found and checks if it's presented in the Group Name  column.

Pressing the Filter Group button again will ensure that the same Group Name is not used for filtering, so you can browse through groups by clicking this button.



### Filter Addresses

Filters out all blank Wallet Addresses that can not be added to the transaction



### Convert USD to AGIX

Changes the USD values into AGIX values



### Get Totals

Calculates Contributor amount and calculates transaction costs



### Get Byte Amount

Calculates the potential Transaction size in bytes.

The maximum Transaction size is around 55000 bytes per transaction.



Calculating Byte Amount is is a heavy computational process, may take several minutes, depends on computer CPU speed.



**NB!** Try not to do anything in Excel while its calculating the byte amount



**Optional Errors:**

Task Name already in use

Make sure there are no duplicate tasks. Usually adding Task Date to task name is enough

### Reduce Contribution Rows

Organises Transactions to fit the Contributor amount given in the field Keep Contributors

And deletes all the overflowing contribution rows



An average maximum contribution amount is about 60 contributors .



### Generate JSON

Generates transaction Json



Wait and download the file, and provide it to the Treasury guild for processing, by sending it to Miroslav in the Chat of the Treasury Operation call itself



Once you have the transaction hash, click Pay For All .

Insert the transaction hash into the pop-up field to assign a transaction hash to all the transactions in the Bundle Transactions data table



All Wallet Addresses should turn green if the status is successfully updated.



## Closing Actions

**Save the Excel**

****

**Close the Excel**

