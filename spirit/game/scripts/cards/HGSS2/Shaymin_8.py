from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d66d29ab-d322-5c9f-b9f0-60cd8ddf9746",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic", "Shaymin"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="HGSS2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=492,
    abilities=[
        Ability(
            title="Celebration Wind",
            game_text="Once during your turn, when you put Shaymin from your hand onto your Bench, you may move as many Energy cards attached to your Pok\u00e9mon as you like to any of your other Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Bloom",
            game_text="Remove 3 damage counters from each of your Pok\u00e9mon that has any Energy attached to it.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)