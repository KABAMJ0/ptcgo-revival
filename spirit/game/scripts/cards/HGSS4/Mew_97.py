from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8dc423dc-9c95-5feb-b80f-b768e04f247b",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Prime", "Mew"],
    subtypes=["Basic", "Prime"],
    collector_number=97,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Lost Link",
            game_text="Mew can use the attacks of all Pok\u00e9mon in the Lost Zone (both yours and your opponent's). (You still need the necessary Energy to use each attack.)",
            effect=unimplemented,
        ),
        Attack(
            title="See Off",
            game_text="Search your deck for 1 Pok\u00e9mon and put it in the Lost Zone. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)