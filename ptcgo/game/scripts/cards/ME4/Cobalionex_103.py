from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fab55eb9-7169-5cad-bec9-a2961bbe7b6a",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalionex.Name",
    display_name="Cobalion ex",
    searchable_by=["Cobalion ex", "Basic", "ex", "Cobalionex"],
    subtypes=["Basic", "ex"],
    collector_number=103,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=638,
    abilities=[
        Ability(
            title="Metal Road",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may use this Ability. Move any amount of Metal Energy from your other Pok\u00e9mon to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Power Tackle",
            game_text="During your next turn, this Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)