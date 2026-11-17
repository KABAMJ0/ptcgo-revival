from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26591097-3a80-564a-9aa3-b821da8e3c79",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansQuilava.Name",
    display_name="Ethan's Quilava",
    searchable_by=["Ethan's Quilava", "Stage 1", "EthansQuilava"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EthansCyndaquil.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Bonded by the Journey",
            game_text="Once during your turn, you may search your deck for an Ethan's Adventure card, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
        ),
    ],
)