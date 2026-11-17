from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="13812a61-fbb9-532b-901d-93cb60629a77",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronMoth.Name",
    display_name="Iron Moth",
    searchable_by=["Iron Moth", "Basic", "Future", "IronMoth"],
    subtypes=["Basic", "Future"],
    collector_number=187,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=994,
    abilities=[
        Ability(
            title="Thermal Reactor",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may move any amount of Fire Energy from your other Pok\u00e9mon to it.",
            effect=unimplemented,
        ),
        Attack(
            title="Heat Ray",
            game_text="During your next turn, this Pok\u00e9mon can't use Heat Ray.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)