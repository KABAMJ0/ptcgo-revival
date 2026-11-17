from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ff40a1f8-a614-585f-be60-73829dfd9553",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    display_name="Gloom",
    searchable_by=["Gloom", "Stage 1", "Gloom"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Semi-Blooming Energy",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may look at the top 3 cards of your deck and attach any number of Basic Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Drool",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)