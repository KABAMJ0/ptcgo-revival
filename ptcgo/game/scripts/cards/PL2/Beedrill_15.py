from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="84218b86-fb2c-5ad2-9f68-d81f92db3c15",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Ability(
            title="Flutter Wings",
            game_text="Once during your turn (before your attack), you may search your deck for a Grass Pok\u00e9mon, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Beedrill is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Needle Shock",
            game_text="The Defending Pok\u00e9mon is now Paralyzed and Poisoned. Ignore this effect if any of your Pok\u00e9mon used Needle Shock during your last turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)